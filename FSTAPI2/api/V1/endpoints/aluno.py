from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.aluno_models import ALunoModel
from schemas.aluno_schemas import AlunoSchema
from core.deps import get_session


router = APIRouter()
#Listando todos os Alunos
@router.get('/', response_model=List[AlunoSchema])
async def get_alunos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ALunoModel)
        result = await session.execute(query)
        alunos : List[ALunoModel] = result.scalars().all

        return alunos
#Listando Aluno por ID
@router.get('/{alunoID}',response_model=AlunoSchema, status_code=status.HTTP_200_OK)
async def get_aluno(alunoID: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ALunoModel).filter(ALunoModel.id == alunoID)
        result = await session.execute(query)
        aluno = result.scalar_one_or_none
        if aluno:
            return aluno
        else:
            raise HTTPException(detail=f'Aluno com o ID {alunoID} Não Encontrado', status_code=status.HTTP_404_NOT_FOUND)

#Criando Aluno

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=AlunoSchema)
async def post_aluno(aluno : AlunoSchema, db: AsyncSession = Depends(get_session)):
    novo_aluno = ALunoModel(nome= aluno.name, email= aluno.email)
    db.add(novo_aluno)
    await db.commit()
    return novo_aluno

@router.put('/{alunoID}', response_model=AlunoSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_aluno(alunoID: int, aluno : AlunoSchema, db: AsyncSession = Depends(get_session)):
    async with db as sesssion:
        query = select(ALunoModel).filter(ALunoModel.id == alunoID)
        result = await sesssion.execute(query)
        aluno_up = result.scalar_one_or_none()

        if aluno_up:
            aluno_up.name = aluno.name
            aluno_up.email = aluno.email
            await sesssion.commit()
            return aluno_up
        else:
            raise HTTPException(detail=f'Aluno com o ID {alunoID} Não Encontrado', status_code=status.HTTP_404_NOT_FOUND)

@router.delete('/{alunoID}', response_model=AlunoSchema, status_code=status.HTTP_202_ACCEPTED)
async def delete_aluno(alunoID: int, aluno : AlunoSchema, db: AsyncSession = Depends(get_session)):
    async with db as sesssion:
        query = select(ALunoModel).filter(ALunoModel.id == alunoID)
        result = await sesssion.execute(query)
        aluno_del = result.scalar_one_or_none()

        if aluno_del:
            await sesssion.delete(aluno_del)
            await sesssion.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail=f'Aluno com o ID {alunoID} Não Encontrado', status_code=status.HTTP_404_NOT_FOUND)