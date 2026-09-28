from flask import Blueprint, render_template, session

from app.middleware import login_required


home = Blueprint("home", __name__)


@home.route("/")
@login_required
def home_page():

    usuario = session["usuario"]

    return render_template(
        "home.html",
        usuario=usuario
    )