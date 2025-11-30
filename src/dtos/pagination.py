from typing import Generic, TypeVar
from pydantic import BaseModel

T = TypeVar("T")

class Pagination(BaseModel, Generic[T]):
    content: list[T] = []
    offset: int = 0
    limit: int = 0
    total_elements: int = 0
    total_pages: int = 0 
    next: int | None = None
    previous: int | None = None
    
    def __populate__(self, offset: int, limit: int, total_elements: int):
        self.offset = offset
        self.limit = limit
        self.total_elements = total_elements
        self.total_pages = (total_elements + limit - 1) // limit
        self.next = offset + 1 if offset < self.total_pages else None
        self.previous = offset - 1 if offset > 1 else None
    
    