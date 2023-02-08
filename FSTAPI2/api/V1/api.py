from fastapi import APIRouter

from api.V1.endpoints import aluno

api_router = APIRouter()

api_router.include_router(aluno.router, prefix='/alunos', tags=["alunos"])
