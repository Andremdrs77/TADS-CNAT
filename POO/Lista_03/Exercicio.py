import json
from datetime import datetime
from pathlib import Path


class Cliente:
    def __init__(self, id, nome, email, fone):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_fone(self):
        return self.__fone

    def set_fone(self, fone):
        self.__fone = fone

    def __str__(self):
        return (f"ID: {self.__id} | Nome: {self.__nome} | "
                f"E-mail: {self.__email} | Telefone: {self.__fone}")

    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "fone": self.__fone
        }

    @classmethod
    def from_json(cls, dic):
        return cls(dic["id"], dic["nome"], dic["email"], dic["fone"])


class Categoria:
    def __init__(self, id, descricao):
        self.__id = id
        self.__descricao = descricao

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def __str__(self):
        return f"ID: {self.__id} | Descrição: {self.__descricao}"

    def to_json(self):
        return {"id": self.__id, "descricao": self.__descricao}

    @classmethod
    def from_json(cls, dic):
        return cls(dic["id"], dic["descricao"])


class Produto:
    def __init__(self, id, descricao, preco, estoque, id_categoria):
        self.__id = id
        self.__descricao = descricao
        self.__preco = preco
        self.__estoque = estoque
        self.__id_categoria = id_categoria

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco

    def get_estoque(self):
        return self.__estoque

    def set_estoque(self, estoque):
        self.__estoque = estoque

    def get_id_categoria(self):
        return self.__id_categoria

    def set_id_categoria(self, id_categoria):
        self.__id_categoria = id_categoria

    def __str__(self):
        return (f"ID: {self.__id} | Descrição: {self.__descricao} | "
                f"Preço: R$ {self.__preco:.2f} | Estoque: {self.__estoque} | "
                f"ID da categoria: {self.__id_categoria}")

    def to_json(self):
        return {
            "id": self.__id,
            "descricao": self.__descricao,
            "preco": self.__preco,
            "estoque": self.__estoque,
            "id_categoria": self.__id_categoria
        }

    @classmethod
    def from_json(cls, dic):
        return cls(dic["id"], dic["descricao"], dic["preco"],
                   dic["estoque"], dic["id_categoria"])


class Venda:
    def __init__(self, id, data=None, carrinho=False, total=0.0, id_cliente=0):
        self.__id = id
        self.__data = data if data is not None else datetime.now().isoformat(timespec="seconds")
        self.__carrinho = carrinho
        self.__total = total
        self.__id_cliente = id_cliente

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_carrinho(self):
        return self.__carrinho

    def set_carrinho(self, carrinho):
        self.__carrinho = carrinho

    def get_total(self):
        return self.__total

    def set_total(self, total):
        self.__total = total

    def get_id_cliente(self):
        return self.__id_cliente

    def set_id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente

    def __str__(self):
        return (f"ID: {self.__id} | Data: {self.__data} | "
                f"Carrinho: {self.__carrinho} | Total: R$ {self.__total:.2f} | "
                f"ID do cliente: {self.__id_cliente}")

    def to_json(self):
        return {
            "id": self.__id,
            "data": self.__data,
            "carrinho": self.__carrinho,
            "total": self.__total,
            "id_cliente": self.__id_cliente
        }

    @classmethod
    def from_json(cls, dic):
        return cls(dic["id"], dic["data"], dic["carrinho"],
                   dic["total"], dic["id_cliente"])


class VendaItem:
    def __init__(self, id, qtd, preco, id_venda=0, id_produto=0):
        self.__id = id
        self.__qtd = qtd
        self.__preco = preco
        self.__id_venda = id_venda
        self.__id_produto = id_produto

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_qtd(self):
        return self.__qtd

    def set_qtd(self, qtd):
        self.__qtd = qtd

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco

    def get_id_venda(self):
        return self.__id_venda

    def set_id_venda(self, id_venda):
        self.__id_venda = id_venda

    def get_id_produto(self):
        return self.__id_produto

    def set_id_produto(self, id_produto):
        self.__id_produto = id_produto

    def __str__(self):
        return (f"ID: {self.__id} | Quantidade: {self.__qtd} | "
                f"Preço: R$ {self.__preco:.2f} | ID da venda: {self.__id_venda} | "
                f"ID do produto: {self.__id_produto}")

    def to_json(self):
        return {
            "id": self.__id,
            "qtd": self.__qtd,
            "preco": self.__preco,
            "id_venda": self.__id_venda,
            "id_produto": self.__id_produto
        }

    @classmethod
    def from_json(cls, dic):
        return cls(dic["id"], dic["qtd"], dic["preco"],
                   dic["id_venda"], dic["id_produto"])



