from dao.db_config import get_connection

class AlunoDAO:



    sqlSelect = "SELECT id, nome, idade, cidade FROM aluno"

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        cursor.close() 
        conn.close() 
        return lista

    def excluir(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM aluno WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()

    def buscar_por_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, idade, cidade FROM aluno WHERE id = %s", (id,))
        aluno = cursor.fetchone()
        cursor.close()
        conn.close()
        return aluno

    def salvar_edicao(self, id, nome, idade, cidade):
         conn = get_connection()
         cursor = conn.cursor()
         cursor.execute(
         "UPDATE aluno SET nome = %s, idade = %s, cidade = %s WHERE id = %s",
         (nome, idade, cidade, id)
         )
         conn.commit()
         cursor.close()
         conn.close()

    def inserir(self, nome, idade, cidade):
         conn = get_connection()
         cursor = conn.cursor()
         cursor.execute(
         "INSERT INTO aluno (nome, idade, cidade) VALUES (%s, %s, %s)",
         (nome, idade, cidade)
         )
         conn.commit()
         cursor.close()
         conn.close()

    def alterar(self, aluno):
        sql = "UPDATE aluno SET nome = %s, idade = %s, cidade = %s WHERE id = %s"
        cursor = self.conn.cursor()
        cursor.execute(sql, (aluno.nome, aluno.idade, aluno.cidade, aluno.id))
        self.conn.commit() 
        cursor.close()