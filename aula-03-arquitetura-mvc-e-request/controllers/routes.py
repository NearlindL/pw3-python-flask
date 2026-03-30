from flask import render_template, request, redirect, url_for

def init_app(app):
    
    listaGames = [{"titulo": "CS-GO", "ano": 2012, "categoria": "FPS Online"}]
    
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
        
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        
        if request.method == 'POST':
            listaGames.append({'titulo' : request.form.get ('titulo'), 'ano' : request.form.get ('ano'), 'categoria' : request.form.get ('categoria')})
            return redirect(url_for('cadgames')) 
        return render_template('cadgames.html', listaGames = listaGames)