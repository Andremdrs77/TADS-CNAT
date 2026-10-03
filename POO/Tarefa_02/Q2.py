from datetime import datetime, timedelta


class PlayList:
    def __init__(self, id, nome, descricao):
        self.__id = 0
        self.__nome = ""
        self.__descricao = ""

        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)

    def get_id(self):
        return self.__id

    def set_id(self, id):
        if id > 0:
            self.__id = id

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if len(nome) > 0:
            self.__nome = nome

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        if len(descricao) > 0:
            self.__descricao = descricao

    def tempo_total(self, itens, musicas):
        tempo = timedelta()

        for item in itens:
            if item.get_id_playlist() == self.__id:
                for musica in musicas:
                    if musica.get_id() == item.get_id_musica():
                        tempo += musica.get_duracao()

        return tempo

    def __str__(self):
        return "Id: " + str(self.__id) + "\nNome: " + self.__nome + "\nDescrição: " + self.__descricao


class Musica:
    def __init__(self, id, titulo, artista, album, duracao):
        self.__id = 0
        self.__titulo = ""
        self.__artista = ""
        self.__album = ""
        self.__duracao = timedelta()

        self.set_id(id)
        self.set_titulo(titulo)
        self.set_artista(artista)
        self.set_album(album)
        self.set_duracao(duracao)

    def get_id(self):
        return self.__id

    def set_id(self, id):
        if id > 0:
            self.__id = id

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        if len(titulo) > 0:
            self.__titulo = titulo

    def get_artista(self):
        return self.__artista

    def set_artista(self, artista):
        if len(artista) > 0:
            self.__artista = artista

    def get_album(self):
        return self.__album

    def set_album(self, album):
        if len(album) > 0:
            self.__album = album

    def get_duracao(self):
        return self.__duracao

    def set_duracao(self, duracao):
        if duracao.total_seconds() > 0:
            self.__duracao = duracao

    def __str__(self):
        return "Id: " + str(self.__id) + \
               "\nTítulo: " + self.__titulo + \
               "\nArtista: " + self.__artista + \
               "\nÁlbum: " + self.__album + \
               "\nDuração: " + str(self.__duracao)


class PlayListItem:
    def __init__(self, id, id_playlist, id_musica, data_inclusao, sequencia):
        self.__id = 0
        self.__id_playlist = 0
        self.__id_musica = 0
        self.__data_inclusao = ""
        self.__sequencia = 0

        self.set_id(id)
        self.set_id_playlist(id_playlist)
        self.set_id_musica(id_musica)
        self.set_data_inclusao(data_inclusao)
        self.set_sequencia(sequencia)

    def get_id(self):
        return self.__id

    def set_id(self, id):
        if id > 0:
            self.__id = id

    def get_id_playlist(self):
        return self.__id_playlist

    def set_id_playlist(self, id_playlist):
        if id_playlist > 0:
            self.__id_playlist = id_playlist

    def get_id_musica(self):
        return self.__id_musica

    def set_id_musica(self, id_musica):
        if id_musica > 0:
            self.__id_musica = id_musica

    def get_data_inclusao(self):
        return self.__data_inclusao

    def set_data_inclusao(self, data_inclusao):
        if len(data_inclusao) > 0:
            self.__data_inclusao = data_inclusao

    def get_sequencia(self):
        return self.__sequencia

    def set_sequencia(self, sequencia):
        if sequencia > 0:
            self.__sequencia = sequencia

    def __str__(self):
        return "Id: " + str(self.__id) + \
               "\nId Playlist: " + str(self.__id_playlist) + \
               "\nId Música: " + str(self.__id_musica) + \
               "\nData de inclusão: " + self.__data_inclusao + \
               "\nSequência: " + str(self.__sequencia)


