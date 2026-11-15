from enum import Enum
from typing import Optional

from fastapi import FastAPI, Path, Query,Body
from pydantic import BaseModel,Field

app = FastAPI()

class Gender(str,Enum):
    female = 'female'
    male = 'male'

class UserModel(BaseModel):
    user_name:str=Field(...,title='UserName',min_length=2)
    user_info:Optional[str] = Field(None,min_length=6)
    gender:Gender

@app.post('/users')
def create_user(UserModel:UserModel,username:str=Body(...,title='UserName',min_length=2)):
    user_dict = UserModel.model_dump()
    return user_dict

@app.put('/users/{user_id}')
def update_user(user_model:UserModel,user_id:int = Path(...,title='UserID',le=1000,ge=1)):
    user_dict = user_model.model_dump()
    user_dict['user_id'] = user_id
    return user_dict

@app.get('/item/{item_no}')
def get_item_no(item_no:str = Path(...,pattern='^[abc]-[\d]*$')):
    return {'message':item_no}

@app.get('/users/{user_id}')
def get_user(user_id:int,page_index:int=Query(1,title='Page_Index',ge=1),user_name:str=Body(...,title='UserName',min_length=2)):
    return {'user_id':user_id,
            'user_name':user_name,
            'page_index':page_index}