from core.configs import settings
from pydantic import BaseModel

class AlunoModel(settings.DB_BaseModel):
    __tablename__ = 'alunos'
    
    id : int
    name : str
    email : str
