from flask import render_template, request
from app import models

def pagina_inicial():
    return render_template('index_navegação.html')

def cadastrar_cliente():
    return render_template('cadastrar_cliente.html')

def cadastrar_produto():
    return render_template('cadastrar_produto.html')

def gerenciar_clientes():
    try:
        campo = request.args.get("campo", "id")
        ordem = request.args.get("ordem", "asc") == "asc"
        busca = request.args.get("pesquisa", "")


        clientes = models.buscar_clientes_ordenado(campo=campo,busca=busca, ordem=ordem)
        return render_template('gerenciar_cliente.html', clientes=clientes, campo=campo, ordem=ordem, busca=busca)
    except Exception as e:
        return f"Erro ao buscar clientes: {str(e)}", 500

def gerenciar_produtos():
    try:
        campo = request.args.get("campo", "id")
        ordem = request.args.get("ordem", "asc") == "asc"
        busca = request.args.get("pesquisa", "")


        produtos = models.buscar_produtos_ordenado(campo, busca, ordem)
        return render_template("gerenciar_produto.html", produtos=produtos, campo=campo, ordem=ordem, busca =busca)
    except Exception as e:
        return f"Erro ao buscar produtos: {str(e)}", 500
