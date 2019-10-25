import sqlite3 as sql 
import os.path as path

def inicializa_tabelas():
    conn = sql.connect('database.db')
    cursor = conn.cursor()

    # criando a tabela (clientes)
    cursor.execute("""
    CREATE TABLE clientes (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf     VARCHAR(11) NOT NULL,
            adress TEXT NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE produtos (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL
    );
    """)
    conn.close()

def insere_cliente(cliente):
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    nome = cliente["nome"]
    cpf = cliente["cpf"]
    adress = cliente["adress"]
    # inserindo dados na tabela
    try:
        cursor.execute("""
        INSERT INTO clientes (nome, cpf, adress)
        VALUES (?,?,?)
        """, (nome, cpf, adress))
        conn.commit()
        return cliente
    except Exception as e:
        return e

def insere_produto(produto):
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    nome = produto["nome"]
    quantidade = produto["quantidade"]
    # inserindo dados na tabela
    try:
        cursor.execute("""
        INSERT INTO produtos (nome, quantidade)
        VALUES (?,?)
        """, (nome, quantidade))
        conn.commit()
        return produto
    except Exception as e:
        return e


    

def criar_BD():
    conn = sql.connect('database.db')
    inicializa_tabelas()
    conn.close()

def existe_BD():
    if path.exists('database.db'):
        return True 
    return False

def inicializa_BD():
    if not existe_BD():
        criar_BD()
    conn = sql.connect('database.db')
    return conn
    

if __name__ == "__main__":
    print(insere_produto({"nome": "geovane", "quantidade": "2"}))