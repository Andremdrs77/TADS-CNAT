class Treino:
    def __init__(self, id, data, distancia, tempo):
        self.__id = 0
        self.__data = ""
        self.__distancia = 0
        self.__tempo = 0

        self.set_id(id)
        self.set_data(data)
        self.set_distancia(distancia)
        self.set_tempo(tempo)

    def get_id(self):
        return self.__id

    def set_id(self, id):
        if id > 0:
            self.__id = id

    def get_data(self):
        return self.__data

    def set_data(self, data):
        if len(data) > 0:
            self.__data = data

    def get_distancia(self):
        return self.__distancia

    def set_distancia(self, distancia):
        if distancia > 0:
            self.__distancia = distancia

    def get_tempo(self):
        return self.__tempo

    def set_tempo(self, tempo):
        if tempo > 0:
            self.__tempo = tempo

    def pace(self):
        if self.__distancia > 0 and self.__tempo > 0:
            return self.__tempo / self.__distancia
        else:
            return 0

    def __str__(self):
        pace = self.pace()
        minutos = int(pace)
        segundos = int((pace - minutos) * 60)

        return "Id: " + str(self.__id) + \
               "\nData: " + self.__data + \
               "\nDistância: " + str(self.__distancia) + " km" + \
               "\nTempo: " + str(self.__tempo) + " minutos" + \
               "\nPace: " + str(minutos) + ":" + str(segundos).zfill(2) + " min/km"


class TreinoUI:
    lista = []

    @staticmethod
    def Menu():
        print("1 - Inserir")
        print("2 - Listar")
        print("3 - Listar por Id")
        print("4 - Atualizar")
        print("5 - Excluir")
        print("6 - Mais rápido")
        print("7 - Fim")

        opcao_usuario = int(input())

        return opcao_usuario

    @staticmethod
    def Main():
        opcao = TreinoUI.Menu()

        while opcao != 7:
            if opcao == 1:
                TreinoUI.Inserir()
            if opcao == 2:
                TreinoUI.Listar()
            if opcao == 3:
                TreinoUI.Listar_Id()
            if opcao == 4:
                TreinoUI.Atualizar()
            if opcao == 5:
                TreinoUI.Excluir()
            if opcao == 6:
                TreinoUI.MaisRapido()
                
            opcao = TreinoUI.Menu()

    @staticmethod
    def Inserir():
        id = int(input("Id: "))
        data = input("Data: ")
        distancia = float(input("Distância: "))
        tempo = float(input("Tempo em minutos: "))

        treino = Treino(id, data, distancia, tempo)

        TreinoUI.lista.append(treino)

    @staticmethod
    def Listar():
        for treino in TreinoUI.lista:
            print(treino)
            print()

    @staticmethod
    def Listar_Id():
        id = int(input("Id: "))

        for treino in TreinoUI.lista:
            if treino.get_id() == id:
                print(treino)
                return

        print("Treino não encontrado")

    @staticmethod
    def Atualizar():
        id = int(input("Id do treino: "))

        for treino in TreinoUI.lista:
            if treino.get_id() == id:
                data = input("Data: ")
                distancia = float(input("Distância: "))
                tempo = float(input("Tempo em minutos: "))

                treino.set_data(data)
                treino.set_distancia(distancia)
                treino.set_tempo(tempo)

                return

        print("Treino não encontrado")

    @staticmethod
    def Excluir():
        id = int(input("Id do treino: "))

        for treino in TreinoUI.lista:
            if treino.get_id() == id:
                TreinoUI.lista.remove(treino)
                return

        print("Treino não encontrado")

    @staticmethod
    def MaisRapido():
        if len(TreinoUI.lista) == 0:
            print("Não existem treinos")
            return

        treino_mais_rapido = TreinoUI.lista[0]

        for treino in TreinoUI.lista:
            if treino.pace() < treino_mais_rapido.pace():
                treino_mais_rapido = treino

        print(treino_mais_rapido)


TreinoUI.Main()