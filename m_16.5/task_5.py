from typing import Annotated
from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel # для создания экземпляров класса
from typing import List
from fastapi.templating import Jinja2Templates # для html
app = FastAPI()
templates = Jinja2Templates(directory='tasks_fastapi')


class User(BaseModel):
    id: int = Path(ge=0, le=100, description='Enter user ID')
    name: str = Path(min_length=3, max_length=15, description= 'Enter user username')
    age: int = Path(ge=18, le=65, description= 'Enter user age')


db: List[User] = []

@app.get('/users', response_model= List[User])
def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('ex.html', {'request': request, 'users': db})

@app.get('/user/{user_id}', response_model= List[User])
def get_user(request: Request, user_id: int) -> HTMLResponse:
    for user in db:
        if user.id == user_id:
            return templates.TemplateResponse('ex.html', {'request': request, 'user': user})
    raise HTTPException(status_code= 404, detail= 'User not found')

@app.post('/user/{name}/{age}')
async def create_user(name: Annotated[str, Path(min_length=3, max_length=15, description= 'Enter user username')],
                      age: Annotated[int, Path(ge=18, le=65, description= 'Enter user age')]) -> User:
    new_id = len(db)
    new_user = User(id= new_id, name= name, age= age)
    db.append(new_user)
    return new_user

@app.put('/user/{user_id}/{name}/{age}')
async def update_user(user_id: Annotated[int, Path(ge= 0, le= 100, description= 'Enter user ID: ')],
                      user: User) -> User:
    for current_user in db:
        if current_user.id == user_id:
            current_user.name = user.name
            current_user.age = user.age
            return current_user
    raise HTTPException(status_code=404, detail= 'User not found')

@app.delete('/user/{user_id}')
async def delete_user(user_id: int= Path(ge= 0, le= 100, description= 'Enter user ID: ')):
    try:
        del_user = db.pop(user_id)
        return f'User {del_user.id} {del_user.name} was removed'
    except:
        raise HTTPException(status_code=404, detail= 'User not found')

@app.delete('/')
async def delete_all():
    db.clear()
    return 'All delete'




# python -m uvicorn tasks_fastapi.res_task:app
