from flask import Flask, render_template, request, redirect, flash
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.turma_dao import TurmaDAO
from dao.curso_dao import CursoDAO


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('dashboard/index.html')

@app.route('/sobre')
def sobre_o_sistema():
    return render_template('dashboard/sobre.html')

@app.route('/contato')
def contato():
    return render_template('dashboard/contato.html')

@app.route('/aluno')
def lista():
    dao = AlunoDAO()
    lista = dao.listar()
    return render_template('aluno/lista.html', lista=lista)

@app.route('/aluno/excluir/<int:id_aluno>')
def excluir_aluno(id_aluno):
    dao = AlunoDAO()
    dao.excluir(id_aluno)
    return redirect('/aluno')

@app.route('/aluno/editar/<int:id_aluno>', methods=['GET', 'POST'])
def editar_aluno(id_aluno):
    dao = AlunoDAO()
    
    if request.method == 'POST':
    
        nome = request.form['nome']
        idade = request.form['idade']
        cidade = request.form['cidade']
        
        dao.salvar_edicao(id_aluno, nome, idade, cidade)
        return redirect('/aluno')
        
    aluno = dao.buscar_por_id(id_aluno)
    return render_template('aluno/editar.html', aluno=aluno)

@app.route('/aluno/cadastrar', methods=['GET', 'POST'])
def cadastrar_aluno():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        cidade = request.form['cidade']
        
        dao = AlunoDAO()
        dao.inserir(nome, idade, cidade=cidade) 
        return redirect('/aluno')
        
    return render_template('aluno/cadastrar.html')




@app.route('/turma/excluir/<int:id_turma>')
def excluir_turma(id_turma):
    dao = TurmaDAO()
    dao.excluir(id_turma)
    return redirect('/turma')

@app.route('/turma/editar/<int:id_turma>', methods=['GET', 'POST'])
def editar_turma(id_turma):
    dao = TurmaDAO()
    if request.method == 'POST':
        nome = request.form['nome']
        id_curso = request.form['id_curso']
        dao.salvar_edicao(id_turma, nome, id_curso)
        return redirect('/turma')
        
    turma = dao.buscar_por_id(id_turma)
    return render_template('turma/editar.html', turma=turma)

@app.route('/curso/excluir/<int:id_curso>')
def excluir_curso(id_curso):
    dao = CursoDAO()
    dao.excluir(id_curso)
    return redirect('/curso')

@app.route('/curso/editar/<int:id_curso>', methods=['GET', 'POST'])
def editar_curso(id_curso):
    dao = CursoDAO()
    if request.method == 'POST':
        nome = request.form['nome']
        dao.salvar_edicao(id_curso, nome)
        return redirect('/curso')
        
    curso = dao.buscar_por_id(id_curso)
    return render_template('curso/editar.html', curso=curso)

    

@app.route('/professor')
def listar_professor():
    dao = ProfessorDAO()
    lista = dao.listar()
    return render_template('professor/lista.html', lista=lista)

@app.route('/professor/editar/<int:id_professor>')
def editar_professor(id_professor):
    return f"Página de edição do professor com ID: {id_professor}"

@app.route('/professor/excluir/<int:id_professor>')
def excluir_professor(id_professor):
    dao = ProfessorDAO()
    dao.excluir(id_professor)
    return redirect('/professor') 

@app.route('/professor/cadastrar', methods=['GET', 'POST'])
def cadastrar_professor():
    if request.method == 'POST':
        nome = request.form['nome']
        disciplina = request.form['disciplina']
        
        dao = ProfessorDAO()
        dao.inserir(nome, disciplina)
        return redirect('/professor')
        
    return render_template('professor/cadastrar.html')

@app.route('/turma')
def listar_turma():
    dao = TurmaDAO()
    lista = dao.listar()
    return render_template('turma/lista.html', lista=lista)

@app.route('/turma/cadastrar', methods=['GET', 'POST'])
def cadastrar_turma():
    if request.method == 'POST':
        nome = request.form['nome']
        id_curso = request.form['id_curso']
        
        dao = TurmaDAO()
        dao.inserir(nome, id_curso)
        return redirect('/turma')
        
    return render_template('turma/cadastrar.html')

@app.route('/curso')
def listar_curso():
    dao = CursoDAO()
    lista = dao.listar()
    return render_template('curso/lista.html', lista=lista)

@app.route('/curso/cadastrar', methods=['GET', 'POST'])
def cadastrar_curso():
    if request.method == 'POST':
        nome = request.form['nome']
        
        dao = CursoDAO()
        dao.inserir(nome)
        return redirect('/curso')
        
    return render_template('curso/cadastrar.html')

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    senha = request.form['senha']
    email = request.form['email']
    dados= f'Usuário: {usuario}, Senha: {senha}, Email: {email}'
    return render_template('saudacao/saudacao.html', valor_recebido=dados)

@app.route('/saudacao')        
@app.route('/saudacao/<nome>') 
def saudacao(nome="Visitante"):
    return render_template('saudacao/saudacao.html', valor_recebido=nome)


@app.route('/ajuda')
def ajuda():
    
    return render_template('ajuda/ajuda.html')

@app.route('/desafio')
def desafio1():
    return render_template('dashboard/desafio.html')

if __name__ == '__main__':
    app.run(debug=True)

