'''
状态码
200：表示请求成功
201:表示成功创建资源（POST接口）
204：成功，但没有返回响应体（一般 DELETE 删除后用，不返回数据）
400：请求参数非法（请求参数错误、格式不对、参数校验失败）
401：未登录 /token 缺失、登录凭证无效（没身份）
403：登录了，但是权限不够
404：查找失败（资源不存在）
409：资源冲突（比如注册时用户名已经存在，重复创建）
422：参数格式校验失败（Pydantic 校验不通过，FastAPI 参数校验失败默认返回 422）
500：服务器内部异常（代码报错）
503：服务不可用，服务挂了 / 维护中
'''
from typing import Optional

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

users = {'a':'abc',
         'b':'abc'
         }

app = FastAPI()

class UserBase(BaseModel):
    id:Optional[int] = 0
    username:str
    fullname:Optional[str] = None
    description:Optional[str] = None

class UserIn(UserBase):
    password:str

class UserOut(UserBase):
    ...

class User_Not_Found(Exception):
    def __init__(self, username):
        self.username = username
        
# @app.post('/users',status_code=201,response_model=UserOut)
# def create_user(user:UserIn):
#     user_dict = user.model_dump()
#     return user_dict

@app.get('/users/{username}',status_code=200,response_model=UserOut)
def get_user(username):
    user = users.get(username,None)
    if user:
        return user
    # 异常处理器
    # raise HTTPException(status_code=404,detail='{username} can not find')
    raise User_Not_Found(username)


# 自定义异常
@app.exception_handler(User_Not_Found)
def user_not_found(request:Request,exc:User_Not_Found):
    return JSONResponse(status_code=404,content={
        'error_code':404,
        'message':f'{exc.username} not found',
        'info':'sadfwwfga'
    })


# 处理多种异常
class ErrorMessage(BaseModel):
    error_code:int
    message:str
@app.post('/users',status_code=201,response_model=UserOut,responses={400:{'model':ErrorMessage}})
def create_user(user:UserIn):
    if users.get(user.username,None):
        error_msg = ErrorMessage(error_code=400,
        message = f'{user.username} has already existed')
        return JSONResponse(status_code=400,content=error_msg.model_dump())
    user_dict = UserIn.model_dump()
    return user_dict

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,host='0.0.0.0',port='8000')