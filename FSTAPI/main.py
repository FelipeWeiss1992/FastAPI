from fastapi import FastAPI, HTTPException, status
from models import Aluno
app = FastAPI()


alunos = {

    1 : {'nome' : "Felipe",'idade' : 30, 'email' : 'felipeweiss92@gmail.com'},
    2 : {'nome' : "Jean",'idade' : 40, 'email' : 'jean@gmail.com'},
    3 : {'nome' : "Dieter",'idade' : 40, 'email' :'dieter@gmail.com'},
    4 : {'nome' : "David", 'idade' : 35, 'email' : 'david@gmail.com'}

}

@app.get('/alunos')
async def get_AlunosID():
    return alunos

@app.get('/alunos/{aluno_id}')
async def get_AlunoID(aluno_id: int):
    try:
        aluno = alunos[aluno_id]
        alunos.update({'id': aluno_id})
        return aluno
    except KeyError:
        raise HTTPException(

        status_code = status.HTTP_404_NOT_FOUND, detail='Aluno não encontrado'

        )
        
@app.get('/alunosnome/{aluno_nome}')
async def get_Nomealuno(aluno_nome: str):
    for aluno in alunos.values():
        if aluno['nome'] == aluno_nome:
            return aluno
        
@app.post('/alunonovo', status_code=status.HTTP_201_CREATED)
async def post_NovoAluno(aluno_novo: Aluno):
    next_id : int = len(alunos) + 1
    alunos[next_id] = aluno_novo
    return aluno_novo
    


if __name__ == '__main__':
    import uvicorn

    uvicorn.run (
        "main:app",
        host= "127.0.0.1",
        port= 8000,
        log_level= 'info',
        reload = True
    )

