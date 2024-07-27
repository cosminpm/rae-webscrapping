from fastapi import APIRouter
from pydantic import BaseModel


rae_router: APIRouter = APIRouter(tags=["RAE"])


@rae_router.get("/bolsa")
def get_bolsa() -> list:
    """
    Devuelve lo que hay en la bolsa
    :return:
    :rtype:
    """
    return ...


@rae_router.post("/poner_en_bolsa")
def post_en_bolsa(obj: ...):
    ...
