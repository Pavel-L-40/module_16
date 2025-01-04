from fastapi import FastAPI, Path
from typing import Annotated

app= FastAPI()

@app.get('/user/{user_id}')
async def input_user_id(user_id: int= Path(
    ge= 1,
    le= 100,
    description= 'Enter User ID',
    example= 13
)):
    return f"Вы вошли как пользователь № {user_id}"


@app.get('/user/{username}/{age}')
async def info_user(username: Annotated[str, Path(
    min_length= 5,
    max_length= 20,
    description= 'Enter username',
    example= 'UrbanUser'
)], age: int= Path(
    ge= 18,
    le= 120,
    description= 'Enter age',
    example= 24
)):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"



# uvicorn tasks_fastapi.task_02:app
