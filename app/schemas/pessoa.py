from pydantic import BaseModel, Field

class CriarPessoa(BaseModel):
    nome: str = Field(min_length=1, max_length=100)
    idade: int = Field(ge=0, le=150)
    email: str = Field(min_length=1, max_length=255)

class PessoaOut(BaseModel):
    id: int
    nome: str
    idade: int
    email: str


class AtualizarPessoas(BaseModel):
    nome: str = Field(min_length=1, max_length=100)
    idade: int = Field(ge=0, le=150)
    email: str = Field(min_length=1, max_length=255)