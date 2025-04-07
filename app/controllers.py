from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, date
from app import models

def configurar_rotas(app):
    @app.route("/")
    def pagina_inicial():
        return render_template('index_navegação.html')
    
    @app.route("/cadastrar")
    def cadastrar_cliente():
        return render_template('cadastrar_cliente.html')
    
    @app.route("/gerenciar")
    def gerenciar_clientes():
        return render_template('gerenciar_cliente.html')
    
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
            return redirect(url_for('gerenciar_clientes'))
        except Exception as e:
            return f"Erro ao cadastrar cliente: {str(e)}", 500


def calcular_idade(data_nasc):
    if isinstance(data_nasc, str):
        data_nasc = datetime.strptime(data_nasc, "%Y-%m-%d").date()
    
    hoje = date.today()
    idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
    return idade