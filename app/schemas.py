from pydantic import BaseModel, EmailStr

class ContatoCreate(BaseModel):
    nome: str
    email: EmailStr
    mensagem: str

class ContatoResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr
    mensagem: str

    class Config:
        from_attributes=True