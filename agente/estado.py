class Estado:
    def __init__(self):
        self.tipo_aplicacion = None
        self.arquitectura = None
        self.stack = []

        self.rendimiento = None
        self.experiencia = None
        self.restricciones = []

        self.tiempo = None
        self.escalabilidad = None
        self.tamanio_equipo = None
        self.complejidad = None

        self.posibles_arquitecturas = []
        self.prioridad = None
        self.validado = False