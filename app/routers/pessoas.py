from fastapi import APIRouter, HTTPException, status
from typing import List
import sqlite3
from app.schemas.pessoa import CriarPessoa, PessoaOut, AtualizarPessoas
from app.services.pessoa_service import pessoa_create, pessoa_list, pessoa_delete, atualizar_pessoa
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("pessoas")

router = APIRouter()

@router.post("/pessoas", response_model=PessoaOut, status_code=201)
def registrar_pessoas(pessoa: CriarPessoa):
    logger.info(f"POST/ pessoas - nome: {pessoa.nome}, idade: {pessoa.idade}, email: {pessoa.email}")
    try:
        return pessoa_create(pessoa)
    except sqlite3.IntegrityError:
        logger.warning(f"POST /pessoas - email duplicado:{pessoa.email}")
        raise HTTPException(status_code=409, detail="Erro! e-mail já cadastrado")


@router.get("/pessoas", response_model=List[PessoaOut])
def listar_pessoas():
    logger.info("GET /pessoas")
    return pessoa_list()

@router.delete("/pessoas/{pessoa_id}", status_code=status.HTTP_200_OK)
def deletar_pessoa(pessoa_id: int):
    logger.info(f"DELETE /pessoas/{pessoa_id}")
    deletados = pessoa_delete(pessoa_id)
    if deletados == 0:
        logger.warning(f"DELETE /pessoas/{pessoa_id} - Não encontrado")
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    return {"message": "Pessoa deletada com sucesso"}

@router.put("/pessoas/{pessoa_id}", response_model=PessoaOut)
def atualizar_pessoa(pessoa_id: int, pessoa: AtualizarPessoas):
    logger.info(f"PUT /pessoas/{pessoa_id} - nome:{pessoa.nome} - email:{pessoa.email}")
    atualizados = atualizar_pessoa(pessoa_id, pessoa)
    if atualizados == 0:
        logger.warning(f"PUT /pessoas/{pessoa_id} - não encontrada")
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    
    return {"id": pessoa_id, "nome": pessoa.nome, "idade": pessoa.idade, "email": pessoa.email}
