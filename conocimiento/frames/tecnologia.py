class Tecnologia:
    def __init__(self, nombre, tipo, compatible_con=None, requiere=None):
        self.nombre = nombre
        self.tipo = tipo
        self.compatible_con = compatible_con or []
        self.requiere = requiere or []