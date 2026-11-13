
from dao.db_config import get_connection

class TurmaDAO:

    sqlSelect = '''
        SELECT
            turma.id,
            turma.semestre,
            curso.nome_curso,
            professor.nome
        FROM turma
        INNER JOIN curso ON curso.id = turma.curso_id
        INNER JOIN professor ON professor.id = turma.professor_id
        ORDER BY turma.id DESC
    '''

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(self.sqlSelect)
            turmas = cursor.fetchall()
            return turmas

        except Exception as e:
            print("Erro ao listar turmas:", str(e))
            return []

        finally:
            cursor.close()
            conn.close()

    def listar_cursos(self):
        return self.listar()

    def salvar(self, id, semestre, curso_id, professor_id):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            if id:
                cursor.execute('''
                    UPDATE turma
                    SET semestre = %s,
                        curso_id = %s,
                        professor_id = %s
                    WHERE id = %s
                ''', (semestre, curso_id, professor_id, id))
            else:
                cursor.execute('''
                    INSERT INTO turma (semestre, curso_id, professor_id)
                    VALUES (%s, %s, %s)
                ''', (semestre, curso_id, professor_id))

            conn.commit()
            return {"status": "ok"}

        except Exception as e:
            conn.rollback()
            print("Erro ao salvar turma:", str(e))
            return {"status": "erro", "mensagem": str(e)}

        finally:
            cursor.close()
            conn.close()

    def buscar_por_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute('''
                SELECT id, semestre, curso_id, professor_id
                FROM turma
                WHERE id = %s
            ''', (id,))

            return cursor.fetchone()

        finally:
            cursor.close()
            conn.close()

    def remover(self, id):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                'DELETE FROM turma WHERE id = %s', (id,)
            )
            conn.commit()
            return {"status": "ok"}

        except Exception as e:
            conn.rollback()
            return {"status": "erro", "mensagem": str(e)}

        finally:
            cursor.close()
            conn.close()
