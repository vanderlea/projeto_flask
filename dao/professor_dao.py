from dao.db_config import get_connection

class ProfessorDAO:

    sqlSelect = 'SELECT id, nome, disciplina from professor'

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        return lista

    def excluir(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlDelete, (id,))
        conn.commit()  
        cursor.close()
        conn.close()

    def buscar_por_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelectId, (id,))
        professor = cursor.fetchone() 
        cursor.close()
        conn.close()
        return professor

    def salvar_edicao(self, id, nome, disciplina):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
        'UPDATE professor SET nome = %s, disciplina = %s WHERE id = %s',
        (nome, disciplina, id)
    )
        conn.commit()
        cursor.close()
        conn.close()

    def inserir(self, nome, disciplina):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO professor (nome, disciplina) VALUES (%s, %s)',
            (nome, disciplina)
        )
        conn.commit()
        cursor.close()
        conn.close()