from app.api.models import ClothIn, ClothOut, ClothUpdate
from app.api.db import cloths, database


async def add_cloth(payload: ClothIn):
    query = cloths.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_cloths():
    query = cloths.select()
    return await database.fetch_all(query=query)


async def get_cloth(id):
    query = cloths.select(cloths.c.id == id)
    return await database.fetch_one(query=query)


async def delete_cloth(id: int):
    query = cloths.delete().where(cloths.c.id == id)
    return await database.execute(query=query)


async def update_cloth(id: int, payload: ClothIn):
    query = (
        cloths
        .update()
        .where(cloths.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)
