from pydantic import BaseModel
from typing import List, Optional

class Comment(BaseModel):
    text: str

class Note(BaseModel):
    title: str
    desc: str
    comments: List[Comment] = []
