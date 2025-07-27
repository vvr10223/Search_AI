from pydantic import BaseModel,Field
from typing import Annotated, List, Tuple
class webstate(BaseModel):
    input:str
    plan:List[str]=Field(default=[])
    past_steps:List[Tuple]=Field(default=[])
    response: str=Field(default="")