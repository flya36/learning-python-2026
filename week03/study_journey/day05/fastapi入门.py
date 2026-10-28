from fastapi import FastAPI

# 创建FastAPI实例
app =  FastAPI()

# 定义api接口-->返回值为API接口的返回值，接口访问路径为/，请求方式为get
@app.get("/")
def root():
    return {"message": "Hello World"}

# 定义api接口-->返回值为API接口的返回值，接口访问路径为/users，请求方式为get
@app.get("/users")
def get_users():
    return [
        {"username": "alice"},
        {"username": "bob"},
    ]

# 启动FastAPI服务，监听端口8000
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)