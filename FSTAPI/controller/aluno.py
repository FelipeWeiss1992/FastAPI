from models.aluno import Aluno
from database import engine
from sqlmodel import Session,select
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

def getAlunos():
    with Session(engine) as session:
        statement = select(Aluno)
        results = session.exec(statement).all()
        return JSONResponse(content=jsonable_encoder(results))

def getAlunoID(alunoID):
    with Session(engine) as session:
        statement = select(Aluno).where(Aluno.id == alunoID)
        results = session.exec(statement).first()
        if results == None:
            return f'Aluno com ID ({alunoID}) Não encontrado.'
        return JSONResponse(content=jsonable_encoder(results))

def getAlunoNome(nomeAluno):
    with Session(engine) as session:
        statement = select(Aluno).where(Aluno.nome == nomeAluno)
        results = session.exec(statement).first()
        print(results)
        if results == None:
            return f'{nomeAluno} Não encontrado.'
        return JSONResponse(content=jsonable_encoder(results))

def criarAluno(aluno:Aluno):
    with Session(engine) as session:
        session.add(aluno)
        session.commit()
        session.refresh(aluno)
        return 'Aluno Criado Com Sucesso'

def editaAluno(alunoID, dadosAluno: Aluno):
    with Session(engine) as session:
        statement = select(Aluno).where(Aluno.id == alunoID)
        results = session.exec(statement).first()
        results.nome = dadosAluno.nome
        results.idade = dadosAluno.idade
        results.email = dadosAluno.email

        session.add(results)
        session.commit()
        session.refresh(results)


        return JSONResponse(content=jsonable_encoder(results))

def deletaAluno(alunoID):
    with Session(engine) as session:
        statement = select(Aluno).where(Aluno.id == alunoID)
        results = session.exec(statement).first()
        session.delete(results)
        session.commit()
        return 'Aluno Deletado'


