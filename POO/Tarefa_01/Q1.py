class Viagem:
    def __init__(self, destino, distancia, litros):
        self.__destino = ""
        self.__distancia = 0
        self.__litros = 0

        self.set_destino(destino)
        self.set_distancia(distancia)
        self.set_litros(litros)
        
    def get_destino(self):
        return self.__destino
    
    def set_destino(self, destino):
        if len(destino) > 0:
            self.__destino = destino
            
    def __str__(self):
        return "Destino: " + self.__destino + "\nDistância: " + str(self.__distancia) + "km\nLitros: " + str(self.__litros)

    def get_distancia(self):
        return self.__distancia
    
    def set_distancia(self, distancia):
        if distancia > 0:
            self.__distancia = distancia
    
    def get_litros(self):
        return self.__litros
    
    def set_litros(self, litros):
        if litros > 0:
            self.__litros = litros        

    def consumo(self):
        if self.__distancia > 0 and self.__litros > 0:
            return self.__distancia / self.__litros
        else:
            return "ERRO: Valor indefinido para consumo"
        
        
class ViagemUI:
    
    @staticmethod
    def Menu():
        print("1 - Calcular")
        print("2 - Fim")
        
        opcao_usuario = int(input())
        
        return opcao_usuario
    
    @staticmethod
    def Main():
        opcao = ViagemUI.Menu()
        
        while opcao != 2:
            
            if opcao == 1:
                ViagemUI.Calculo()
                
            opcao = ViagemUI.Menu()
        
    @staticmethod
    def Calculo():
        destino = input("Destino: ")
        distancia = float(input("Distancia: "))
        litros = float(input("Litros: "))
        
        viagem1 = Viagem(destino, distancia, litros)
        
        print(viagem1)
        print(viagem1.consumo())
        
ViagemUI.Main()