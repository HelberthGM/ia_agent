class Tecnologia:
    def __init__(
        self,
        nombre,
        tipo,
        compatible_con=None,
        incompatible_con=None,
        requiere=None,
        restricciones=None
    ):
        self.nombre = nombre
        self.tipo = tipo
        self.compatible_con = compatible_con or []
        self.incompatible_con = incompatible_con or []
        self.requiere = requiere or []
        self.restricciones = restricciones or []