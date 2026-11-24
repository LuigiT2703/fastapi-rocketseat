from sqlalchemy import insert, select, delete, update
from src.models.entities.users import Users
from src.models.settings.database_connection_handler import DBConnection
from interfaces.users_repository import InsertUserInterface
class InsertUser(InsertUserInterface):
  async def insert_user(self, infos_user: dict):
    async with DBConnection() as db:
      query = insert(Users).values(**infos_user)
      await db.session.execute(query)
      await db.session.commit()

  async def get_user(self, user_name: str):
    async with DBConnection() as db:
      query = (
        select(Users)
        .where(Users.c.user_name == user_name) 
      )

      resultado = await db.session.execute(query)
      rows = resultado.fetchall()
      users_list = [dict(row._mapping) for row in rows]
      return users_list

  async def update_user(self, user_id: int, att_user:dict):
    async with DBConnection() as db:
      query = (
        update(Users)
        .where(Users.c.id == user_id)
        .values(**att_user)
      )
      await db.session.execute(query)
      await db.session.commit() 

  async def delete_user(self, user_id: int):
    async with DBConnection() as db:
      query = (
        delete(Users)
        .where(Users.c.id == user_id)
      )

      await db.session.execute(query)
      await db.session.commit()

    
      

      