"""Independent, bounded story rules; no network, execution, model-written memory.

JSON is declarative. The importer accepts only explicitly registered built-in
files; it does not browse user paths or load executable Ren'Py/Python scripts.
"""
import json
import re
from pathlib import Path

ROLES = ('deepseek','gpt','claude','grok','minimax','kimi','gemini','qwen','glm','opencode','zcode')
TASKS = {
 'deepseek':[('一起先吃','eat_first'),('一起收灯','collect_lanterns'),('约好一起休息','rest_together')],
 'gpt':[('一起画小告示','sketch_notice'),('放下清单喝茶','share_tea'),('问她自己想画什么','ask_self_portrait')],
 'claude':[('帮忙修好旧书','repair_book'),('听她把理由说完','listen_reason'),('邀请她下班后读书','invite_reading')],
 'grok':[('帮她摆好夜市摊','open_stall'),('散场后陪她收灯','close_stall'),('认真约一次夜谈','invite_nighttalk')],
 'minimax':[('一起整理分镜','sort_storyboard'),('问她愿不愿意录音','ask_recording'),('关机后一起散步','walk_off_camera')],
 'kimi':[('整理公开目录','sort_index'),('归还取回的愿签','return_wish'),('请她写新的一页','write_new_page')],
 'gemini':[('一起核对星图','verify_starmap'),('准备备用雨伞','bring_umbrella'),('约下一次观测','invite_stargazing')],
 'qwen':[('补还代班的人情','repay_help'),('一起教摊主题字','teach_lettering'),('听她提出要求','hear_request')],
 'glm':[('帮忙布置小庭院','prepare_garden'),('赠品送完也陪收摊','stay_after_gifts'),('赴无赠品的约','visit_no_gifts')],
 'opencode':[('学会修灯的步骤','learn_repair'),('安排轮流休息','share_shift'),('没故障也来坐坐','visit_no_fault')],
 'zcode':[('询问信件的许可','ask_permission'),('一起走完送信路','walk_mail_route'),('当面收下她的信','accept_letter')],
}
ALIASES = {
 'sketch_notice':['画告示','画小告示','画海报'], 'share_tea':['喝茶','泡茶'], 'ask_self_portrait':['想画什么','自己想画'],
 'repair_book':['修书','修好旧书','修旧书'], 'listen_reason':['理由说完','听你说完','把理由说完'], 'invite_reading':['一起读书','下班后读书'],
 'open_stall':['摆摊','摆好夜市摊','开摊'], 'close_stall':['收摊','散场后陪','陪你收灯'], 'invite_nighttalk':['夜谈','晚上聊','夜里聊'],
 'sort_storyboard':['整理分镜','整理镜头'], 'ask_recording':['愿意录音','愿不愿意录音','可以录音'], 'walk_off_camera':['关机后','放下相机散步'],
 'sort_index':['整理目录','整理公开目录'], 'return_wish':['归还愿签','归还取回','还回愿签'], 'write_new_page':['写新的一页','写新页'],
 'verify_starmap':['核对星图','检查星图'], 'bring_umbrella':['备用雨伞','带雨伞','带把伞'], 'invite_stargazing':['下一次观测','一起看星','下次观星'],
 'repay_help':['还人情','补还代班','代班的人情'], 'teach_lettering':['教摊主','教题字','一起题字'], 'hear_request':['提出要求','听你的要求'],
 'prepare_garden':['布置庭院','布置小庭院'], 'stay_after_gifts':['赠品送完','陪你收摊'], 'visit_no_gifts':['没有赠品也来','无赠品的约','不送东西也来'],
 'learn_repair':['学修灯','修灯的步骤'], 'share_shift':['轮流休息','替你一班'], 'visit_no_fault':['没故障也来','没坏也来','没故障也来坐坐'],
 'ask_permission':['信件的许可','可以看信吗','允许看信'], 'walk_mail_route':['一起送信','送信路'], 'accept_letter':['收下你的信','收下她的信','当面收下'],
}

