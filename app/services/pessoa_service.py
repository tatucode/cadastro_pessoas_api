from app.db.database import get_connection
from app.schemas.pessoa import CriarPessoa, AtualizarPessoas
import sqlite3

def pessoa_create(pessoa: CriarPessoa):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
                    INSERT INTO pessoas (nome, idade, email)
                    VALUES (?, ?, ?)
                    """, (pessoa.nome, pessoa.idade, pessoa.email))
        conn.commit()
        pessoa_id = cursor.lastrowid
        return {"id": pessoa_id, "nome": pessoa.nome, "idade": pessoa.idade, "email": pessoa.email}

    except sqlite3.IntegrityError as e:
        raise e
    finally:
        conn.close()


def pessoa_list():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome, idade, email FROM pessoas")
    rows = cursor.fetchall()
    conn.close()

    pessoas = []
    for row in rows:
        pessoas.append({
            "id": row["id"],
            "nome": row["nome"],
            "idade": row["idade"],
            "email": row["email"]
        })

    return pessoas

def pessoa_delete(pessoa_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM pessoas WHERE id = ?", (pessoa_id,))
    conn.commit()

    deletados = cursor.rowcount
    conn.close()

    return deletados

def atualizar_pessoa(pessoa_id: int, pessoa: AtualizarPessoas):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
                   UPDATE pessoas
                   SET nome = ?, idade = ?, email = ?
                   WHERE id = ?
                   """, (pessoa.nome, pessoa.idade, pessoa.email, pessoa_id))
    conn.commit()
    atualizados = cursor.rowcount
    conn.close()

    return atualizados