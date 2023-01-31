from typing import Optional
from sqlmodel import SQLModel, Field

class Aluno(SQLModel, table= True):
    id : Optional[int] = Field(default=None, primary_key=True)
    nome : str
    idade : int
    email : str