def _node(event, label, stage, aliases, context, fact, branch=None, requires=None):
    return dict(event=event,label=label,stage=stage,aliases=aliases,context=context,fact=fact,branch=branch,requires=requires)

SCENES = {}
for role, tasks in TASKS.items():
    SCENES[role] = [_node(event,label,i,ALIASES.get(event,[label]),label+'，仍在同一个日常场景。',label+'。') for i,(label,event) in enumerate(tasks)]
SCENES['deepseek'] = [
 _node('eat_first','一起先吃',0,['先吃','先开饭','一起吃饭','盛一碗','先吃白饭'],'你们先坐到桌边吃白米饭，收灯的事还没做。她把盛得最高的那碗推给你。','你们决定先一起吃饭。',branch='rice'),
 _node('lanterns_first','一起先收灯',0,['先收灯','先把灯收','先修灯','收灯再吃'],'你们先把院里的灯收好，她把最后一盏递给你，饭还在锅里保温。','你们决定先把灯收好。',branch='work'),
 _node('collect_lanterns','吃完一起收灯',1,['收灯','把灯收','修灯','收好灯'],'饭吃完了，你们一起收好了灯。她特地没把你的那盏放远。','饭后你们一起收好了灯。',requires='rice'),
 _node('share_rice','收灯后一起吃饭',1,['吃饭','盛饭','一碗白饭','一起吃','开饭'],'灯已经收好，你们才开饭。她嘴上嫌你太认真，却早留了两碗热饭。','收灯后你们一起吃了热饭。',requires='work'),
 _node('rest_together','约好一起休息',2,['一起休息','约好休息','一起歇','一起坐','坐会','歇一会'],'饭和灯都安排好了，你们约好下次也一起歇会儿。不要声称完整角色线已经通关。','你们约好一起休息。'),
]

def new_state():
    return {'stage':0,'branch':None,'events':[]}

def available(role, state, scenes=None):
    data = SCENES if scenes is None else scenes
    return [n for n in data.get(role,[]) if n['stage']==state['stage'] and (n.get('requires') is None or n['requires']==state.get('branch'))]

def _positive_intent(message, aliases):
    message=re.sub(r'\s+','',message)
    for alias in aliases:
        start=message.find(alias)
        if start < 0:
            continue
        prefix=message[max(0,start-8):start]
        if any(negative in prefix for negative in ('不要','不想','别','拒绝','不先','不让','不给','禁止','不愿','没打算','不能','不打算')) or re.search(r'不(?:会|要|再)?(?:你|我|她|我们)?$',prefix):
            continue
        # Authored, conservative intent coverage; asking about an action or
        # discussing it is not automatically performing it.
        if '？' in message or '?' in message or any(word in prefix for word in ('如果','假如','要是','说过','听说')):
            continue
        if start>0 and not any(word in prefix for word in ('我','我们','咱','一起','现在')):
            continue
        return True
    return False

def candidates(role, state, message, action=None, scenes=None):
    if not isinstance(message,str) or len(message)>800:
        return []
    nodes=available(role,state,scenes)
    # Buttons are suggestions, not a bypass. The user's sentence still needs
    # to express the action, and the model must propose the same eligible event.
    return [n['event'] for n in nodes if (action is None or n['event']==action) and _positive_intent(message,n['aliases']+[n['label']])]

def apply_proposal(role, state, event, eligible, scenes=None):
    result=dict(stage=state['stage'],branch=state.get('branch'),events=list(state.get('events',[])))
    if not isinstance(event,str) or event not in eligible:
        return result, None
    node=next((n for n in available(role,state,scenes) if n['event']==event),None)
    if node is None or event in result['events']:
        return result, None
    result['stage'] += 1  # exactly one node per received answer
    result['branch'] = node.get('branch') or result['branch']
    result['events'].append(event)
    return result, node['fact']

def restore_state(role, saved):
    # Old integer checkpoints do not provide enough branch evidence.
    state=new_state()
    if not isinstance(saved,dict) or not isinstance(saved.get('events'),list):
        return state
    for event in saved['events'][:3]:
        allowed=[n['event'] for n in available(role,state)]
        state, fact=apply_proposal(role,state,event,allowed)
        if fact is None:
            break
    return state

