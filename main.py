from agente import Agente
from reglas import reglas

agente = Agente(reglas)

entrada = input("\nDescribe tu proyecto: ")
print(agente.actuar(entrada))