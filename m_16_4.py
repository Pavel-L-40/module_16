from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import List

from pygments.lexer import default

app= FastAPI()

users= []

class User(BaseModel):
    id: int
    username: str
    age: int

class UserCreate(BaseModel):
    username: str= Path(...,
                        min_length=3,
                        max_length= 15,
                        description= 'Enter your user name')
    age: int= Path(...,
                   ge= 18,
                   le= 65,
                   description= 'Enter your age')


@app.get('/users', response_model= List[User])
def show_all_users() -> List[User]:
    return users

@app.post('/user/{username}/{age}', response_model= User)
def add_user(user: UserCreate) -> str:
    new_id= max((user.id for user in users), default= 0) + 1
    new_user= User(id= new_id, username= user.username, age= user.age)
    users.append(new_user)
    return new_user

@app.put('/user/{user_id}/{username}/{age}', response_model= User)
def update_user(user_new_id: int, user_new: UserCreate):
    for user in users:
        if user.id == user_new_id:
            user.username= user_new.username
            user.age= user_new.age
            return user
    raise HTTPException(status_code= 404, detail= 'User was not found')

@app.delete('/user/{user_id}', response_model= dict)
def delete_user(user_id: int):
    for item, user in enumerate(users):
        if user.id == user_id:
            users.pop(item)
            return f'User {item} deleted'
    raise HTTPException(status_code= 404, detail= 'User was not found')
