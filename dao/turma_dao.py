from dao.db_config import get_connection

class TurmaDAO:

    sqlSelect = 'SELECT id, semestre, curso_id, professor_id from turma'

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        return lista

    def excluir(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM turma WHERE id = %s', (id,))
        conn.commit()
        cursor.close()
        conn.close()

    def buscar_por_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, nome, id_curso FROM turma WHERE id = %s', (id,))
        turma = cursor.fetchone()
        cursor.close()
        conn.close()
        return turma

    def salvar_edicao(self, id, nome, id_curso):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE turma SET nome = %s, id_curso = %s WHERE id = %s', (nome, id_curso, id))
        conn.commit()
        cursor.close()
        conn.close()

    def inserir(self, nome, id_curso):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO turma (nome, id_curso) VALUES (%s, %s)",
            (nome, id_curso)
        )
        conn.commit()
        cursor.close()
        conn.close()