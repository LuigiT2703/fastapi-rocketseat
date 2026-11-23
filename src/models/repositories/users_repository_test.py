import pytest
from src.models.repositories.users_repository import InsertUser

@pytest.mark.asyncio
@pytest.mark.asyncio.skip
async def test_user_insert():
  nome = {
    "user_name": "pereira",
    "age": 260,
    "uf": "SP"
  }

  query = InsertUser()
  await query.insert_user(nome)

@pytest.mark.asyncio
async def test_get_user():
  query = InsertUser()
  result = await query.get_user("Luigi")
  print(result)