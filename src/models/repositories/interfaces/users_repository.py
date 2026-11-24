from abc import ABC, abstractmethod
class InsertUserInterface(ABC):
  @abstractmethod
  async def insert_user(self, infos_user: dict): pass
  @abstractmethod
  async def get_user(self, user_name: str): pass