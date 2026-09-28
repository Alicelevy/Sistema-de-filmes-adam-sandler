from app import create_app
from database import create_tables, create_test_user


create_tables()
create_test_user()

app = create_app()


if __name__ == "__main__":
    app.run(debug=True)