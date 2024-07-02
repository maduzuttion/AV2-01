from flask import Flask, render_template, request, redirect
from pony.orm import *

db=Database()
app=Flask(__name__)

class Prod(db.Entity):
    cod_barra=Required(str)
    nome_prod=Required(str)
    preco_prod=Required(float)
    qtd=Required(str)
    tipo_prod=Optional(str)

    def __str__(self):
        return f'{self.nome_prod},{self.preco_prod}'

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/listar_produto")
def listar_prod():
    with db_session:
        produtos=Prod.select() 
        return render_template("listar_prod.html", produtos=produtos)

@app.route("/form_produto")
def form_prod():
    return render_template("form_prod.html")

@app.route("/cadastrar_novo_produto")
def cadastrar_novo_produto():
    cod=request.args.get("cod")
    produto= request.args.get("produto")
    valor= request.args.get("preco")
    qtdd= request.args.get("qtd")
    tipo= request.args.get("tipo")
    with db_session:
        p= Prod(cod_barra=cod, nome_prod=produto, preco_prod=valor, qtd=qtdd, tipo_prod=tipo)
        commit()
        return redirect("listar_prod") 
