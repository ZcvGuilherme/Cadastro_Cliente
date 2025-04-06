from flask import Flask, render_template, request, redirect, url_for
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
        #aqui vai o cadastar cliente
        print("ok")