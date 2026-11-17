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



class Service:
    @staticmethod
    def _proximo_id(dao):
        objetos = dao.Listar()
        if not objetos:
            return 1
        return max(obj.get_id() for obj in objetos) + 1

    @staticmethod
    def cliente_inserir(nome, email, fone):
        id = Service._proximo_id(ClienteDAO)
        obj = Cliente(id, nome, email, fone)
        ClienteDAO.Inserir(obj)
        return obj

    @staticmethod
    def cliente_listar():
        return ClienteDAO.Listar()

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO.Listar_Id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        if ClienteDAO.Listar_Id(id) is None:
            return False
        obj = Cliente(id, nome, email, fone)
        return ClienteDAO.Atualizar(obj)

    @staticmethod
    def cliente_excluir(id):
        return ClienteDAO.Excluir(id)

    @staticmethod
    def categoria_inserir(descricao):
        id = Service._proximo_id(CategoriaDAO)
        obj = Categoria(id, descricao)
        CategoriaDAO.Inserir(obj)
        return obj

    @staticmethod
    def categoria_listar():
        return CategoriaDAO.Listar()

    @staticmethod
    def categoria_listar_id(id):
        return CategoriaDAO.Listar_Id(id)

    @staticmethod
    def categoria_atualizar(id, descricao):
        if CategoriaDAO.Listar_Id(id) is None:
            return False
        obj = Categoria(id, descricao)
        return CategoriaDAO.Atualizar(obj)

    @staticmethod
    def categoria_excluir(id):
        for produto in ProdutoDAO.Listar():
            if produto.get_id_categoria() == id:
                raise ValueError("Existem produtos vinculados a essa categoria.")
        return CategoriaDAO.Excluir(id)

    @staticmethod
    def produto_inserir(descricao, preco, estoque, idCategoria):
        if CategoriaDAO.Listar_Id(idCategoria) is None:
            raise ValueError("Categoria não encontrada.")
        id = Service._proximo_id(ProdutoDAO)
        obj = Produto(id, descricao, preco, estoque, idCategoria)
        ProdutoDAO.Inserir(obj)
        return obj

    @staticmethod
    def produto_listar():
        return ProdutoDAO.Listar()

    @staticmethod
    def produto_listar_id(id):
        return ProdutoDAO.Listar_Id(id)

    @staticmethod
    def produto_atualizar(id, descricao, preco, estoque, idCategoria):
        if ProdutoDAO.Listar_Id(id) is None:
            return False
        if CategoriaDAO.Listar_Id(idCategoria) is None:
            raise ValueError("Categoria não encontrada.")
        obj = Produto(id, descricao, preco, estoque, idCategoria)
        return ProdutoDAO.Atualizar(obj)

    @staticmethod
    def produto_excluir(id):
        return ProdutoDAO.Excluir(id)

    @staticmethod
    def produto_reajustar(percentual):
        for produto in ProdutoDAO.Listar():
            novo_preco = produto.get_preco() * (1 + percentual / 100)
            produto.set_preco(round(novo_preco, 2))
            ProdutoDAO.Atualizar(produto)



