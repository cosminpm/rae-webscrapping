import uvicorn
from fastapi import FastAPI

app = FastAPI()


def root():
    return "Hola, mundo"


if __name__ == '__main__':
    uvicorn.run(app)
