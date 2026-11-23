import pytest
from src.models.repositories.users_repository import InsertUser

@pytest.mark.asyncio
@pytest.mark.skip
async def test_user_insert():
  nome = {
    "user_name": "pereira",
    "age": 260,
    "uf": "SP"
  }

  query = InsertUser()
  await query.insert_user(nome)

@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_user():
  query = InsertUser()
  result = await query.get_user("Luigi")
  print(result)

  
@pytest.mark.asyncio
async def test_update_user():
  repo = InsertUser()
  await repo.update_user(3, {"age": 31, "uf": "RJ"})
  print(await repo.get_user("Luidenis")) 

@pytest.mark.asyncio
@pytest.mark.skip
async def test_delete_user():
  repo = InsertUser()
  deletando = await repo.delete_user(4)
  print(deletando)