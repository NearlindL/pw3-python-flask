from flask import render_template, request, redirect, url_for


def init_app(app):
    lista_bosses = [
        {
            "nome": "Yhorm The Giant",
            "localizacao": "Profaned Capital",
            "fraqueza": "Lightning, Dark",
            "resistencia": "Slash, Thrust",
        },
        {
            "nome": "Dragonslayer Armour",
            "localizacao": "Lothric Castle",
            "fraqueza": "Frost, Strike",
            "resistencia": "Lightning, Dark, Slash",
        },
        {
            "nome": "Soul of Cinder",
            "localizacao": "Kiln of the First Flame",
            "fraqueza": "Lightning, Dark",
            "resistencia": "Fire, Bleed",
        },
    ]

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/boss')
    def boss():
        return render_template('boss.html', listaBosses=lista_bosses)

    @app.route('/formulario', methods=['GET', 'POST'])
    def formulario():
        if request.method == 'POST':
            lista_bosses.append(
                {
                    "nome": request.form.get('nome'),
                    "localizacao": request.form.get('localizacao'),
                    "fraqueza": request.form.get('fraqueza'),
                    "resistencia": request.form.get('resistencia'),
                }
            )
            return redirect(url_for('boss'))

        return render_template('formulario.html')

