from itertools import count
import confdatabase
import questionary
import sys
import logging

class EstoqueMenuVisual:
    def __init__(self, db):
        self.db = db

    def exibir_menu(self):
        escolha = questionary.select(
            "Escolha uma opção:",
            choices=[
                'Cadastrar novo produto',
                'Consultar produtos cadastrados',
                'Atualizar  quantidade de produto',
                'Remover produto do cadastro',
                'Sair'
            ]
        ).ask()
        return escolha

    def executar(self):
        for _ in count():
            escolha = self.exibir_menu()
            if escolha == 'Cadastrar novo produto':
                self.cadastrar_produto()
            elif escolha == 'Consultar produtos cadastrados':
                self.consultar_produtos()
            elif escolha == "Atualizar quantidade de produto":
                self.atualizar_quantidade_produto()
            elif escolha == 'Remover produto do cadastro':
                self.remover_produto()
            elif escolha == 'Sair':
                self.sair()

    def cadastrar_produto(self):
        print("\n--- Cadastrar Produto ---")
        nome = input("Nome do produto: ")
        descricao = input("Descrição do produto: ")
        quantidade = int(input("Quantidade inicial: "))
        preco = float(input("Preço: "))
        self.db.inserir_produto(nome, descricao, quantidade, preco)
        print(f"Produto '{nome}' cadastrado com sucesso!")

    def consultar_produtos(self):
        print("\n--- Produtos Cadastrados ---")
        produtos = self.db.listar_produtos()
        if produtos:
            for produto in produtos:
                print(f"ID: {produto[0]} | Nome: {produto[1]} | Quantidade: {produto[3]} | Preço: R$ {produto[4]:.2f}")
        else:
            print("Nenhum produto cadastrado!")

        # Listagem dos produtos no BD (Banco de Dados.)
        print("Exibindo produtos cadastrados..")

    def remover_produto(self):
        print("\n--- Remover Produto ---")
        produto_id = input("ID do produto a remover: ")
        self.db.remover_produto(produto_id)
        print(f"Produto {produto_id} removido com sucesso!")
        # Remoção no BD

    def atualizar_quantidade_produto(self):
        print("\n--- Atualizar Quantidade de Produto ---")
    
        try:
            id_produto = int(input("Digite o ID do produto que deseja atualizar: "))
            nova_quantidade = int(input("Digite a nova quantidade: "))

            # Verifica se o produto existe
            produto = self.db.buscar_produto_por_id(id_produto)
            if produto:
                self.db.atualizar_quantidade(id_produto, nova_quantidade)
                print(f"Quantidade do produto '{produto[1]}' atualizada para {nova_quantidade}!")
            else:
                print(f"Produto com ID {id_produto} não encontrado.")
        except ValueError:
            print("Por favor, insira valores válidos para o ID e a quantidade.")

    def sair(self):
        print(f"\nAté logo!:)")
        sys.exit()

if __name__ == "__main__":
    db = database.DataBase()
    menu = EstoqueMenuVisual(db)
    menu.executar()
