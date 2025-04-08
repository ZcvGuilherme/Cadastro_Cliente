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
        cliente = cursor.fetchone()
        
### Confirmação de exclusão ###        
        
        if cliente:
            print("\n Cliente encontrado:")
            print(f"ID:{cliente[0]}")
            print(f"Nome:{cliente[1]}")
            print(f"Idade:{cliente[2]}")
            print(f"telefone:{cliente[3]}")
            print(f"Email:{cliente[4]}")
            print(f"Sexo:{cliente[5]}")
                       
            
        confirmar = input("Tem certeza que deseja deletar esse cliente? (s/n):").lower()
        
        if confirmar == "s":
            cursor.execute("DELETE FROM clientes WHERE id = ?",(id,))
            conexao.commit()
            print("Cliente deletado com sucesso!")
        else: 
            print("Cliente não deletado.")
            
        print("Cliente não encontrado com o ID {id}.")
        
        cursor.close()
        conexao.close()
                 

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

