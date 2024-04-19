from pydantic import BaseModel
from typing import List, Optional


class ClothIn(BaseModel):
    name: str
    brand: str
    price: int
    genre: str
    shops_id: List[int]


class ClothOut(ClothIn):
    id: int


class ClothUpdate(ClothIn):
    name: Optional[str] = None
    brand: Optional[str] = None
    price: Optional[int] = None
    genre: Optional[str] = None
    shops_id: Optional[List[int]] = None