from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def users_list() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', examples='UrbanUser')],
                    age: Annotated[int, Path(le=120, ge=18, description='Enter age', examples='24')])-> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {user_id} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(gt=0, lt=100, description='Enter User ID', examples='1')],
                      username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', examples='UrbanUser')],
                    age: Annotated[int, Path(le=120, ge=18, description='Enter age', examples='24')]) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {user_id} has been updated"

@app.delete('/user/{user_id}')
async def delete_user(user_id: int = Path(gt=1, lt=100, description='Enter User ID', examples='1')) -> str:
    users.pop(str(user_id))
    return f'User {user_id} has been deleted'

#Запуск: uvicorn module_16_3:app --reload