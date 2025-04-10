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
        
        cursor.execute("DELETE FROM clientes WHERE id = ?",(id,))
        cursor.close()
        conexao.close()


#buscar por nome
#buscar pelo email

#ordenar por :
# nome 
# idade
# sexo
