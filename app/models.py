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
        
        cursor.execute("DELETE FROM clientes WHERE id = ?",(id,))
        conexao.commit()
        cursor.close()  
        
        
#buscar por ID
def buscar_por_id(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

#buscar por nome
def buscar_por_nome(nome):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes WHERE nome LIKE ?", ('%' + nome + '%',))
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado


#buscar por idade
def buscar_por_idade(idade):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes WHERE idade = ?", (idade,))
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

#buscar por telefone
def buscar_por_telefone(telefone):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes WHERE telefone LIKE ?", ('%' + telefone + '%',))
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

#buscar por email
def buscar_por_email(email):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes WHERE email LIKE ?", ('%' + email + '%',))
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

#buscar por sexo
def buscar_por_sexo(sexo):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes WHERE sexo = ?", (sexo.upper(),))
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

#mostrar todos, por ordem alfabética
def listar_clientes_alfabetica():
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM clientes ORDER BY nome ASC")
    clientes = cursor.fetchall()
    cursor.close()
    conexao.close()
    return clientes
#ordem alfabética, so que decrescente
def listar_clientes_alfabetica_decrescente():
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM clientes ORDER BY nome DESC")
    clientes = cursor.fetchall()
    cursor.close()
    conexao.close()
    return clientes

#ordem numérica (id) 
def listar_clientes_id():
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM clientes ORDER BY id ASC")
    clientes = cursor.fetchall()
    cursor.close()
    conexao.close()
    return clientes

#ordem numérica (id) decrescente
def listar_clientes_id_decrescente():
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM clientes ORDER BY id DESC")
    clientes = cursor.fetchall()
    cursor.close()
    conexao.close()
    return clientes

###_____________________________________________________________________________________###



### BANCO DE DADOS PRODUTOS ###
import sqlite3

### CONEXÃO COM O BANCO ###
def conectar():
    return sqlite3.connect("banco_produtos.db")


### CRIAÇÃO DA TABELA PRODUTO  ###
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


### CADASTRAR PRODUTOS ###
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


### VISUALIZAR PRODUTO ###
def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos;")
    produtos = cursor.fetchall()
    cursor.close()
    conexao.close()
    return produtos


### BUSCAR PRODUTOS  ###
def buscar_produto_por_nome(nome):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos WHERE nome LIKE ?;", ('%' + nome + '%',))
    produtos = cursor.fetchall()
    cursor.close()
    conexao.close()
    return produtos


### ATUALIZAR TABELA PRODUTOS  ###
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