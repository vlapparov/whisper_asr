from pydantic import BaseModel


class OutputSchema(BaseModel):
    text: str
