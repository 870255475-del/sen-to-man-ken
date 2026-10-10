"""Optional BYOK chat adapter. Importing, configuring and previewing perform no I/O.

Session secrets live in this imported module, outside Ren'Py's saved store.
Only send_chat() issues a request, once, without retries or tool execution.
"""
import json
import socket
import threading
from urllib import request, error, parse

MAX_REPLY_BYTES = 1024 * 1024
MOODS = {'neutral', 'happy', 'shy', 'serious', 'sad', 'angry'}

class BridgeError(Exception):
    pass

class Session:
    def __init__(self):
        self.base_url = 'https://api.deepseek.com'
        self.model = 'deepseek-flash'
        self.api_key = ''
        self.enabled = False
        self.max_tokens = 384
        self.busy = False
        self.generation = 0
        self.lock = threading.Lock()
        self.status = '离线；尚未发出任何请求。'
        self.request_count = 0
        self.messages = []
        self.role = 'deepseek'
        self.stage = 0
        self.last_mood = 'neutral'
        self.story = {'stage':0,'branch':None,'events':[]}
        self.story_revision = 0
        self.memory_revision = 0
        self.draft = ''

    def __reduce__(self):
        # Ren'Py serializes screen scope, including FieldInputValue.object.
        # Rebind to the current module singleton, never serialize its key,
        # chat, draft or lock. Loading a game cannot restore old credentials.
        return (_current_session, ())

def _current_session():
    return session

session = Session()

# Exact loopback names only: no LAN addresses, suffix matching or DNS lookup.
LOOPBACK_HOSTS = frozenset(('localhost', '127.0.0.1', '::1'))

def completion_url(base_url):
    if not isinstance(base_url, str):
        raise BridgeError('请填写接口根地址。')
    value = base_url.strip().rstrip('/')
    if any(c.isspace() for c in value):
        raise BridgeError('接口根地址中不能有空白字符。')
    try:
        parts = parse.urlsplit(value)
        port = parts.port
        if (not parts.hostname or parts.username is not None or parts.password is not None
                or parts.query or parts.fragment or port == 0):
            raise ValueError('invalid endpoint')
    except ValueError:
        raise BridgeError('填写不含密钥、查询参数或账号密码的有效接口根地址。') from None
    if parts.scheme != 'https' and not (parts.scheme == 'http' and parts.hostname in LOOPBACK_HOSTS):
        raise BridgeError('云端接口使用 HTTPS；本地模型仅可用 localhost、127.0.0.1 或 ::1 的 HTTP。')
    return value if parts.path.rstrip('/').endswith('/chat/completions') else value + '/chat/completions'

def is_loopback_endpoint(base_url):
    # Safe while the settings field is partially edited; never resolves a host.
    try:
        return parse.urlsplit(completion_url(base_url)).hostname in LOOPBACK_HOSTS
    except BridgeError:
        return False

def validate_config(base_url, model, api_key, max_tokens):
    url = completion_url(base_url)
    if not isinstance(model, str) or not model.strip() or len(model) > 160:
        raise BridgeError('请填写服务商提供的模型名。')
    if not isinstance(api_key, str) or any(c in api_key for c in '\r\n'):
        raise BridgeError('API Key 格式无效；此操作不会发送请求。')
    if not api_key.strip() and not is_loopback_endpoint(url):
        raise BridgeError('云端接口需要自己的 API Key；只有本机接口可留空。')
    if type(max_tokens) is not int or not 64 <= max_tokens <= 1024:
        raise BridgeError('输出上限应为 64–1024。')
    return url

def make_payload(model, system_prompt, history, message, max_tokens):
    if not isinstance(message, str) or not message.strip():
        raise BridgeError('先写一句想对她说的话。')
    if len(message) > 800:
        raise BridgeError('这一条最多 800 字。')
    messages = [{'role':'system', 'content':system_prompt[:6000]}]
    for item in history[-8:]:
        if item.get('role') in {'user', 'assistant'} and isinstance(item.get('content'), str):
            messages.append({'role':item['role'], 'content':item['content'][:1200]})
    messages.append({'role':'user', 'content':message.strip()})
    return {'model':model.strip(), 'messages':messages, 'max_tokens':max_tokens, 'stream':False}

