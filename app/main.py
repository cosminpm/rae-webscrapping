from fastapi import FastAPI
import uvicorn

from app.services.rae.router import rae_router

app = FastAPI()

app.include_router(rae_router)

@app.get("/")
def root():
    return "Hola mundo"


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