class UI:
    @staticmethod
    def menu():
        print("\n========== SISTEMA DE COMÉRCIO ELETRÔNICO ==========")
        print("1  - Inserir cliente")
        print("2  - Listar clientes")
        print("3  - Atualizar cliente")
        print("4  - Excluir cliente")
        print("5  - Inserir categoria")
        print("6  - Listar categorias")
        print("7  - Atualizar categoria")
        print("8  - Excluir categoria")
        print("9  - Inserir produto")
        print("10 - Listar produtos")
        print("11 - Atualizar produto")
        print("12 - Excluir produto")
        print("13 - Reajustar preço dos produtos")
        print("0  - Finalizar")
        return input("Escolha uma opção: ").strip()

    @staticmethod
    def _listar(objetos, nome):
        print(f"\n--- {nome} cadastrados ---")
        if not objetos:
            print("Nenhum registro cadastrado.")
            return
        for obj in objetos:
            print(obj)

    @staticmethod
    def cliente_inserir():
        print("\n--- Inserir cliente ---")
        nome = input("Nome: ").strip()
        email = input("E-mail: ").strip()
        fone = input("Telefone: ").strip()
        obj = Service.cliente_inserir(nome, email, fone)
        print(f"Cliente cadastrado. ID: {obj.get_id()}")

    @staticmethod
    def cliente_listar():
        UI._listar(Service.cliente_listar(), "Clientes")

    @staticmethod
    def cliente_atualizar():
        id = int(input("ID do cliente: "))
        atual = Service.cliente_listar_id(id)
        if atual is None:
            print("Cliente não encontrado.")
            return

        nome = input(f"Nome [{atual.get_nome()}]: ").strip()
        email = input(f"E-mail [{atual.get_email()}]: ").strip()
        fone = input(f"Telefone [{atual.get_fone()}]: ").strip()

        if not nome:
            nome = atual.get_nome()
        if not email:
            email = atual.get_email()
        if not fone:
            fone = atual.get_fone()

        Service.cliente_atualizar(id, nome, email, fone)
        print("Cliente atualizado.")

    @staticmethod
    def cliente_excluir():
        id = int(input("ID do cliente: "))
        if Service.cliente_excluir(id):
            print("Cliente excluído.")
        else:
            print("Cliente não encontrado.")

    @staticmethod
    def categoria_inserir():
        print("\n--- Inserir categoria ---")
        descricao = input("Descrição: ").strip()
        obj = Service.categoria_inserir(descricao)
        print(f"Categoria cadastrada. ID: {obj.get_id()}")

    @staticmethod
    def categoria_listar():
        UI._listar(Service.categoria_listar(), "Categorias")

    @staticmethod
    def categoria_atualizar():
        id = int(input("ID da categoria: "))
        atual = Service.categoria_listar_id(id)
        if atual is None:
            print("Categoria não encontrada.")
            return
        descricao = input(f"Descrição [{atual.get_descricao()}]: ").strip()
        if not descricao:
            descricao = atual.get_descricao()
        Service.categoria_atualizar(id, descricao)
        print("Categoria atualizada.")

    @staticmethod
    def categoria_excluir():
        id = int(input("ID da categoria: "))
        if Service.categoria_excluir(id):
            print("Categoria excluída.")
        else:
            print("Categoria não encontrada.")

    @staticmethod
    def produto_inserir():
        print("\n--- Inserir produto ---")
        if not Service.categoria_listar():
            print("Cadastre uma categoria antes de inserir produtos.")
            return
        descricao = input("Descrição: ").strip()
        preco = float(input("Preço: ").replace(",", "."))
        estoque = int(input("Estoque: "))
        idCategoria = int(input("ID da categoria: "))
        obj = Service.produto_inserir(descricao, preco, estoque, idCategoria)
        print(f"Produto cadastrado. ID: {obj.get_id()}")

    @staticmethod
    def produto_listar():
        UI._listar(Service.produto_listar(), "Produtos")

    @staticmethod
    def produto_atualizar():
        id = int(input("ID do produto: "))
        atual = Service.produto_listar_id(id)
        if atual is None:
            print("Produto não encontrado.")
            return

        descricao = input(f"Descrição [{atual.get_descricao()}]: ").strip()
        preco_txt = input(f"Preço [{atual.get_preco()}]: ").strip()
        estoque_txt = input(f"Estoque [{atual.get_estoque()}]: ").strip()
        categoria_txt = input(
            f"ID da categoria [{atual.get_id_categoria()}]: "
        ).strip()

        if not descricao:
            descricao = atual.get_descricao()
        preco = float(preco_txt.replace(",", ".")) if preco_txt else atual.get_preco()
        estoque = int(estoque_txt) if estoque_txt else atual.get_estoque()
        idCategoria = int(categoria_txt) if categoria_txt else atual.get_id_categoria()

        Service.produto_atualizar(id, descricao, preco, estoque, idCategoria)
        print("Produto atualizado.")

    @staticmethod
    def produto_excluir():
        id = int(input("ID do produto: "))
        if Service.produto_excluir(id):
            print("Produto excluído.")
        else:
            print("Produto não encontrado.")

    @staticmethod
    def produto_reajustar():
        percentual = float(
            input("Percentual (positivo para aumento, negativo para promoção): ")
            .replace(",", ".")
        )
        Service.produto_reajustar(percentual)
        print("Preços atualizados.")
        UI.produto_listar()

    @staticmethod
    def main():
        for dao in (ClienteDAO, CategoriaDAO, ProdutoDAO,
                    VendaDAO, VendaItemDAO):
            dao.Abrir()

        while True:
            opcao = UI.menu()

            try:
                if opcao == "1":
                    UI.cliente_inserir()
                elif opcao == "2":
                    UI.cliente_listar()
                elif opcao == "3":
                    UI.cliente_atualizar()
                elif opcao == "4":
                    UI.cliente_excluir()
                elif opcao == "5":
                    UI.categoria_inserir()
                elif opcao == "6":
                    UI.categoria_listar()
                elif opcao == "7":
                    UI.categoria_atualizar()
                elif opcao == "8":
                    UI.categoria_excluir()
                elif opcao == "9":
                    UI.produto_inserir()
                elif opcao == "10":
                    UI.produto_listar()
                elif opcao == "11":
                    UI.produto_atualizar()
                elif opcao == "12":
                    UI.produto_excluir()
                elif opcao == "13":
                    UI.produto_reajustar()
                elif opcao == "0":
                    print("Aplicação finalizada.")
                    break
                else:
                    print("Opção inválida.")
            except ValueError as erro:
                print(f"Erro: {erro}")
            except OSError as erro:
                print(f"Erro ao acessar os arquivos: {erro}")


if __name__ == "__main__":
    UI.main()
