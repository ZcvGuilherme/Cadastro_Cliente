from flask import Flask
from app import models, controllers


app = Flask(__name__,
            template_folder='app/templates',
            static_folder='app/static') 
app.secret_key = 'chave_do_123'


models.criar_tabela_clientes()
models.criar_tabela_produtos()
controllers.configurar_rotas(app)


if __name__ == "__main__":
    app.run(debug=True)