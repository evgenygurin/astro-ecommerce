
from pydantic import BaseModel
from typing import List, Optional

# --- Pydantic Schemas ---

class Product(BaseModel):
    id: str
    thumb_src: str
    thumb_alt: str
    title: str
    price: float
    description: Optional[str] = None
    color: Optional[str] = None
    colors: Optional[List[str]] = []
    rating: Optional[float] = None
    reviews: Optional[int] = None
    stock: Optional[bool] = True
    images: Optional[List[str]] = []
    full_description: Optional[str] = None
    highlights: Optional[List[str]] = []
    details: Optional[str] = None
    sizes: Optional[dict] = {}
    data: Optional[dict] = {}
    featuresDetails: Optional[dict] = {}

    class Config:
        orm_mode = True


class Category(BaseModel):
    id: str
    thumb_src: str
    title: str
    collection: str

    class Config:
        orm_mode = True