class DAO:
    classe = None
    arquivo = ""
    objetos = []

    @classmethod
    def Inserir(cls, obj):
        if cls.Listar_Id(obj.get_id()) is not None:
            raise ValueError("Já existe um registro com esse ID.")
        cls.objetos.append(obj)
        cls.Salvar()

    @classmethod
    def Listar(cls):
        return cls.objetos

    @classmethod
    def Listar_Id(cls, id):
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def Atualizar(cls, obj):
        for i, atual in enumerate(cls.objetos):
            if atual.get_id() == obj.get_id():
                cls.objetos[i] = obj
                cls.Salvar()
                return True
        return False

    @classmethod
    def Excluir(cls, id):
        for i, obj in enumerate(cls.objetos):
            if obj.get_id() == id:
                del cls.objetos[i]
                cls.Salvar()
                return True
        return False

    @classmethod
    def Abrir(cls):
        caminho = Path(cls.arquivo)
        if not caminho.exists():
            cls.objetos = []
            return

        try:
            with caminho.open("r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
            cls.objetos = [cls.classe.from_json(item) for item in dados]
        except (json.JSONDecodeError, TypeError, KeyError) as erro:
            raise ValueError(f"Não foi possível ler {cls.arquivo}: {erro}")

    @classmethod
    def Salvar(cls):
        with open(cls.arquivo, "w", encoding="utf-8") as arquivo:
            json.dump([obj.to_json() for obj in cls.objetos],
                      arquivo, ensure_ascii=False, indent=4)


class ClienteDAO(DAO):
    classe = Cliente
    arquivo = "clientes.json"
    objetos = []


class VendaDAO(DAO):
    classe = Venda
    arquivo = "vendas.json"
    objetos = []


class VendaItemDAO(DAO):
    classe = VendaItem
    arquivo = "venda_itens.json"
    objetos = []


class ProdutoDAO(DAO):
    classe = Produto
    arquivo = "produtos.json"
    objetos = []


class CategoriaDAO(DAO):
    classe = Categoria
    arquivo = "categorias.json"
    objetos = []



class UI:
    @staticmethod
    def Menu():
        print("\n========== SISTEMA DE COMÉRCIO ELETRÔNICO ==========")
        print("1 - Listar clientes")
        print("2 - Inserir cliente")
        print("3 - Atualizar cliente")
        print("4 - Excluir cliente")
        print("5 - Listar categorias")
        print("6 - Inserir categoria")
        print("7 - Atualizar categoria")
        print("8 - Excluir categoria")
        print("9 - Listar produtos")
        print("10 - Inserir produto")
        print("11 - Atualizar produto")
        print("12 - Excluir produto")
        print("0 - Finalizar")
        return input("Escolha uma opção: ").strip()

    @staticmethod
    def ler_id(mensagem="ID: "):
        return int(input(mensagem))

    @staticmethod
    def listar(dao, nome):
        print(f"\n--- {nome} cadastrados ---")
        objetos = dao.Listar()
        if not objetos:
            print("Nenhum registro cadastrado.")
            return
        for obj in objetos:
            print(obj)

    @staticmethod
    def inserir_cliente():
        print("\n--- Novo cliente ---")
        id = UI.ler_id()
        nome = input("Nome: ").strip()
        email = input("E-mail: ").strip()
        fone = input("Telefone: ").strip()
        ClienteDAO.Inserir(Cliente(id, nome, email, fone))
        print("Cliente cadastrado com sucesso.")

    @staticmethod
    def atualizar_cliente():
        id = UI.ler_id("ID do cliente que deseja atualizar: ")
        atual = ClienteDAO.Listar_Id(id)
        if atual is None:
            print("Cliente não encontrado.")
            return
        nome = input(f"Nome [{atual.get_nome()}]: ").strip() or atual.get_nome()
        email = input(f"E-mail [{atual.get_email()}]: ").strip() or atual.get_email()
        fone = input(f"Telefone [{atual.get_fone()}]: ").strip() or atual.get_fone()
        ClienteDAO.Atualizar(Cliente(id, nome, email, fone))
        print("Cliente atualizado com sucesso.")

    @staticmethod
    def excluir_cliente():
        id = UI.ler_id("ID do cliente que deseja excluir: ")
        if ClienteDAO.Excluir(id):
            print("Cliente excluído com sucesso.")
        else:
            print("Cliente não encontrado.")

    @staticmethod
    def inserir_categoria():
        print("\n--- Nova categoria ---")
        id = UI.ler_id()
        descricao = input("Descrição: ").strip()
        CategoriaDAO.Inserir(Categoria(id, descricao))
        print("Categoria cadastrada com sucesso.")

    @staticmethod
    def atualizar_categoria():
        id = UI.ler_id("ID da categoria que deseja atualizar: ")
        atual = CategoriaDAO.Listar_Id(id)
        if atual is None:
            print("Categoria não encontrada.")
            return
        descricao = input(f"Descrição [{atual.get_descricao()}]: ").strip()
        if not descricao:
            descricao = atual.get_descricao()
        CategoriaDAO.Atualizar(Categoria(id, descricao))
        print("Categoria atualizada com sucesso.")

    @staticmethod
    def excluir_categoria():
        id = UI.ler_id("ID da categoria que deseja excluir: ")
        if any(p.get_id_categoria() == id for p in ProdutoDAO.Listar()):
            print("Não é possível excluir: existem produtos vinculados a essa categoria.")
            return
        if CategoriaDAO.Excluir(id):
            print("Categoria excluída com sucesso.")
        else:
            print("Categoria não encontrada.")

    @staticmethod
    def inserir_produto():
        print("\n--- Novo produto ---")
        if not CategoriaDAO.Listar():
            print("Cadastre uma categoria antes de inserir produtos.")
            return
        id = UI.ler_id()
        descricao = input("Descrição: ").strip()
        preco = float(input("Preço: ").replace(",", "."))
        estoque = int(input("Estoque: "))
        id_categoria = UI.ler_id("ID da categoria: ")
        if CategoriaDAO.Listar_Id(id_categoria) is None:
            print("Categoria não encontrada. Produto não cadastrado.")
            return
        ProdutoDAO.Inserir(Produto(id, descricao, preco, estoque, id_categoria))
        print("Produto cadastrado com sucesso.")

    @staticmethod
    def atualizar_produto():
        id = UI.ler_id("ID do produto que deseja atualizar: ")
        atual = ProdutoDAO.Listar_Id(id)
        if atual is None:
            print("Produto não encontrado.")
            return

        descricao = input(f"Descrição [{atual.get_descricao()}]: ").strip()
        if not descricao:
            descricao = atual.get_descricao()

        entrada = input(f"Preço [{atual.get_preco()}]: ").strip()
        preco = float(entrada.replace(",", ".")) if entrada else atual.get_preco()

        entrada = input(f"Estoque [{atual.get_estoque()}]: ").strip()
        estoque = int(entrada) if entrada else atual.get_estoque()

        entrada = input(f"ID da categoria [{atual.get_id_categoria()}]: ").strip()
        id_categoria = int(entrada) if entrada else atual.get_id_categoria()

        if CategoriaDAO.Listar_Id(id_categoria) is None:
            print("Categoria não encontrada. Produto não atualizado.")
            return

        ProdutoDAO.Atualizar(Produto(id, descricao, preco, estoque, id_categoria))
        print("Produto atualizado com sucesso.")

    @staticmethod
    def excluir_produto():
        id = UI.ler_id("ID do produto que deseja excluir: ")
        if ProdutoDAO.Excluir(id):
            print("Produto excluído com sucesso.")
        else:
            print("Produto não encontrado.")

    @staticmethod
    def Main():
        for dao in (ClienteDAO, CategoriaDAO, ProdutoDAO,
                    VendaDAO, VendaItemDAO):
            dao.Abrir()

        operacoes = {
            "1": lambda: UI.listar(ClienteDAO, "Clientes"),
            "2": UI.inserir_cliente,
            "3": UI.atualizar_cliente,
            "4": UI.excluir_cliente,
            "5": lambda: UI.listar(CategoriaDAO, "Categorias"),
            "6": UI.inserir_categoria,
            "7": UI.atualizar_categoria,
            "8": UI.excluir_categoria,
            "9": lambda: UI.listar(ProdutoDAO, "Produtos"),
            "10": UI.inserir_produto,
            "11": UI.atualizar_produto,
            "12": UI.excluir_produto
        }

        while True:
            opcao = UI.Menu()
            if opcao == "0":
                print("Aplicação finalizada.")
                break

            operacao = operacoes.get(opcao)
            if operacao is None:
                print("Opção inválida.")
                continue

            try:
                operacao()
            except ValueError as erro:
                print(f"Erro: {erro}")
            except OSError as erro:
                print(f"Erro ao acessar arquivo: {erro}")


if __name__ == "__main__":
    UI.Main()
