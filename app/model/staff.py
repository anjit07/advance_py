from pydantic import BaseModel

class Staff(BaseModel):
    name: str
    empCode: int
    address: str
    
