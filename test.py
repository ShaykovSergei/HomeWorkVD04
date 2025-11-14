from flask import Flask

app = Flask(__name__)








# @app.route("/")
# def hello_world():
#     html = """
#     <h1>тестовый запуск локального сервера</h1>
#     <p>А это просто текст</p>
#     """
#     return html



# @app.route("/")
# @app.route("/<password>/")
# def hello_world(password=None):
#     if password == "1234":
#         return f"Доступ разрешен"
#     else:
#         return f"Доступ запрещен"



# @app.route("/")
# def hello_world():
#     return "Hello World!"
#
# @app.route("/new")
# @app.route("/newpage")
# @app.route("/новая страница")
# def new():
#     return "new page"


if __name__ == "__main__":
    app.run()