def context(role,state):
    if not state.get('events'):
        return '刚见面，还没有完成当前小场景的行动。'
    node=next((n for n in SCENES[role] if n['event']==state['events'][-1]),None)
    return node['context'] if node else '尚未发生新的行动。'

def response_is_current(ticket, generation, story_revision, memory_revision):
    return ticket == (generation,story_revision,memory_revision)

def epilogue(role,state):
    if state['stage']<3:
        return ''
    if role=='deepseek':
        return ('她把空碗叠好，又在你旁边放了一双筷子。\n“下次还先吃。……这双留给你。”' if state.get('branch')=='rice'
                else '她把最后一盏灯挂稳，才端出一直保温的两碗饭。\n“我有留你的份。下次别忙到忘记吃。”')
    return '今天的三件小事都做完了。她给你留了一个座位。\n本次互动小场景结束，长篇角色线仍按原创剧本制作。'

def record_fact(records, enabled, role, event):
    # Facts are selected exclusively from local authored declarations.
    result=list(records[-8:]) if isinstance(records,list) else []
    node=next((n for n in SCENES.get(role,[]) if n['event']==event),None)
    if not enabled or node is None:
        return result
    item={'role':role,'event':event,'summary':node['fact'][:120]}
    if item not in result:
        result.append(item)
    return result[-8:]

def memory_context(records, enabled, role):
    if not enabled or not isinstance(records,list):
        return ''
    facts=[]
    for item in records[-8:]:
        if not isinstance(item,dict) or item.get('role')!=role:
            continue
        node=next((n for n in SCENES.get(role,[]) if n['event']==item.get('event')),None)
        if node and node['fact'] not in facts:
            facts.append(node['fact'][:120])
    return '本地已验证的往事（不含完整聊天）：'+' '.join(facts) if facts else ''

def load_builtin_json(path, registered_paths):
    """Read only a known internal JSON file, with a small fixed schema."""
    target=Path(path).resolve()
    if target not in {Path(p).resolve() for p in registered_paths} or target.suffix.lower()!='.json':
        raise ValueError('Only explicitly registered built-in JSON scenes are accepted')
    if target.stat().st_size>65536:
        raise ValueError('Scene JSON too large')
    data=json.loads(target.read_text(encoding='utf-8'))
    if not isinstance(data,dict) or data.get('version')!=1 or not isinstance(data.get('roles'),dict):
        raise ValueError('Invalid scene schema')
    result={}
    for role,nodes in data['roles'].items():
        if role not in ROLES or not isinstance(nodes,list) or len(nodes)>12:
            raise ValueError('Invalid role or scene count')
        clean=[]
        for n in nodes:
            if not isinstance(n,dict) or set(n)-{'event','label','stage','aliases','context','fact','branch','requires'}:
                raise ValueError('Executable or unknown fields are not allowed')
            for k in ('event','label','context','fact'):
                if not isinstance(n.get(k),str) or not n[k] or len(n[k])>240:
                    raise ValueError('Invalid text field')
            if not re.fullmatch('[a-z_]{1,48}',n['event']) or type(n.get('stage')) is not int or n['stage'] not in range(3):
                raise ValueError('Invalid event or stage')
            aliases=n.get('aliases')
            if not isinstance(aliases,list) or not 1<=len(aliases)<=12 or any(not isinstance(a,str) or not 1<=len(a)<=40 for a in aliases):
                raise ValueError('Invalid aliases')
            if any(n.get(k) is not None and (not isinstance(n[k],str) or not re.fullmatch('[a-z_]{1,32}',n[k])) for k in ('branch','requires')):
                raise ValueError('Invalid branch')
            clean.append(dict(n))
        if len({n['event'] for n in clean})!=len(clean):
            raise ValueError('Duplicate events')
        result[role]=clean
    return result

def configure_builtin(game_directory):
    path=Path(game_directory).resolve() / 'story_data' / 'ai_scenes.json'
    loaded=load_builtin_json(path,[path])
    SCENES.update(loaded)
