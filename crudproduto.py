from conexao import Conexao

class CRUDProduto:
    def inserir(self, nome, preco, id_categoria):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()
        sql = """INSERT INTO produto (
                 nome, preco, id_categoria) 
                 VALUES (%s, %s, %s)
             """
        cursor.execute(sql, (nome, preco, id_categoria))
        conexao.commit()
        cursor.close()
        conexao.close()

    def listar(self):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = "SELECT id, nome, preco, id_categoria FROM produto"
        cursor.execute(sql)
        produtos = cursor.fetchall()
        cursor.close()
        conexao.close()
        return produtos
    
    def buscar_por_id(self, id_produto):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT id, nome, preco, id_categoria 
            FROM produto
            WHERE id = %s
        """
        cursor.execute(sql, (id_produto,))
        produto = cursor.fetchone()
        cursor.close()
        conexao.close()
        return produto
    
    def atualizar(self, id_produto, nome, preco, id_categoria):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = """
            UPDATE produto
            SET nome = %s, preco = %s, id_categoria = %s
            WHERE id = %s
        """
        cursor.execute(sql, (nome, preco, id_categoria, id_produto))
        conexao.commit()
        cursor.close()
        conexao.close()

    def excluir(self, id_produto):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()

        sql = "DELETE FROM produto WHERE id = %s"
        cursor.execute(sql, (id_produto,))
        conexao.commit()
        cursor.close()
        conexao.close()