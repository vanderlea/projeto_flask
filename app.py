from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sobre')
def sobre_o_sistema():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/aluno')
def alunos():
    return render_template('aluno/lista.html')

@app.route('/professor')
def lista_professores():
    return render_template('professor/lista.html')


if __name__ == '__main__':
    app.run(debug=True)