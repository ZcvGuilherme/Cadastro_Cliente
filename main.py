from flask import Flask
from app import models, controllers


app = Flask(__name__,
            template_folder='app/templates',
            static_folder='app/static') 
    
models.criar_tabela_clientes()
controllers.configurar_rotas(app)

if __name__ == "__main__":
    app.run(debug=True)

# Caminho para as pastas templates e static


# # Função para conectar ao banco
# def conectar_banco():
#     caminho_banco = os.path.join(os.path.dirname(__file__), 'cadastro_clientes.db')
#     return sqlite3.connect(caminho_banco)

# # Página inicial
# @app.route('/')
# def index():
#     return render_template('index_navegação.html')

# # Página de cadastro
# @app.route('/cadastrar')
# def cadastrar_cliente():
#     return render_template('cadastrar_cliente.html')

# # Rota que recebe o formulário
# @app.route('/novo_cliente', methods=['POST'])
# def novo_cliente():
#     nome = request.form.get('nome')
#     idade = request.form.get('idade')
#     telefone = request.form.get('tell')
#     email = request.form.get('e-mail')
#     sexo = request.form.get('sexo')

#     conn = conectar_banco()
#     cursor = conn.cursor()
#     cursor.execute('''
#         INSERT INTO clientes (nome, idade, telefone, email, sexo)
#         VALUES (?, ?, ?, ?, ?)
#     ''', (nome, idade, telefone, email, sexo))
#     conn.commit()
#     conn.close()

#     return redirect('/')

# # Página para visualizar os clientes
# @app.route('/gerenciar')
# def gerenciar_clientes():
#     conn = conectar_banco()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM clientes")
#     clientes = cursor.fetchall()
#     conn.close()
#     return render_template('gerenciar_cliente.html', clientes=clientes)

# if __name__ == '__main__':
#     app.run(debug=True)
