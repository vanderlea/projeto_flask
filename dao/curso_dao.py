from dao.db_config import get_connection

class CursoDAO:

    sqlSelect = "SELECT id, nome_curso, duracao from curso"

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        return lista

    def excluir(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM curso WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()

    def buscar_por_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome FROM curso WHERE id = %s", (id,))
        curso = cursor.fetchone()
        cursor.close()
        conn.close()
        return curso

    def salvar_edicao(self, id, nome):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE curso SET nome = %s WHERE id = %s", (nome, id))
        conn.commit()
        cursor.close()
        conn.close()

    def inserir(self, nome):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO curso (nome) VALUES (%s)",
            (nome,)
        )
        conn.commit()
        cursor.close()
        conn.close()