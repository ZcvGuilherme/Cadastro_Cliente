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
#buscar por sexo

#mostrar todos, por ordem alfabética
#ordem alfabética, so que decrescente

#ordem numérica (id) 
#ordem numérica (id) decrescente

