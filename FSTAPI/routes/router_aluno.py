from fastapi import FastAPI, HTTPException, status
from models.aluno import Aluno
from database import engine
from controller.aluno import  getAlunos, getAlunoID, getAlunoNome, criarAluno, editaAluno, deletaAluno
from fastapi import Query, Path, Header

app = FastAPI(

    title = 'MoreDevs',
    version ='007',
    description ='Desenvolvido Python'
)

@app.get('/alunos', description='Todos os Alunos', summary='Retorna Alunos', response_description='Lista de Alunos Cadastrados')
async def get_Aluno():
    return getAlunos()

@app.get('/alunos/{alunoID}',description='Busca Aluno ID', summary='Retorna Aluno Especifico Pelo ID')
async def get_AlunoID(alunoID : int):
    return getAlunoID(alunoID)

@app.get('/alunosnome/{nomeAluno}',description='Busca Aluno Nome', summary='Retorna Aluno Especifico Pelo Nome')
async def get_AlunoNome(nomeAluno : str):
        return getAlunoNome(nomeAluno)

@app.post('/alunos', status_code=status.HTTP_201_CREATED, description='Cria Aluno', summary='Retorna Aluno Novo')
async def post_Aluno(aluno_novo: Aluno):
    return criarAluno(aluno_novo)

@app.put('/alunos/{alunoID}',description='Editar Aluno', summary='Retorna Aluno Editado')
async def put_AlunoID(alunoID : int, novosDados :Aluno):
    return editaAluno(alunoID, novosDados)

@app.delete('/alunos/{alunoID}',description='Deleta Aluno', summary='Retorna Aluno Deletado')
async def delete_AlunoID(alunoID : int):
    return deletaAluno(alunoID)

@app.get('/calculadora')
async def soma(num1: int = Query(default=None, gt=5), num2: int = Query(default=None, gt=10),xdevs: str = Header(default=None), num3: int = 0):
    soma = num1+num2+num3
    print(f'devs: {xdevs}')
    raise HTTPException(

        status_code=status.HTTP_200_OK, detail=f'NRs = {num1} + {num2} + {num3} = {soma}'
    )
    