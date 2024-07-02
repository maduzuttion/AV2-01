from flask import Flask, render_template, request, redirect
from pony.orm import *

db=Database()
app=Flask(__name__)

class Produto(db.Entity):
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
def about():
    return render_template("sobre.html")

@app.route("/listar_produto")
def listar_prod():
    with db_session:
        produtos=Produto.select() 
        return render_template("listar_prod.html", produtos=produtos)

@app.route("/form_produto")
def form_prod():
    return render_template("form_prod.html")

@app.route("/cadastrar_novo_produto")
def cadastrar_novo_produto():
    cod_bar=request.args.get("cod")
    nome_prod= request.args.get("produto")
    preco= request.args.get("preco")
    qtdd= request.args.get("qtd")
    tipo= request.args.get("tipo")
    with db_session:
        i= Produto(**request.args)
        commit()
        return redirect("listar_prod") 
