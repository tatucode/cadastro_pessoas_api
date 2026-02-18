## Cadastro de Pessoas API

API REST simples para gerenciamento de pessoas usando FastAPI e SQLite.
Projeto desenvolvido com estrutura em camadas, seguindo boas práticas de back-end.

## Tecnologias
- Python 
- FastAPI
- SQLite3
- Uvicorn
- Pydantic
- Logging

## Como rodar o projeto
1 - Clonar repositório

git clone
https://github.com/tatucode/cadastro_pessoas_api.git
cd cadastro_pessoas_api

2 - Criar ambiente virtual

Linux/Mac:
python -m venv.venv
source.venv/bin/activate

Windows:
.venv\Scripts\activate

3 - Instalar dependências

pip install -r requirements.txt

4 - Rodar a API

uvicorn app.main:app --reload --port 8001

Abrir no navegador:
https://127.0.0.1:8001/docs

## Endpoints

GET /health
Verifica se a API está rodando

POST /pessoas
Cria uma nova pessoa

GET /pessoas
Lista todas as pessoas

PUT /pessoas{id}
Atualiza uma pessoa

DELETE /pessoas{id}
Remove uma pessoa

## Estrutura do projeto

app/
--main.py
--core/logger.py
--db/database.py
--routers/pessoas.py
--routers/health.py
--schemas/pessoas.py
--services/pessoa_service.py

## Arquitetura

Routers: recebem requisições HTTP
Services: regras de negócio
DB: acesso ao banco SQLite
Schemas: validação de dados
Core: logger e configurações

## Logs

A aplicação registra:
- Requisições HTTP
- Status code
- Criação, listagem, update e delete
- Erros

## Melhorias futuras
- Autenticação JWT
- Testes automatizados
- PostgreSQL
- Docker
- Deploy em nuvem
- Paginação
- Filtros

## Autor

Pedro Victor
Backend Developer | Cibersecurity | Python | APIs

## Status

CRUD completo
Banco persistente
Logging ativo
Estrutura organizada
Projeto funcional