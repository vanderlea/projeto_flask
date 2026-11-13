from flask import Flask, render_template, request, redirect, flash
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.turma_dao import TurmaDAO
from dao.curso_dao import CursoDAO
from dao.matricula_dao import MatriculaDAO


app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'  

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

 #salvar aluno
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

@app.route('/turma')
def listar_turma():
    dao = TurmaDAO()
    lista = dao.listar()
    return render_template('turma/lista.html', lista=lista)

@app.route("/turma/form")
def form_turma():
    cursos = CursoDAO().listar()
    professores = ProfessorDAO().listar()
    return render_template('turma/form.html', turma=None, cursos=cursos, professores=professores)

@app.route('/turma/editar/<int:id>')
def editar_turma(id):
    dao = TurmaDAO()
    turma = dao.buscar_por_id(id)
    cursos = CursoDAO().listar()
    professores = ProfessorDAO().listar()
    return render_template('turma/form.html', turma=turma, cursos=cursos, professores=professores)

@app.route('/turma/cadastrar', methods=['GET', 'POST'])
def cadastrar_turma():
    if request.method == 'POST':
        nome = request.form['nome']
        id_curso = request.form['id_curso']
        
        dao = TurmaDAO()
        dao.salvar(None, nome, id_curso, professor_id=request.form['professor_id'])
        return redirect('/turma')
        
    return render_template('turma/cadastrar.html')


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


@app.route('/matricula')
def listar_matriculas():
    dao = MatriculaDAO()
    lista = dao.listar()
    return render_template('matricula/lista.html', lista=lista)

@app.route('/matricula/form')
def form_matricula():
    lista_alunos = AlunoDAO().listar()
    lista_turmas = TurmaDAO().listar() 
    return render_template('matricula/form.html', matricula=None, alunos=lista_alunos, turmas=lista_turmas)

@app.route('/matricula/salvar', methods=['POST'])
@app.route('/matricula/salvar/<int:id>', methods=['POST'])
def salvar_matricula(id=None):
    aluno_id = request.form['aluno_id']
    turma_id = request.form['turma_id']
    dao = MatriculaDAO()
    resultado = dao.salvar_edicao(id, aluno_id, turma_id)
    
    if resultado["status"] == "ok":
        flash("Matrícula salva com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
        
    return redirect('/matricula')

@app.route('/matricula/editar/<int:id>')
def editar_matricula(id):
    dao = MatriculaDAO()
    matricula = dao.buscar_por_id(id)
    if matricula is None:
        flash("Matrícula não encontrada.", "danger")
        return redirect('/matricula')
    lista_alunos = AlunoDAO().listar()
    lista_turmas = TurmaDAO().listar()
    
    return render_template('matricula/form.html', matricula=matricula, lista_alunos=lista_alunos, lista_turmas=lista_turmas)

@app.route('/matricula/remover/<int:id>')
def remover_matricula(id):
    dao = MatriculaDAO()
    resultado = dao.remover(id)
    
    if resultado["status"] == "ok":
        flash("Matrícula removida com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
        
    return redirect('/matricula')

    

@app.route('/professor')
def listar_professor():
    dao = ProfessorDAO()
    lista = dao.listar()
    return render_template('professor/lista.html', lista=lista)

@app.route('/professor/editar/<int:id_professor>')
def editar_professor(id_professor):
    return f"Página de edição do professor com ID: {id_professor}"

@app.route('/professor/remover/<int:id_professor>')
def remover_professor(id_professor):
    dao = ProfessorDAO()
    dao.remover(id_professor)
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
    return render_template('desafio/desafio.html')

if __name__ == '__main__':
    app.run(debug=True)

