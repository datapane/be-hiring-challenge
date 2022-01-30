from pydantic import BaseModel


class Dataset(BaseModel):
    id: int
    size: int
    dataframe: str

