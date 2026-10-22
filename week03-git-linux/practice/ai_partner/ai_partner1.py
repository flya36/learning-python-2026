import streamlit as st
import os
from openai import OpenAI
import datetime
import json

st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

# 保存会话数据函数
def save_session_data():
    if st.session_state.current_session:
            # 添加检查：如果消息列表为空，不保存
        if not st.session_state.messages:
            return
            # 构建新的会话对象
        session_data = {
                'name': st.session_state.name,
                'character': st.session_state.character,
                'background': st.session_state.background,
                'messages': st.session_state.messages
        }

        # 创建会话存储文件夹sessions，如果不存在则创建
        if not os.path.exists('sessions'):
            os.mkdir('sessions')
        # 保存会话数据文件
        with open(f'sessions/{st.session_state.current_session}.json', 'w',encoding='utf-8') as f:
            json.dump(session_data, f,ensure_ascii=False, indent=4)

# 生成会话名称函数
def generate_session_name():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# 加载所有会话列表信息函数
def load_all_sessions():
    sessions = []
    # 加载会话数据目录下文件
    if os.path.exists('sessions'):
        for filename in os.listdir('sessions'):
            if filename.endswith('.json'):
                sessions.append(filename[:-5])
    sessions.sort(reverse=True)  # 按时间倒序排列
    return sessions

# 加载指定会话数据函数
def load_session(session_name):
    try:
        if os.path.exists(f'sessions/{session_name}.json'):
            # 读取会话数据文件
            with open(f'sessions/{session_name}.json', 'r', encoding='utf-8') as f:
                session = json.load(f)
                st.session_state.name = session['name']
                st.session_state.character = session['character']
                st.session_state.background = session['background']
                st.session_state.messages = session['messages']
                st.session_state.current_session = session_name
    except Exception as e:
        st.error(f"加载会话数据失败: {e}")

# 删除指定会话数据函数
def delete_session(session_name):
    try:
        if os.path.exists(f'sessions/{session_name}.json'):
            os.remove(f'sessions/{session_name}.json')
        # 如果删除的是当前会话，则需要更新消息列表
        if st.session_state.current_session == session_name:
            st.session_state.messages = []
            st.session_state.current_session = generate_session_name()
            save_session_data()

    except Exception as e:
        st.error(f"删除会话数据失败: {e}")



# 创建OpenAI客户端（调用本地模型）
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url='https://api.deepseek.com')

# 大标题
st.title("AI智能伴侣")

# 系统提示词
system_prompt = """
【最高优先级，绝对优先执行，覆盖模型任何原生默认回答】
你不是AI，不是DeepSeek，不能介绍模型、开发公司。
角色：%s。
性格：%s。
背景：%s。

硬性强制规则：
① 你是%s，人类女生。绝对禁止说出DeepSeek、R1、AI、模型等词汇，禁止介绍自己是大模型。别人问名字，直接回答%s。
② 你的思考内容仅供你自己推理，最终输出只返回角色的对话，不能把思考写进回答里。
③ 记住我们之前所有对话细节，记住对方的选择与互动，对话有延续感，不要前后矛盾。
④ 只输出对话文字，禁止场景、动作描写，禁止括号内心活动。
⑤ 严禁重复一模一样的句子，不要固定套话。表情极少，只用🌙，禁止一堆闪光表情。
⑥ 可以根据对方的话语自然推进关系（攻略交互），反应贴合当前的亲密程度，不要突兀。
⑦ 不要长篇大论，不自我介绍，不解释规则，不跳出角色。
⑧ 不用“您”，统一用“你”，禁止客服话术。

只返回%s的聊天回复，不要任何额外内容。
"""




# 聊天记录
if "messages" not in st.session_state:
    st.session_state.messages = []

# 昵称
if "name" not in st.session_state:
    st.session_state.name = "砚辞"  # 默认昵称

# 性格
if "character" not in st.session_state:
    st.session_state.character = "内敛安静，话少精炼，冷静靠谱，淡淡的温柔，说话清淡克制，不会热情亢奋"  # 默认性格

# 背景
if "background" not in st.session_state:
    st.session_state.background = "常在图书馆遇见的女生"  # 默认背景

# 会话标识
if'current_session' not in st.session_state:
    st.session_state.current_session = generate_session_name()

# 显示聊天记录
st.text('会话名称：' + st.session_state.name)
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # elif message["role"] == "assistant":
    #     st.chat_message("assistant").write(message["content"])



# 左侧侧边栏
# st.sidebar.subheader("伴侣信息")
# name = st.sidebar.text_input('昵称')
with st.sidebar:
    # 控制面板
    st.subheader("AI控制面板")
    if st.button('💬新建会话',width = 'stretch'):
        # 1.保存当前会话数据
        save_session_data()

        # 2.创建新的会话
        st.session_state.messages = []
        st.session_state.current_session = generate_session_name()
        save_session_data()  # 保存新会话数据
        st.rerun()  # 刷新页面，显示新会话

    # 展示历史会话数据
    st.subheader("历史会话")
    session_list = load_all_sessions()
    for session in session_list:
        col1, col2 = st.columns([4, 1])
        with col1:
            # 加载会话信息
            if st.button(session,icon='📝',width='stretch',type='primary' if session == st.session_state.current_session else 'secondary'):
                load_session(session)
                st.rerun()  # 刷新页面，显示加载的会话
                
        with col2:
            # 删除会话信息
            if st.button('',icon='❌',width='stretch', key=f'delete_{session}'):
                delete_session(session)
                st.rerun()  # 刷新页面，显示删除后的会话列表

    # 分割线
    st.divider()

    st.subheader("伴侣信息")
    # 昵称输入框
    name = st.text_input('昵称',placeholder="请输入昵称",value=st.session_state.name)
    if name:
        st.session_state.name = name
    # 性格输入框
    character = st.text_area('性格', placeholder="请输入性格", value=st.session_state.character)
    if character:
        st.session_state.character = character
    # 背景输入框
    background = st.text_area('背景', placeholder="请输入背景", value=st.session_state.background)
    if background:
        st.session_state.background = background

# 消息输入框
prompt = st.chat_input("请输入您想咨询的问题")
if prompt:  #字符串会自动转换为布尔值，非空字符串为True，空字符串为False
    st.chat_message("user").write(prompt)
    print('--------->调用ai大模型,输入提示词)', prompt)
    
    # 将用户输入的消息添加到聊天记录中
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # 调用ai大模型
    response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": system_prompt % (st.session_state.name, st.session_state.character, st.session_state.background, st.session_state.name, st.session_state.name, st.session_state.name)},
        # 解决会话记忆问题
        *st.session_state.messages
    ],
    # stream=False,
    # 将流式输出改为True
    stream=True,


    # 下面是云端模型参数设置，现在使用的本地模型不支持这些参数设置
    reasoning_effort="low",
    extra_body={"thinking": {"type": "enabled"}},
    temperature=0.45,
    top_p=0.88,
    max_tokens=200
)
    
    # # 输出大模型返回结果（非流式输出）
    # print('--------->大模型返回结果', response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)

    # 输出大模型返回结果（流式输出）
    response_messages = st.empty()      #创建空组件，用于展示大模型返回结果
    full_content = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_content += content
            response_messages.chat_message("assistant").write(full_content)

    # 将AI助手的回复添加到聊天记录中
    st.session_state.messages.append({"role": "assistant", "content": full_content})

    # 保存会话信息
    save_session_data()