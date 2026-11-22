import pytest
from database_connection_handler import DBConnection

@pytest.mark.asyncio
@pytest.mark.skip
async def test_connection():
  async with DBConnection() as db:
    assert db.session is not None
    print(f'passou dog!\n{db.session}')