import sqlite3

### CONEXÃO COM O BANCO DE DADOS ###

def conectar():
    conexao = sqlite3.connect("cadastro_clientes.db")
    return conexao


def criar_tabela_clientes():
    conexao = conectar()
    cursor = conexao.cursor()



    cursor.execute("""
               CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nome TEXT  NOT NULL, 
                    idade INTEGER NOT NULL,
                    telefone TEXT,
                    email TEXT,
                    sexo TEXT (1) CHECK (sexo IN ('M','F'))
        );
        """)

    conexao.commit()
    cursor.close()
    conexao.close()
    
    def cadastrar_cliente(nome,idade,telefone,email,sexo):
        conexao = conectar()
        cursor = conexao.cursor()
        
        cursor.execute("""
                       INSERT INTO clientes (nome, idade, telefone, email, sexo) 
                    VALUES (?, ?, ?, ?, ?)""",
                    (nome,idade,telefone,email,sexo))
        
        conexao.commit()
        cursor.close()
        conexao.close()
        
        