def parse_reply(content):
    if not isinstance(content, str) or not content.strip():
        raise BridgeError('模型没有返回可显示的对白。')
    text = content.strip()
    if text.startswith('```'):
        text = text.split('\n',1)[-1].rsplit('```',1)[0].strip()
    try:
        result = json.loads(text)
    except (ValueError, TypeError):
        # Text-only compatible models still speak; they cannot issue commands.
        return {'reply':content[:1200], 'mood':'neutral'}
    if not isinstance(result, dict) or not isinstance(result.get('reply'), str) or not result['reply'].strip():
        raise BridgeError('JSON 回答缺少字符串 reply；关卡未推进。')
    mood = result.get('mood', 'neutral')
    parsed = {'reply':result['reply'][:1200], 'mood':mood if isinstance(mood,str) and mood in MOODS else 'neutral'}
    # Proposal only. Local story rules validate ordering and user intent.
    event = result.get('event')
    if isinstance(event,str) and len(event)<=48 and event and all(c in 'abcdefghijklmnopqrstuvwxyz_' for c in event):
        parsed['event'] = event
    return parsed

class NoRedirect(request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise BridgeError('接口发生重定向；请填写最终接口根地址。')

def send_chat(base_url, model, api_key, system_prompt, history, message, max_tokens=384, opener=None):
    url = validate_config(base_url, model, api_key, max_tokens)
    payload = make_payload(model, system_prompt, history, message, max_tokens)
    # Official DeepSeek defaults to thinking mode. These short in-character
    # turns use non-thinking so the small output budget can reach the reply.
    # Do not send provider-specific fields to arbitrary compatible endpoints.
    if parse.urlsplit(url).hostname == 'api.deepseek.com' and model.strip() in {'deepseek-flash','deepseek-v4-pro'}:
        payload['thinking'] = {'type':'disabled'}
    body = json.dumps(payload, ensure_ascii=False).encode('utf-8')
    secret = api_key.strip()
    headers = {'Content-Type':'application/json', 'User-Agent':'SenToManKen/0.4'}
    if secret:
        headers['Authorization'] = 'Bearer ' + secret
    req = request.Request(url, data=body, method='POST', headers=headers)
    client = opener if opener is not None else request.build_opener(NoRedirect())
    try:
        with client.open(req, timeout=30) as response:
            raw = response.read(MAX_REPLY_BYTES+1)
        if len(raw) > MAX_REPLY_BYTES:
            raise BridgeError('接口返回过大；请检查接口。')
        packet = json.loads(raw.decode('utf-8'))
        if not isinstance(packet, dict):
            raise BridgeError('返回格式不是 Chat Completions 对象。')
        result = parse_reply(packet['choices'][0]['message']['content'])
        if secret:
            result['reply'] = result['reply'].replace(secret, '［密钥已隐藏］')
        return result
    except error.HTTPError as exc:
        msg = {401:'密钥无效或已过期。',403:'接口没有此模型的使用权限。',429:'服务商额度或速率受限；没有自动重试。'}.get(exc.code, '服务商返回 HTTP '+str(exc.code)+'；没有自动重试。')
        raise BridgeError(msg) from None
    except (socket.timeout, TimeoutError):
        raise BridgeError('请求超时；没有自动重试。可稍后再发送。') from None
    except error.URLError:
        raise BridgeError('无法连接接口；检查网络和根地址。') from None
    except (UnicodeError, ValueError, KeyError, IndexError, TypeError):
        raise BridgeError('返回格式不兼容；需要 Chat Completions 的 choices.message.content。') from None

def reset_role(role, greeting):
    with session.lock:
        session.generation += 1
        session.role = role
        session.stage = 0
        session.messages = [{'role':'assistant','content':greeting,'local':True}]
        session.last_mood = 'neutral'
        session.story = {'stage':0,'branch':None,'events':[]}
        session.story_revision += 1
        session.draft = ''
        # Never clear busy while an actual request is still running.

def claim_request():
    with session.lock:
        if session.busy:
            raise BridgeError('正在等待她的回答，请勿重复发送。')
        if not session.enabled:
            raise BridgeError('当前离线。配置完成并手动启用后才能发送。')
        validate_config(session.base_url,session.model,session.api_key,session.max_tokens)
        session.busy = True
        session.request_count += 1
        return session.generation

def release_request():
    with session.lock:
        session.busy = False

def advance_checkpoint(stage, action, expected_actions):
    # The local finite-state engine owns progress; API output is never evaluated.
    if stage < len(expected_actions) and action == expected_actions[stage]:
        return stage + 1
    return stage
