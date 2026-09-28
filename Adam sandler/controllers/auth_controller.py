from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from database import get_connection
from app.middleware import guest_required


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
@guest_required
def login():

    erro = None

    if request.method == "POST":

        username = request.form["usuario"]
        password = request.form["senha"]

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id, username, password_hash
            FROM users
            WHERE username = ?
            """,
            (username,)
        )

        usuario = cursor.fetchone()

        connection.close()

        if usuario and check_password_hash(
            usuario["password_hash"],
            password
        ):

            session["user_id"] = usuario["id"]

            return redirect(
                url_for("home.home_page")
            )

        erro = "Usuário ou senha inválidos."

    return render_template(
        "login.html",
        erro=erro
    )


@auth.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("auth.login")
    )