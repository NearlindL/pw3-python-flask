# comentario em python
# importando o flask na aplicação
from flask import Flask
# carregando o flask em uma variavel
from controllers import routes

app = Flask(__name__, template_folder='views')
# __name__ é uma variavel de ambiemte do python que tem o nome do modulo atual

routes.init_app(app)
if __name__ == '__main__':
    app.run(debug=True)




