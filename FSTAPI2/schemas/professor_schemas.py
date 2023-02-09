from typing import Optional
from pydantic import BaseModel as SCBaseModel

class ProfessorSchema(SCBaseModel):
    id : Optional[int]
    name : str
    idade : int

    class config():
        orm_mode = True