from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime, date
from app import models, views
#---------------------------------------ROTAS PAGINAS----------------------------------#
def configurar_rotas(app):
    @app.route("/")
    def pagina_inicial():
        return views.pagina_inicial()
    
    @app.route("/cadastrar-cliente")
    def cadastrar_cliente():
        return views.cadastrar_cliente()
    
    @app.route("/cadastrar-produto")
    def cadastrar_produto():
        return views.cadastrar_produto()
    
    @app.route("/gerenciar-clientes")
    def gerenciar_clientes():
        return views.gerenciar_clientes()

    @app.route("/gerenciar-produtos")
    def gerenciar_produtos():
        return views.gerenciar_produtos()
#---------------------------------------ROTAS PAGINAS----------------------------------#





#---------------------------------------ROTAS CLIENTES----------------------------------#
    @app.route("/novo_cliente", methods=['POST'])
    def novo_cliente():
        nome = request.form.get('nome')
        data_nasc = request.form.get('data_nasc')
        telefone = request.form.get('telefone')
        email = request.form.get('email')
        sexo = request.form.get('sexo')

        try:
            if sexo == "Masculino":
                sexo = 'M'
            elif sexo == "Feminino":
                sexo = 'F'               
                
            idade = calcular_idade(data_nasc)
            models.cadastrar_cliente_tabela(nome, idade, telefone, email, sexo)
            flash(f"Cliente '{nome}' cadastrado com sucesso!", "sucesso")
            return redirect(url_for('cadastrar_cliente'))
        except Exception as e:
            flash(f"Erro ao cadastrar cliente: {str(e)}", "erro")
            return redirect(url_for('cadastrar_cliente'))

    def calcular_idade(data_nasc):
        if isinstance(data_nasc, str):
            data_nasc = datetime.strptime(data_nasc, "%Y-%m-%d").date()
        
        hoje = date.today()
        idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
        return idade
    

    @app.route("/editar-cliente/<int:id>", methods=["POST"])
    def editar_cliente(id):
        try:
            if request.is_json:
                data = request.get_json()
                nome = data.get('nome')
                idade = data.get('idade')
                telefone = data.get('telefone')
                email = data.get('email')
                sexo = data.get('sexo')

                models.editar_cliente(id, nome=nome, idade=idade, telefone=telefone, email=email, sexo=sexo)
                return '', 204 
            else:

                return redirect(url_for("gerenciar_clientes"))
        except Exception as e:
           
            return redirect(url_for("gerenciar_clientes"))
    

    @app.route("/deletar/<int:id>", methods=["POST"])
    def deletar_cliente(id):
        try:
            models.deletar_cliente(id)
            return redirect(url_for('gerenciar_clientes'))
        except Exception as e:
         return f"Erro ao deletar cliente: {str(e)}", 500

#---------------------------------------ROTAS CLIENTES----------------------------------#






#---------------------------------------ROTAS PRODUTOS----------------------------------#
    @app.route("/deletar-produto/<int:id>", methods=["POST"])
    def deletar_produto(id):
        try:
            models.deletar_produto(id)
            return redirect(url_for('gerenciar_produtos'))
        except Exception as e:
            flash(f"Erro ao excluir produto: {str(e)}", "erro")
            return redirect(url_for('gerenciar_produtos'))


    @app.route("/editar-produto/<int:id>", methods=["POST"]) 
    def editar_produto(id):
        try:
            models.editar_produto(id)
            return redirect(url_for('gerenciar_produtos'))
        except Exception as e:
            return redirect(url_for('gerenciar_produtos'))
      

    @app.route("/novo_produto", methods=['POST'])
    def novo_produto():
        nome = request.form.get("nome")
        quantidade = request.form.get("quantidade")
        valor = request.form.get("valor")
        try:

            quantidade = int(quantidade)
            valor = float(valor)

            models.cadastrar_produto(nome, valor, quantidade)
            flash(f"Produto '{nome}' cadastrado com sucesso!", "sucesso")
            return redirect(url_for('cadastrar_produto'))
        except Exception as e:
            flash(f"Erro ao cadastrar produto: {str(e)}", "erro")
            return redirect(url_for('cadastrar_produto'))


#---------------------------------------ROTAS PRODUTOS----------------------------------#