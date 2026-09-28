from functools import wraps

from flask import session, redirect, url_for


def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if "usuario" not in session:
            return redirect(url_for("auth.login"))

        return func(*args, **kwargs)

    return wrapper


def guest_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if "usuario" in session:
            return redirect(url_for("home.home_page"))

        return func(*args, **kwargs)

    return wrapper