"""Ephemeral UI session; secrets remain solely in ai_bridge.session."""
class Session:
    def __init__(self):
        self.generation=0
        self.active=False
        self.context=None
        self.state=None
        self.messages=[]
        self.draft=''
        self.busy=False
        self.status='默认离线；手动启用后，发送才调用接口。'
    def __reduce__(self):
        return (current_session, ())
session=Session()
def current_session():
    return session
def invalidate():
    session.generation+=1
    session.active=False
    session.draft=''
    session.status='对话已离开或存档已载入；旧回答不会写回。'

