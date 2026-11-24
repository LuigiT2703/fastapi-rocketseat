from src.models.repositories.interfaces.users_repository import InsertUserInterface


class UserFinder:
  def __init__(self, users_repository: InsertUserInterface) -> None:
    self.__users_repository = users_repository

  async def finder_user_by_name(self, name: str) -> dict:
    busca_users = await self.__users_repository.get_user(name)

    return{
      "type": "USERS",
      "count": len(busca_users),
      "attributes": busca_users
    }