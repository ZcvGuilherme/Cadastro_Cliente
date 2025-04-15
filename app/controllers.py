from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime, date
from app import models

def configurar_rotas(app):
    @app.route("/")
    def pagina_inicial():
        return render_template('index_navegação.html')
    
    @app.route("/cadastrar-cliente")
    def cadastrar_cliente():
        return render_template('cadastrar_cliente.html')
    
    @app.route("/cadastrar-produto")
    def cadastrar_produto():
        return render_template('cadastrar_produto.html')
    
    @app.route("/deletar/<int:id>", methods=["POST"])
    def deletar_cliente(id):
        try:
            models.deletar_cliente(id)
            return redirect(url_for('gerenciar_clientes'))
        except Exception as e:
         return f"Erro ao deletar cliente: {str(e)}", 500
    
    
    @app.route("/gerenciar-clientes")
    def gerenciar_clientes():
        try:
            clientes = models.listar_clientes()
            return render_template('gerenciar_cliente.html', clientes=clientes)
        except Exception as e:
            return f"Erro ao buscar clientes: {str(e)}", 500

    @app.route("/gerenciar-produtos")
    def gerenciar_produtos():
        return render_template('gerenciar_produto.html')
    
    
    @app.route("/novo_cliente", methods=['POST'])
    def novo_cliente():
        nome = request.form.get('nome')
        data_nasc = request.form.get('data_nasc')
        telefone = request.form.get('telefone')
        email = request.form.get('email')
        sexo = request.form.get('sexo')
        
        if not nome or not data_nasc or not sexo:
            return "Nome, data de nascimento e sexo obrigatórios", 400
        
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
            flash(f"Erro ao cadastrar produto: {str(e)}", "erro")
            return redirect(url_for('cadastrar_cliente'))



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





def calcular_idade(data_nasc):
    if isinstance(data_nasc, str):
        data_nasc = datetime.strptime(data_nasc, "%Y-%m-%d").date()
    
    hoje = date.today()
    idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
    return idade