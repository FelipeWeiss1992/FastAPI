from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def home():
    return{
        "message": "Hello World"
    }

alunos = {

    1 : "Felipe",
    2 : "Jean",
    3 : "Dieter",
    4 : "David"

}

@app.get('/alunos')
async def get_alunos():
    return alunos

@app.get('/alunos/{item_id}')
def get_AlunosID(item_id: int):
    return alunos[item_id]


if __name__ == '__main__':
    import uvicorn

    uvicorn.run (
        "main:app",
        host= "127.0.0.1",
        port= 8000,
        log_level= 'info',
        reload = True
    )