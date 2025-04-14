import sqlite3

def conectar():
    conexao = sqlite3.connect("cadastro_clientes.db")
    return conexao


def criar_tabela_clientes():
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                nome TEXT NOT NULL, 
                idade INTEGER NOT NULL,
                telefone TEXT,
                email TEXT,
                sexo TEXT CHECK (sexo IN ('M', 'F'))
        );
        """)
    conexao.commit()
    cursor.close()
    conexao.close()
    
def cadastrar_cliente_tabela(nome,idade,telefone,email,sexo):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute ("""
                           INSERT INTO clientes (nome, idade, telefone,email,sexo)
                           VALUES (?,?,?,?,?)
                           
                        """,(nome,idade,telefone,email,sexo))
        conexao.commit()
        cursor.close()
        conexao.close()
        
def listar_clientes():
    conexao = conectar()
    conexao.row_factory = sqlite3.Row  
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    
    cursor.close()
    conexao.close()
    return clientes
    
#deletar pessoa (busca por ID)
def deletar_cliente(id):
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id,))
    
    conexao.commit()
    cursor.close()
    conexao.close()
                 
def buscar_por_id(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def buscar_por_nome(nome):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes WHERE nome LIKE ?", ('%' + nome + '%',))
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def buscar_por_idade(idade):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes WHERE idade = ?", (idade,))
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def buscar_por_telefone(telefone):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes WHERE telefone LIKE ?", ('%' + telefone + '%',))
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def buscar_por_email(email):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes WHERE email LIKE ?", ('%' + email + '%',))
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def buscar_por_sexo(sexo):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes WHERE sexo = ?", (sexo.upper(),))
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def listar_ordem_alfabetica():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes ORDER BY nome ASC")
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def listar_ordem_alfabetica_decrescente():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes ORDER BY nome DESC")
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def listar_por_id():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes ORDER BY id ASC")
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def listar_por_id_decrescente():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes ORDER BY id DESC")
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado 


#buscar por ID
#buscar por nome
#buscar por idade
#buscar por telefone
#buscar por email
#buscar por sexo

#mostrar todos, por ordem alfabética
#ordem alfabética, so que decrescente

#ordem numérica (id) 
#ordem numérica (id) decrescente



### CONEXÃO COM O BANCO ###
def conectar():
    return sqlite3.connect("banco_produtos.db")


### CRIAÇÃO DA TABELA ###
def criar_tabela_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL,
            categoria TEXT
        );
    """)
    conexao.commit()
    cursor.close()
    conexao.close()


### CREATE ###
def cadastrar_produto(nome, preco, quantidade, categoria):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO produtos (nome, preco, quantidade, categoria)
        VALUES (?, ?, ?, ?);
    """, (nome, preco, quantidade, categoria))
    conexao.commit()
    cursor.close()
    conexao.close()


### READ ###
def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos;")
    produtos = cursor.fetchall()
    cursor.close()
    conexao.close()
    return produtos


### SEARCH ###
def buscar_produto_por_nome(nome):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos WHERE nome LIKE ?;", ('%' + nome + '%',))
    produtos = cursor.fetchall()
    cursor.close()
    conexao.close()
    return produtos


### UPDATE ###
def atualizar_produto(id, nome=None, preco=None, quantidade=None, categoria=None):
    conexao = conectar()
    cursor = conexao.cursor()

    campos = []
    valores = []

    if nome:
        campos.append("nome = ?")
        valores.append(nome)
    if preco is not None:
        campos.append("preco = ?")
        valores.append(preco)
    if quantidade is not None:
        campos.append("quantidade = ?")
        valores.append(quantidade)
    if categoria:
        campos.append("categoria = ?")
        valores.append(categoria)

    valores.append(id)

    sql = f"UPDATE produtos SET {', '.join(campos)} WHERE id = ?"
    cursor.execute(sql, valores)

    conexao.commit()
    cursor.close()
    conexao.close()