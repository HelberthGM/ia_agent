from agente.agente import Agente

agente = Agente()

entrada = input("\nDescribe tu proyecto: ")
estado_agente= agente.actuar(entrada)
print(agente.mostrar_recomendacion())