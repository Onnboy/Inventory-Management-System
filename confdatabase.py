import mysql.connector
from datetime import datetime

class DataBase:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='71208794',
            database='cursoinfinity'
        )
        self.cursor = self.conexao.cursor()
    
    def inserir_produto(self, nome, descricao, quantidade, preco):
        query = """ INSERT INTO Produtos (Nome, Descricao, Quantidade_disponivel, Preco) VALUES (%s, %s, %s, %s)"""
        valores = (nome, descricao, quantidade, preco)
        self.cursor.execute(query, valores)
        self.conexao.commit()

    def listar_produtos(self):
        query = "SELECT * FROM Produtos"
        self.cursor.execute(query)
        produtos = self.cursor.fetchall()
        if produtos:
            for produto in produtos:
                print(f"ID: {produto[0]}, Nome: {produto[1]}, Quantidade: {produto[3]}, Preço: {produto[4]}")
        else:
            print("Nenhum produto cadastrado!")
        return produtos
    
    def buscar_produto_por_id(self, id_produto):
        query = "SELECT * FROM Produtos WHERE id = %s"
        self.cursor.execute(query, (id_produto,))
        return self.cursor.fetchone()
    
    def atualizar_quantidade(self, id_produto, nova_quantidade):
        query = "UPDATE Produtos SET Quantidade_disponivel = %s WHERE id = %s"
        self.cursor.execute(query, (nova_quantidade, id_produto))
        self.conexao.commit()

    def remover_produto(self, produto_id):
        query = "DELETE FROM Produtos WHERE ID = %s"
        self.cursor.execute(query, (produto_id,))
        self.conexao.commit()

    def registrar_venda(self, produto_id, quantidade):
        query = """
        INSERT INTO Vendas (ID_Produto_Vendido, Quantidade_Vendida, Data_Venda) VALUES (%s, %s, %s)
        """
        data_venda = datetime.now().strftime("%Y-%m-%d")
        valores = (produto_id, quantidade, data_venda)
        self.cursor.execute(query, valores)
        self.conexao.commit()

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()