from itertools import count
import confdatabase
import questionary
import sys
class EstoqueMenuVisual:
    def __init__(self, db):
        self.db = db

    def exibir_menu(self):
        escolha = questionary.select(
            "Escolha uma opção:",
            choices=[
                'Cadastrar novo produto',
                'Consultar produtos cadastrados',
                'Atualizar quantidade dos produtos',
                'Remover produto do cadastro',
                'Registrar venda',
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
            elif escolha == "Atualizar quantidade dos produtos":
                self.atualizar_quantidade_produto()
            elif escolha == 'Remover produto do cadastro':
                self.remover_produto()
            elif escolha == 'Registrar venda':
                self.registrar_venda()
            elif escolha == 'Sair':
                self.sair()

    def cadastrar_produto(self):
        print("\n--- Cadastrar Produto ---")
        nome = input("Nome do produto: ").strip()
        while not nome:
            print("O nome do produto não pode estar vazio")
            nome = input("Nome do produto: ").strip()

        descricao = input("Descrição do produto: ").strip()
        while not descricao:
            print("A descrição do produto não pode estar vazia")
            descricao = input("Descrição do produto: ").strip()

        while True:
            try:
                quantidade = int(input("Quantidade inicial: "))
                if quantidade < 0:
                    raise ValueError("Quantidade inicial não pode ser negativa! ")
                break
            except ValueError as e:
                print(f"Erro: {e}")
            
        while True:
            try:
                preco = float(input("Preço: "))
                if preco <= 0:
                    raise ValueError("O preço deve ser maior que zero")
                break
            except ValueError as f:
                print(f"Erro: {f}")

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

    def remover_produto(self):
        print("\n--- Remover Produto ---")
        try:
            produto_id = int(input("ID do produto a remover: "))
            produto = self.db.buscar_produto_por_id(produto_id)
            if produto:
                self.db.remover_produto(produto_id)
                print(f"Produto '{produto[1]}' removido com sucesso!")
            else:
                print(f"Produto não encotrado")
        except ValueError:
            print("Por favor, insira um ID válido!")

    def atualizar_quantidade_produto(self):
        print("\n--- Atualizar Quantidade dos Produtos ---")
        try:
            id_produto = int(input("Digite o ID do produto que deseja atualizar: "))
            produto = self.db.buscar_produto_por_id(id_produto)
            if produto:
                while True:
                    try:
                        nova_quantidade = int(input("Digite a nova quantidade: "))
                        if nova_quantidade < 0:
                            raise ValueError("A quantidade não pode ser negativa")
                        break
                    except ValueError as e:
                        print(f"Erro: {e}")
                self.db.atualizar_quantidade(id_produto, nova_quantidade)
                print(f"Quantidade do produto '{produto[1]}' atualizada para {nova_quantidade}!")
            else:
                print(f"Produto com ID {id_produto} não  encontrado")
        except ValueError:
                print("Por favor, insira um ID válido")

    def registrar_venda(self):
        print("\n--- Registrar Venda ---")
        try:
            produto_id = int(input("ID do produto vendido: "))
            quantidade_vendida = int(input("Quantidade vendida: "))

            produto = self.db.buscar_produto_por_id(produto_id)
            if produto:
                if produto[3] >= quantidade_vendida:
                    self.db.registrar_venda(produto_id, quantidade_vendida)
                    nova_quantidade = produto[3] - quantidade_vendida
                    self.db.atualizar_quantidade(produto_id, nova_quantidade)
                    print(f"Venda registrada! Quantidade atual de '{produto[1]}': {nova_quantidade}")
                else:
                    print("Produto não encontrado ou quantidade insuficiente!")
            else:
                print("Produto não encontrado!")
        except ValueError:
            print("Por favor, insira valores válidos para o ID e a quantidade")

    def sair(self):
        print(f"\nAté logo!:)")
        self.db.fechar_conexao()
        sys.exit()

if __name__ == "__main__":
    db = confdatabase.DataBase()
    menu = EstoqueMenuVisual(db)
    menu.executar()
