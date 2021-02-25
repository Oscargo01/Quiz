from abc import ABC, abstractmethod

class Receiver:
    Bot = [1,2,3,4]
class Command:
    	@abstractmethod
    def ejecutar(self, receptor):
		pass
    def Enceder(Bot):
        print("El bot se esta encendiendo", Bot[1])
    def Apagar(Bot):
        print("El bot se esta apagando", Bot[2])
    def Hablar(Bot):
        print("El bot esta hablando", Bot[3])
    def Dormir(Bot):
        print("El bot esta comiendo", Bot[4])

comandos = {"E":encender, "A":apagar, "H":hablar, "D":dormir}

class Invoker:
    def Invocador(comando, bot):
        comando(bot)

def Comando_Solicitado():
    valor = input("Introduzca el comando que desee que el Bot realice "+str(list(comandos.keys())) )
    return if comandos[valor] if comandos.keys() else print("El comando no lo reconce el Bot")