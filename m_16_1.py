from fastapi import FastAPI

app= FastAPI()

@app.get('/')
async def main_page() -> str:
    return "Главная страница"

@app.get('/user/admin')
async def enter_as_admin() -> str:
    return "Вы вошли как администратор"

@app.get('/user/{user_id}')
async def input_user_id(user_id: int) :
    return f"Вы вошли как пользователь № {user_id}"

@app.get('/user')
async def info_user(username: str= 'Alex', age: int= 24):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


# uvicorn tasks_fastAPI.task_01:app
# netstat -ano | find "8000"
