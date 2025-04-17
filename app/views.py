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
        ordem = request.args.get("ordem", "asc")

        ordem_bool = True if ordem == "asc" else False
        clientes = models.buscar_clientes_ordenado(campo=campo, ordem=ordem_bool)

        return render_template('gerenciar_cliente.html', clientes=clientes, campo=campo, ordem=ordem)
    except Exception as e:
        return f"Erro ao buscar clientes: {str(e)}", 500

def gerenciar_produtos():
    try:
        campo = request.args.get("campo", "id")
        ordem = request.args.get("ordem", "asc") == "asc"
        produtos = models.buscar_produtos_ordenado(campo, ordem)
        return render_template("gerenciar_produto.html", produtos=produtos, campo=campo, ordem=ordem)
    except Exception as e:
        return f"Erro ao buscar produtos: {str(e)}", 500
