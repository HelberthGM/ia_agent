from agente import estado
from agente.agente import Agente
from reglas import reglas

agente = Agente(reglas)

entrada = input("\nDescribe tu proyecto: ")
print(agente.actuar(entrada))
print(estado.__dict__)