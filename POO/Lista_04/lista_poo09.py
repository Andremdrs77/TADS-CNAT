import json
import streamlit as st
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
    def _caminho_arquivo(cls):
        return Path(__file__).resolve().parent / cls.arquivo

    @classmethod
    def Abrir(cls):
        caminho = cls._caminho_arquivo()
        if not caminho.exists():
            cls.objetos = []
            return
        try:
            with caminho.open("r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
            if not isinstance(dados, list):
                raise ValueError(f"{caminho.name} deve conter uma lista JSON.")
            cls.objetos = [cls.classe.from_json(item) for item in dados]
        except (json.JSONDecodeError, TypeError, KeyError) as erro:
            raise ValueError(f"Não foi possível ler {caminho.name}: {erro}")

    @classmethod
    def Salvar(cls):
        caminho = cls._caminho_arquivo()
        with caminho.open("w", encoding="utf-8") as arquivo:
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



class ManterClienteUI:
    @staticmethod
    def Main():
        st.title("Manter cadastro de clientes")
        operacao = st.radio("Operação", ["Listar", "Inserir", "Atualizar", "Excluir"],
                            horizontal=True)
        clientes = Service.cliente_listar()

        if operacao == "Listar":
            if clientes:
                st.dataframe([{"ID": c.get_id(), "Nome": c.get_nome(),
                               "E-mail": c.get_email(), "Telefone": c.get_fone()}
                              for c in clientes], use_container_width=True,
                             hide_index=True)
            else:
                st.info("Nenhum cliente cadastrado.")

        elif operacao == "Inserir":
            with st.form("cliente_novo"):
                nome = st.text_input("Nome")
                email = st.text_input("E-mail")
                fone = st.text_input("Telefone")
                enviar = st.form_submit_button("Cadastrar")
            if enviar:
                if not all((nome.strip(), email.strip(), fone.strip())):
                    st.error("Preencha todos os campos.")
                else:
                    cliente = Service.cliente_inserir(nome.strip(), email.strip(), fone.strip())
                    st.success(f"Cliente cadastrado. ID: {cliente.get_id()}")

        elif operacao == "Atualizar":
            if not clientes:
                st.info("Nenhum cliente para atualizar.")
                return
            id_cliente = st.selectbox("Cliente", [c.get_id() for c in clientes])
            atual = Service.cliente_listar_id(id_cliente)
            with st.form("cliente_editar"):
                nome = st.text_input("Nome", atual.get_nome())
                email = st.text_input("E-mail", atual.get_email())
                fone = st.text_input("Telefone", atual.get_fone())
                enviar = st.form_submit_button("Salvar alterações")
            if enviar:
                if not all((nome.strip(), email.strip(), fone.strip())):
                    st.error("Preencha todos os campos.")
                else:
                    Service.cliente_atualizar(id_cliente, nome.strip(), email.strip(), fone.strip())
                    st.success("Cliente atualizado.")

        else:
            if not clientes:
                st.info("Nenhum cliente para excluir.")
                return
            opcoes = {f"{c.get_id()} - {c.get_nome()}": c.get_id() for c in clientes}
            escolha = st.selectbox("Cliente", list(opcoes))
            if st.button("Excluir cliente", type="primary"):
                Service.cliente_excluir(opcoes[escolha])
                st.success("Cliente excluído.")


class ManterCategoriaUI:
    @staticmethod
    def Main():
        st.title("Manter cadastro de categorias")
        operacao = st.radio("Operação", ["Listar", "Inserir", "Atualizar", "Excluir"],
                            horizontal=True)
        categorias = Service.categoria_listar()

        if operacao == "Listar":
            if categorias:
                st.dataframe([{"ID": c.get_id(), "Descrição": c.get_descricao()}
                              for c in categorias], use_container_width=True,
                             hide_index=True)
            else:
                st.info("Nenhuma categoria cadastrada.")

        elif operacao == "Inserir":
            with st.form("categoria_nova"):
                descricao = st.text_input("Descrição")
                enviar = st.form_submit_button("Cadastrar")
            if enviar:
                if not descricao.strip():
                    st.error("Informe a descrição.")
                else:
                    categoria = Service.categoria_inserir(descricao.strip())
                    st.success(f"Categoria cadastrada. ID: {categoria.get_id()}")

        elif operacao == "Atualizar":
            if not categorias:
                st.info("Nenhuma categoria para atualizar.")
                return
            id_categoria = st.selectbox("Categoria", [c.get_id() for c in categorias])
            atual = Service.categoria_listar_id(id_categoria)
            with st.form("categoria_editar"):
                descricao = st.text_input("Descrição", atual.get_descricao())
                enviar = st.form_submit_button("Salvar alterações")
            if enviar:
                if not descricao.strip():
                    st.error("Informe a descrição.")
                else:
                    Service.categoria_atualizar(id_categoria, descricao.strip())
                    st.success("Categoria atualizada.")

        else:
            if not categorias:
                st.info("Nenhuma categoria para excluir.")
                return
            opcoes = {f"{c.get_id()} - {c.get_descricao()}": c.get_id()
                      for c in categorias}
            escolha = st.selectbox("Categoria", list(opcoes))
            if st.button("Excluir categoria", type="primary"):
                try:
                    Service.categoria_excluir(opcoes[escolha])
                    st.success("Categoria excluída.")
                except ValueError as erro:
                    st.error(str(erro))


class ManterProdutoUI:
    @staticmethod
    def Main():
        st.title("Manter cadastro de produtos")
        operacao = st.radio("Operação", ["Listar", "Inserir", "Atualizar", "Excluir"],
                            horizontal=True)
        produtos = Service.produto_listar()
        categorias = Service.categoria_listar()
        nomes_categorias = {c.get_id(): c.get_descricao() for c in categorias}

        if operacao == "Listar":
            if produtos:
                st.dataframe([
                    {"ID": p.get_id(), "Descrição": p.get_descricao(),
                     "Preço": p.get_preco(), "Estoque": p.get_estoque(),
                     "Categoria": nomes_categorias.get(p.get_id_categoria(),
                                                       f"ID {p.get_id_categoria()}")}
                    for p in produtos
                ], use_container_width=True, hide_index=True)
            else:
                st.info("Nenhum produto cadastrado.")

        elif operacao == "Inserir":
            if not categorias:
                st.warning("Cadastre uma categoria antes de inserir produtos.")
                return
            with st.form("produto_novo"):
                descricao = st.text_input("Descrição")
                preco = st.number_input("Preço (R$)", min_value=0.0, step=0.5,
                                        format="%.2f")
                estoque = st.number_input("Estoque", min_value=0, step=1)
                id_categoria = st.selectbox("Categoria", list(nomes_categorias),
                                            format_func=lambda x: nomes_categorias[x])
                enviar = st.form_submit_button("Cadastrar")
            if enviar:
                if not descricao.strip():
                    st.error("Informe a descrição.")
                else:
                    produto = Service.produto_inserir(descricao.strip(), preco,
                                                      int(estoque), id_categoria)
                    st.success(f"Produto cadastrado. ID: {produto.get_id()}")

        elif operacao == "Atualizar":
            if not produtos:
                st.info("Nenhum produto para atualizar.")
                return
            id_produto = st.selectbox("Produto", [p.get_id() for p in produtos])
            atual = Service.produto_listar_id(id_produto)
            if not categorias:
                st.warning("Cadastre uma categoria antes de atualizar produtos.")
                return
            ids_categoria = list(nomes_categorias)
            indice = (ids_categoria.index(atual.get_id_categoria())
                      if atual.get_id_categoria() in ids_categoria else 0)
            with st.form("produto_editar"):
                descricao = st.text_input("Descrição", atual.get_descricao())
                preco = st.number_input("Preço (R$)", min_value=0.0,
                                        value=float(atual.get_preco()),
                                        step=0.5, format="%.2f")
                estoque = st.number_input("Estoque", min_value=0,
                                          value=int(atual.get_estoque()), step=1)
                id_categoria = st.selectbox("Categoria", ids_categoria, index=indice,
                                            format_func=lambda x: nomes_categorias[x])
                enviar = st.form_submit_button("Salvar alterações")
            if enviar:
                if not descricao.strip():
                    st.error("Informe a descrição.")
                else:
                    Service.produto_atualizar(id_produto, descricao.strip(),
                                              preco, int(estoque), id_categoria)
                    st.success("Produto atualizado.")

        else:
            if not produtos:
                st.info("Nenhum produto para excluir.")
                return
            opcoes = {f"{p.get_id()} - {p.get_descricao()}": p.get_id()
                      for p in produtos}
            escolha = st.selectbox("Produto", list(opcoes))
            if st.button("Excluir produto", type="primary"):
                Service.produto_excluir(opcoes[escolha])
                st.success("Produto excluído.")


class ReajustarProdutoUI:
    @staticmethod
    def Main():
        st.title("Reajustar preço dos produtos")
        st.write("Percentual positivo aumenta os preços; percentual negativo aplica promoção.")
        with st.form("reajuste"):
            percentual = st.number_input("Percentual (%)", value=0.0,
                                         step=1.0, format="%.2f")
            enviar = st.form_submit_button("Aplicar reajuste")
        if enviar:
            produtos = Service.produto_listar()
            if not produtos:
                st.warning("Não existem produtos cadastrados.")
            elif percentual <= -100:
                st.error("O percentual não pode ser igual ou inferior a -100%.")
            else:
                Service.produto_reajustar(percentual)
                st.success(f"Reajuste de {percentual:.2f}% aplicado.")
                st.dataframe([
                    {"ID": p.get_id(), "Produto": p.get_descricao(),
                     "Novo preço": p.get_preco()}
                    for p in Service.produto_listar()
                ], use_container_width=True, hide_index=True)


class IndexUI:
    @staticmethod
    def Main():
        st.set_page_config(page_title="Comércio Eletrônico",
                           page_icon="🛒", layout="wide")
        st.sidebar.title("Comércio Eletrônico")
        pagina = st.sidebar.selectbox(
            "Selecione a página",
            ["Início", "Clientes", "Categorias", "Produtos", "Reajustar preços"]
        )

        if pagina == "Início":
            st.title("Sistema de Comércio Eletrônico")
            st.subheader("Área administrativa")
            c1, c2, c3 = st.columns(3)
            c1.metric("Clientes", len(Service.cliente_listar()))
            c2.metric("Categorias", len(Service.categoria_listar()))
            c3.metric("Produtos", len(Service.produto_listar()))
            st.info("Escolha uma página no menu lateral para começar.")
        elif pagina == "Clientes":
            ManterClienteUI.Main()
        elif pagina == "Categorias":
            ManterCategoriaUI.Main()
        elif pagina == "Produtos":
            ManterProdutoUI.Main()
        elif pagina == "Reajustar preços":
            ReajustarProdutoUI.Main()


for _dao in (ClienteDAO, CategoriaDAO, ProdutoDAO, VendaDAO, VendaItemDAO):
    _dao.Abrir()

IndexUI.Main()
