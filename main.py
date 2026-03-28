from agente import Agente
from reglas import reglas

agente = Agente(reglas)

while True:
    entrada = input("\nDescribe tu proyecto: ")

    if entrada == "salir":
        break

    print(agente.actuar(entrada))