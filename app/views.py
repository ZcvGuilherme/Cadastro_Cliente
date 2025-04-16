from flask import render_template
from app import models

def pagina_inicial():
    return render_template('index_navegação.html')

def cadastrar_cliente():
    return render_template('cadastrar_cliente.html')

def cadastrar_produto():
    return render_template('cadastrar_produto.html')

def gerenciar_clientes():
    try:
        clientes = models.listar_clientes()
        return render_template('gerenciar_cliente.html', clientes=clientes)
    except Exception as e:
        return f"Erro ao buscar clientes: {str(e)}", 500

def gerenciar_produtos():
    try:
        produtos = models.listar_produtos()
        return render_template('gerenciar_produto.html', produtos=produtos)
    except Exception as e:
        return f"Erro ao buscar produtos: {str(e)}", 500
