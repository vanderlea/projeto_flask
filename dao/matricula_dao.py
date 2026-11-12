from dao.db_config import get_connection

class MatriculaDAO:

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT matricula.id, turma.semestre, aluno.nome, curso.nome_curso, professor.nome, professor.disciplina
        FROM matricula
        JOIN turma ON matricula.turma_id = turma.id
        JOIN aluno ON matricula.aluno_id = aluno.id
        JOIN curso ON matricula.curso_id = curso.id
        JOIN professor ON turma.professor_id = professor.id
        ORDER BY matricula.id DESC
        """)
        lista = cursor.fetchall()
        conn.close()
        return lista
    
    def listar_alunos(self):
         conn = get_connection()
         cursor = conn.cursor()
         cursor.execute("SELECT id, nome FROM aluno ORDER BY nome")
         lista = cursor.fetchall()
         cursor.close()
         conn.close()
         return lista
        
    def listar_turmas(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT turma.id, turma.semestre, curso.nome_curso, professor.nome, professor.disciplina
        FROM turma
        JOIN curso ON turma.curso_id = curso.id
        JOIN professor ON turma.professor_id = professor.id
        ORDER BY turma.id DESC""")
        lista = cursor.fetchall()
        cursor.close()
        conn.close()
        return lista
        


    def buscar_por_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, aluno_id, turma_id FROM matricula WHERE id = %s', (id,))
        matricula = cursor.fetchone()
        cursor.close()
        conn.close()
        return matricula

    def salvar_edicao(self, id, aluno_id, turma_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT curso_id FROM turma WHERE id = %s', (turma_id,))
            resultado = cursor.fetchone()
            if not resultado:
                return {"status": "erro", "mensagem": "Turma não encontrada."}
            curso_id = resultado[0]
            if id:
                cursor.execute("""UPDATE matricula SET aluno_id = %s, curso_id = %s, turma_id = %s WHERE id = %s""", (aluno_id, curso_id, turma_id, id))
            else:
                cursor.execute('INSERT INTO matricula (aluno_id, curso_id, turma_id) VALUES (%s, %s, %s)', (aluno_id, curso_id, turma_id))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            conn.rollback()
            return {"status": "erro", "mensagem": str(e)}
        finally:
            cursor.close()
            conn.close()
    
    def remover(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM matricula WHERE id = %s', (id,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            conn.rollback()
            return {"status": "erro", "mensagem": str(e)}
        finally:
            cursor.close()
            conn.close()