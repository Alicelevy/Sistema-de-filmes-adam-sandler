from werkzeug.security import generate_password_hash


usuarios = {
    "alice": generate_password_hash("1234"),
    "admin": generate_password_hash("admin123"),
    "teste": generate_password_hash("teste123")
}