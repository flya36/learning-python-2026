import streamlit as st

# 大标题
st.title('streamlit 入门演示')
st.header('一级标题')
st.subheader('二级标题')

# 段落文字
st.write('内容：以段的形式,每个write内容是一段')

# 图片
st.image('输入图片文件地址')

#音频
st.audio('输入音频文件地址')

# 视频
st.video('输入视频文件地址')

# logo
st.logo('输入logo文件地址,出现在网页左上方')

# 表格
student_data = {
    '姓名':['fly','fqq','fzy'],
    '学号':[1,2,3],
    '成绩':[100,100,100]    
    #一个键值对是一列，key表示表头
}
st.table(student_data)

# 输入框
# 普通输入框
name = st.text_input('请输入姓名：')
st.write(f'当前姓名为：{name}')
# 密码输入框
password = st.text_input('请输入密码：',type='password')
st.write(f'当前密码为：{password}')

# 单选按钮
gender = st.radio('请选择性别',['男','女'])
st.write(f'当前选择：{gender}')