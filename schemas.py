from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List, Dict

class SorteioRequest(BaseModel):
    nomes: List[str] = Field(..., min_length=2)

    @field_validator('nomes')
    @classmethod
    def checar_duplicatas(cls, v):
        if len(v) != len(set(v)):
            raise ValueError("Nomes duplicados.")
        return v

class SorteioResponse(BaseModel):
    total_participantes: int
    pares: Dict[str, str]

class UsuarioBase(BaseModel):
    username: str = Field(..., min_length=3, description="Nome de usuário único")
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    senha: str = Field(..., min_length=4, description="Senha secreta")

class UsuarioLogin(BaseModel):
    username: str
    senha: str

class UsuarioPublic(UsuarioBase):
    # Não retornamos a senha nunca!
    id: int