class UI:
    playlists = []
    musicas = []
    itens = []

    @staticmethod
    def Menu():
        print("1 - Inserir Playlist")
        print("2 - Listar Playlists")
        print("3 - Listar Playlist por Id")
        print("4 - Atualizar Playlist")
        print("5 - Excluir Playlist")
        print("6 - Tempo total da Playlist")
        print()
        print("7 - Inserir Música")
        print("8 - Listar Músicas")
        print("9 - Listar Música por Id")
        print("10 - Atualizar Música")
        print("11 - Excluir Música")
        print()
        print("12 - Inserir Item na Playlist")
        print("13 - Listar Itens")
        print("14 - Listar Itens de uma Playlist")
        print("15 - Atualizar Item")
        print("16 - Excluir Item")
        print()
        print("17 - Fim")

        opcao_usuario = int(input())

        return opcao_usuario

    @staticmethod
    def Main():
        opcao = UI.Menu()

        while opcao != 17:

            if opcao == 1:
                UI.Inserir_Playlist()

            if opcao == 2:
                UI.Listar_Playlists()

            if opcao == 3:
                UI.Listar_Playlist_Id()

            if opcao == 4:
                UI.Atualizar_Playlist()

            if opcao == 5:
                UI.Excluir_Playlist()

            if opcao == 6:
                UI.Tempo_Total_Playlist()

            if opcao == 7:
                UI.Inserir_Musica()

            if opcao == 8:
                UI.Listar_Musicas()

            if opcao == 9:
                UI.Listar_Musica_Id()

            if opcao == 10:
                UI.Atualizar_Musica()

            if opcao == 11:
                UI.Excluir_Musica()

            if opcao == 12:
                UI.Inserir_Item()

            if opcao == 13:
                UI.Listar_Itens()

            if opcao == 14:
                UI.Listar_Itens_Playlist()

            if opcao == 15:
                UI.Atualizar_Item()

            if opcao == 16:
                UI.Excluir_Item()

            opcao = UI.Menu()

    @staticmethod
    def Inserir_Playlist():
        id = int(input("Id: "))
        nome = input("Nome: ")
        descricao = input("Descrição: ")

        playlist = PlayList(id, nome, descricao)

        UI.playlists.append(playlist)

    @staticmethod
    def Listar_Playlists():
        for playlist in UI.playlists:
            print(playlist)
            print()

    @staticmethod
    def Listar_Playlist_Id():
        id = int(input("Id: "))

        for playlist in UI.playlists:
            if playlist.get_id() == id:
                print(playlist)
                return

        print("Playlist não encontrada")

    @staticmethod
    def Atualizar_Playlist():
        id = int(input("Id da playlist: "))

        for playlist in UI.playlists:
            if playlist.get_id() == id:
                nome = input("Nome: ")
                descricao = input("Descrição: ")

                playlist.set_nome(nome)
                playlist.set_descricao(descricao)

                return

        print("Playlist não encontrada")

    @staticmethod
    def Excluir_Playlist():
        id = int(input("Id da playlist: "))

        for playlist in UI.playlists:
            if playlist.get_id() == id:
                UI.playlists.remove(playlist)
                return

        print("Playlist não encontrada")

    @staticmethod
    def Tempo_Total_Playlist():
        id = int(input("Id da playlist: "))

        for playlist in UI.playlists:
            if playlist.get_id() == id:
                tempo = playlist.tempo_total(UI.itens, UI.musicas)

                print("Tempo total: " + str(tempo))

                return

        print("Playlist não encontrada")

    @staticmethod
    def Inserir_Musica():
        id = int(input("Id: "))
        titulo = input("Título: ")
        artista = input("Artista: ")
        album = input("Álbum: ")

        minutos = float(input("Duração em minutos: "))
        duracao = timedelta(minutes=minutos)

        musica = Musica(id, titulo, artista, album, duracao)

        UI.musicas.append(musica)

    @staticmethod
    def Listar_Musicas():
        for musica in UI.musicas:
            print(musica)
            print()

    @staticmethod
    def Listar_Musica_Id():
        id = int(input("Id: "))

        for musica in UI.musicas:
            if musica.get_id() == id:
                print(musica)
                return

        print("Música não encontrada")

    @staticmethod
    def Atualizar_Musica():
        id = int(input("Id da música: "))

        for musica in UI.musicas:
            if musica.get_id() == id:
                titulo = input("Título: ")
                artista = input("Artista: ")
                album = input("Álbum: ")

                minutos = float(input("Duração em minutos: "))
                duracao = timedelta(minutes=minutos)

                musica.set_titulo(titulo)
                musica.set_artista(artista)
                musica.set_album(album)
                musica.set_duracao(duracao)

                return

        print("Música não encontrada")

    @staticmethod
    def Excluir_Musica():
        id = int(input("Id da música: "))

        for musica in UI.musicas:
            if musica.get_id() == id:
                UI.musicas.remove(musica)
                return

        print("Música não encontrada")

    @staticmethod
    def Inserir_Item():
        id = int(input("Id: "))
        id_playlist = int(input("Id da playlist: "))
        id_musica = int(input("Id da música: "))
        data_inclusao = input("Data de inclusão: ")
        sequencia = int(input("Sequência: "))

        item = PlayListItem(
            id,
            id_playlist,
            id_musica,
            data_inclusao,
            sequencia
        )

        UI.itens.append(item)

    @staticmethod
    def Listar_Itens():
        for item in UI.itens:
            print(item)
            print()

    @staticmethod
    def Listar_Itens_Playlist():
        id_playlist = int(input("Id da playlist: "))

        for item in UI.itens:
            if item.get_id_playlist() == id_playlist:
                print(item)
                print()

    @staticmethod
    def Atualizar_Item():
        id = int(input("Id do item: "))

        for item in UI.itens:
            if item.get_id() == id:
                id_playlist = int(input("Id da playlist: "))
                id_musica = int(input("Id da música: "))
                data_inclusao = input("Data de inclusão: ")
                sequencia = int(input("Sequência: "))

                item.set_id_playlist(id_playlist)
                item.set_id_musica(id_musica)
                item.set_data_inclusao(data_inclusao)
                item.set_sequencia(sequencia)

                return

        print("Item não encontrado")

    @staticmethod
    def Excluir_Item():
        id = int(input("Id do item: "))

        for item in UI.itens:
            if item.get_id() == id:
                UI.itens.remove(item)
                return

        print("Item não encontrado")


UI.Main()