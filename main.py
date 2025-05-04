import uvicorn
from fastapi import FastAPI

app = FastAPI()


def root():
    return "Hola, mundo"

from starlette import status
status.HTTP_500_INTERNAL_SERVER_ERROR

if __name__ == '__main__':
    uvicorn.run(app)
