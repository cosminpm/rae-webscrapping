from fastapi import FastAPI
import uvicorn


from dotenv import load_dotenv

from app.services.rae.router import rae_router


app = FastAPI()

load_dotenv()
app.include_router(rae_router)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
