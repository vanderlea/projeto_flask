from flask import Flask, render_template
import sqlite3

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
def lista_alunos():
    BD_PATH = 'banco_de_dad9s.db'
    conn = sqlite3.connect(BD_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, idade, cidade FROM alunos")
    lista_alunos = cursor.fetchall()
    conn.close()
    return render_template('aluno/lista.html', lista_alunos=lista_alunos)

@app.route('/professor')
def lista_professores():
    BD_PATH = 'banco_de_dad9s.db'
    conn = sqlite3.connect(BD_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, idade, cidade FROM professores")
    lista_professores = cursor.fetchall()
    conn.close()
    return render_template('professor/lista.html', lista_professores=lista_professores)

@app.route('/ajuda')
def ajuda():
    return render_template('ajuda do sistema/ajuda.html')


if __name__ == '__main__':
    app.run(debug=True)