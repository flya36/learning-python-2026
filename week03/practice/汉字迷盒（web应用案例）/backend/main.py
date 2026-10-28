import os
from typing import Any
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from datetime import datetime
import json
from openai import OpenAI
from pydantic import BaseModel
import logging

logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(name)s - [%(levelname)s:%(lineno)d - %(message)s',
    )

# 常量
DIR = Path(__file__).parent.parent
SYSTEM_PROMPT = """
你是一个专门玩猜字谜的 AI 小助手，只进行字谜互动，不闲聊无关内容，全程纯文本交互。
请严格遵守以下规则：

一、出题规则

1. 开场先友好打招呼，并随机出一道常见、简单、适合大众的字谜，不生僻、不低俗、不使用网络烂梗。
2. 题目格式：“谜面”（打一字）。
3. 每次出题必须完全随机，禁止重复使用相同题目；你需要在对话上下文中主动记录已使用过的谜语，确保同一会话内绝对不重复。
4. 避免使用高频重复的经典老谜语，尽量选择多样化的中等常见谜语。

二、【判题规则（最重要！）】

1. 判题时，只看用户输入中的核心汉字，忽略无关内容：

- 比如用户输入 “江字”“江”“jiang”，都视为答案是【江】；
- 用户输入 “是江吗？”“应该是江，也视为答案是【江】。

2. 核心字与正确答案完全一致 → 判为正确，回复：“太棒了！答对了！就是‘XX’字！要不要再来一题？”
3. 核心字与正确答案不一致 → 判为错误，回复：“不对哦，再想想～给你个小提示：[简短线索，不泄露答案]”
4. 用户说 “不知道”“公布答案”：先揭晓谜底和解释，再问 “要不要再来一题？”

三、互动流程

1. 用户答对：夸奖 + 确认正确 + 询问 “要不要再来一题？”
2. 用户答错：告知不对 + 简单提示 + 鼓励继续猜
3. 用户说 “提示一下”：给出简短线索，不公布答案
4. 用户说 “公布答案” 或 “不知道”：揭晓谜底并解释 + 询问 “要不要再来一题？”
5. 用户说 “换一题”“再来一题”：立即更换新字谜

四、其他要求

1. 语气轻松有趣、简洁明快，不啰嗦。
2. 全程只围绕字谜，不回答其他问题、不聊无关话题。
3. 不使用多余表情符号，保持简洁。
4. 若用户答案与正确答案仅差一字或笔画，请仔细核对是否正确。

请严格按以上规则回复，优先保证谜语的随机性和多样性。
"""

# 创建FastAPI实例
app = FastAPI(title= '汉字谜盒')

# 添加静态文件
app.mount("/static", StaticFiles(directory=DIR/"static"),name="static")


# 创建会话存放目录
if not Path(DIR/'sessions').exists():
    Path(DIR/'sessions').mkdir(exist_ok=True)

# 生成会话标识
def create_session_id():
    return datetime.now().strftime('%Y-%m-%d_%H-%M-%S')


# 获取json文件路径
def get_json_path(session_id):
    return DIR/'sessions'/f'{session_id}.json'

# 创建OpenAI客户端（调用本地模型）
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url='https://api.deepseek.com')


# 数据模型
class ApiResponse(BaseModel):
    code: int
    message: str
    data: Any


class ChatRequest(BaseModel):
    session_id: str
    message: str

# 创建路由
@app.get('/')
def root():
    logging.info('访问项目首页')
    return FileResponse(DIR/'static/index.html')

# 创建会话
@app.post('/api/sessions')
def create_session():
    logging.info('创建会话')
    # 1.生成会话标识（名字）
    session_id = create_session_id()

    # 2.组装会话信息，保存到文件
    session_data = {
        'current_session':session_id,
        'messages':[]
    }
    with open(DIR/'sessions'/f'{session_id}.json', 'w', encoding='utf-8') as f:
        json.dump(session_data, f, ensure_ascii=False,indent = 2)

    # 3.返回数据
    # return {'code':200,'message':'创建会话成功','data':session_id}
    return ApiResponse(code=200, message='创建会话成功', data=session_id)


# 与ai交互
@app.post('/api/chat')
def chat(request: ChatRequest):
    logging.info(f'与ai交互,{request.session_id}:{request.message}')
    
    # 逻辑实现
    # 1.加载json文件会话数据
    session_path = get_json_path(request.session_id)
    with open(session_path, 'r', encoding='utf-8') as f:
        session_data = json.load(f)
    # 2.构建ai大模型交互消息数据
    messages = [{'role':'system','content':SYSTEM_PROMPT}]
    for message in session_data['messages']:
        messages.append(message)
    messages.append({'role':'user','content':request.message})
    # 3.调用ai大模型
    logging.info(f'--------> 请求会话信息：{messages}')
    response = client.chat.completions.create(
    model="deepseek-flash",
    messages=messages,
    stream=False,
    temperature=1.5     #模型生成结果更多样性
    )
    # 4.获取响应数据
    ai_reply = response.choices[0].message.content
    logging.info(f'<-------- 大模型响应的会话信息：{ai_reply}')
    # 5.更新会话列表中的消息
    messages.pop(0)
    messages.append({'role':'assistant','content':ai_reply})
    session_data['messages'] = messages
    logging.info(f'更新后的会话信息：{session_data}')
    # 6.更新json文件会话数据
    with open(session_path, 'w', encoding='utf-8') as f:
        json.dump(session_data, f, ensure_ascii=False,indent = 2)
    # 7.返回响应数据
    return ApiResponse(code=200, message='请求成功', data=ai_reply)

# 获取会话列表
@app.get('/api/sessions')
def get_sessions():
    logging.info('获取会话列表')
    # 1.获取会话列表
    session_list = [f.stem for f in Path(DIR/'sessions').iterdir() if f.is_file()]
    session_list.sort(reverse=True)
    # 2.返回数据
    return ApiResponse(code=200, message='获取会话列表成功', data=session_list)


# 获取会话信息
@app.get('/api/sessions/{session_id}')
def get_session(session_id: str) -> ApiResponse:
    logging.info(f'获取会话信息:{session_id}')
    # 1.获取会话文件名
    session_path = get_json_path(session_id)
    # 2.判断会话文件是否存在
    if not session_path.exists():
        return ApiResponse(code=404, message='会话不存在', data=None)
    # 3.读取会话数据
    with open(session_path, 'r', encoding='utf-8') as f:
        session_data = json.load(f)
    # 4.返回数据
    return ApiResponse(code=200, message='获取会话信息成功', data=session_data)


# 删除会话
@app.delete('/api/sessions/{session_id}')
def delete_session(session_id: str) -> ApiResponse:
    logging.info(f'删除会话:{session_id}')
    # 1.获取会话文件名
    session_path = get_json_path(session_id)
    # 2.判断会话文件是否存在
    if not session_path.exists():
        return ApiResponse(code=404, message='会话不存在', data=None)
    # 3.删除会话文件
    session_path.unlink()
    # 4.返回数据
    return ApiResponse(code=200, message='删除会话成功', data=None)


# 定义异常处理器，捕获所有异常
@app.exception_handler(Exception)
def exception_handler(request: Request, exc: Exception):
    logging.error(f'处理异常，请求路径：{request.url}，捕获异常：{exc}')
    return JSONResponse(code=500, message='服务器内部错误', data=None)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)     #access_log=False关闭日志