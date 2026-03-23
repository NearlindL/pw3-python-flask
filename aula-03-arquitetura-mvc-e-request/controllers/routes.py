from flask import render_template

def init_app(app):
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
        game = {
            "Título": "Minicraft",
            "Ano": 2012,
            "Categoria": "Sandbox"
        }
        
        jogadores = ['Eduardo', 'Ana', 'Guilherme', 'Caio', 'Antônio']
        
        return render_template('games.html',
                            titulo=titulo,
                            ano=ano,
                            categoria=categoria,
                            jogadores=jogadores,
                            game=game
                            )
        

                                

    @app.route('/consoles')
    def console():
        consoles = ['xbox 360', 'nintendo ds', 'wii', 'P5', 'P2']
        
        return render_template('consoles.html',
                            consoles=consoles) 