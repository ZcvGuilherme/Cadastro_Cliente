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
    
def cadastrar_cliente(nome,idade,telefone,email,sexo):
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


if __name__ == "__main__":
    criar_tabela_clientes()
    print(listar_clientes())