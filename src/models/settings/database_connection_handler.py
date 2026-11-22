from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
DATABASE_URL = "sqlite+aiosqlite:///schema.db"

engine = create_async_engine(
  DATABASE_URL,
  echo=False,
  pool_size=2,
  max_overflow=0,
  pool_timeout=30
)

SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

class DBConnection:
  def __init__(self) -> None:
    self.session: Optional[AsyncSession] = None

  async def __aenter__(self):
    self.session = SessionLocal()
    return self
  async def __aexit__(self, exc_type, exc, tb):
    await self.session.close()