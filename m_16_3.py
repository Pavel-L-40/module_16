from fastapi import FastAPI, Path

# CRUD запросы create read update delete

app= FastAPI()

users = {'1': 'Имя: Example, возраст: 18'} # имитация data base

#read ---------------------------------------------------------------------
@app.get('/users')
async def show_all_users():
    return users

#create -------------------------------------------------------------------
@app.post('/user/{username}/{age}')
async def add_user(username: str= Path(min_length=3, max_length= 15, description= 'Enter your user name'),
                   age: int= Path(ge= 18, le= 65, description= 'Enter your age', example= 25)):
    current_index= str(int(max(users, key=int)) + 1)
    users[current_index]= f'Имя: {username}, возраст: {age}'
    return f'User {current_index} is registered'

#update -------------------------------------------------------------------
@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, username: str= Path(min_length=3, max_length= 15, description= 'Enter your user name'),
                   age: int= Path(ge= 18, le= 65, description= 'Enter your age', example= 25)):
    users[user_id]= f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'

#delete -------------------------------------------------------------------
@app.delete('/user/{user_id}')
async def forger_user(user_id: str):
    users.pop(user_id)
    return f'user {user_id} has been deleted'


# uvicorn tasks_fastapi.task_03:app
