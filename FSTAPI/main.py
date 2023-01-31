from fastapi import FastAPI, HTTPException, status
from models.aluno import Aluno
from database import engine
from controller.aluno import criarAluno, getAlunos, getAlunoID, getAlunoNome, editaAluno, deletaAluno


app = FastAPI()

@app.get('/alunos/')
async def get_Aluno():
    return getAlunos()

@app.get('/alunos/{alunoID}')
async def get_AlunoID(alunoID : int):
    return getAlunoID(alunoID)

@app.get('/alunosnome/{nomeAluno}')
async def get_AlunoNome(nomeAluno : str):
    return getAlunoNome(nomeAluno)

        
@app.post('/alunos', status_code=status.HTTP_201_CREATED)
async def post_Aluno(aluno_novo: Aluno):
    return criarAluno(aluno_novo)

@app.put('/alunos/{item_id}')
async def put_AlunoID(item_id : int, novosDados :Aluno):
    return editaAluno(item_id, novosDados)

@app.delete('/alunos/{item_id}')
async def delete_AlunoID(item_id : int):
    return deletaAluno(item_id)

@app.get('/calculadora')
def soma(num1: int, num2: int, num3: int):
    return num1+num2+num3


if __name__ == '__main__':
    import uvicorn

    uvicorn.run (
        "main:app",
        host= "127.0.0.1",
        port= 8000,
        log_level= 'info',
        reload = True
    )

