from pydantic import BaseModel


class Word(BaseModel):
    name: str
    definitions: list[str]
    url: str
