# comentario em python
# importando o flask na aplicação
from flask import Flask, render_template #render_template renderisa as paginas html
#carregando o flask em uma variavel
app = Flask(__name__, template_folder='views') 
#__name__ é uma variavel de ambiemte do python que tem onome do modulo atual

#criando a rota principal do site
@app.route('/')
#def serve para criar uma fumção do no python
def home():
    return render_template('index.html')

@app.route('/games')
def games():
    titulo = "SilkSong"
    ano = 2025
    categoria = "metroid vania"
    
    jogadores = ['Eduardo', 'Ana', 'Guilherme', 'Caio', 'Antônio']
    
    return render_template('games.html',
                           titulo=titulo,
                           ano=ano,
                           categoria=categoria,
                           jogadores=jogadores
                           )

                            

@app.route('/consoles')
def consoles():
    return render_template('consoles.html') 
#iniciando o servidor web
if __name__ == '__main__': app.run(debug=True)
#verificando se app.py for o arquivo principal ele inicia o sevidor
#declarando uma variavel




