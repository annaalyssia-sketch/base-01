from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

import database


auth_bp = Blueprint("auth", __name__)

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":

        Nome = request.form["Nome"]
        Email = request.form["Email"]
        Senha = request.form["Senha"]

        flash("Implemente o cadastro com hash de senha.")
        return redirect(url_for("registro"))

    return render_template("registro.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        flash("Implemente o login com session.")
        return redirect(url_for("login"))

     if session: 
            session["usuario_id"] = usuario[0]
            session["usuario_nome"] = usuario[0]

    return render_template("login.html")

@app.route("/cadastro", methods = ["GET", "POST"])
def cadastro():

    if request.methods == "POST":

        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]

        banco = conectar_banco()

        banco.execute(
            "INSERT INTO usuarios (nome, email, senha) VALUES(?, ?, ?)", 
            (nome, email, senha)
        )

        banco.commit()
        banco.close()

        return "Cadastro realizado"
        return render_template("cadastro.html")


@app.route("/Login", methods = ["GET", "POST"])
def Login():

    if request.methods == "POST":

        email = request.form["email"]
        senha = request.form["senha"]

        banco = conectar_banco()

        banco.execute(
            "SELECT * FROM usuarios WHERE email = ? AND senha = ?", 
            (email, senha)
        ).fetchone

        banco.close()

        if usuario: 
            session["usuario_id"] = usuario[0]
            return redirect("/area")

        return "email ou senha incorreta"
        return render_template("login.html")


@app.route("/logout")
def logout():
    flash("Implemente o logout com session.")
    return redirect(url_for("index"))


# Complete este arquivo durante a avaliação.
#
# O Blueprint já está criado, mas nenhuma rota foi vinculada ainda.
# Implemente aqui:
#
# - a rota /registro;
# - a rota /login;
# - a rota /logout.
