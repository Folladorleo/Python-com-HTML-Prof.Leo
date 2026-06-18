from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    nome = "Turma de Programação"
    curso = "Python com HTML"

    return render_template(
        'index.html',
        nome = nome,
        curso = curso
    )

@app.route('/sobre')
def sobre():
    return"""
    <h1>Sobre o Projeto</H1>
    <p>Este projeto foi criado usando Python e Flask.</p>
    <a href="/">Volta para o inicio</a>
    """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)