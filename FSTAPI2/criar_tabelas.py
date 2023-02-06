from core.configs import settings
from core.database import engine

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print('Tabela Criada Com Sucesso')

if __name__ == '__main__':
    import asyncio
    asyncio.run(create_tables())
