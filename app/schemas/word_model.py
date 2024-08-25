import json
from typing import Any, Literal

from pydantic import BaseModel
from pydantic.main import IncEx


class WordModel(BaseModel):
    name: str
    definitions: list[str]
    url: str

    def model_dump(
        self,
        *,
        mode: Literal['json', 'python'] | str = 'python',
        include: IncEx = None,
        exclude: IncEx = None,
        context: Any | None = None,
        by_alias: bool = False,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        round_trip: bool = False,
        warnings: bool | Literal['none', 'warn', 'error'] = True,
        serialize_as_any: bool = False,
    ) -> dict[str, Any]:
        data = super().model_dump()
        data["definitions"] = json.dumps(self.definitions)
        return data
