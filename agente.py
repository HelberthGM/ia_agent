class Agente:

    def __init__(self, reglas):
        self.reglas = reglas
     

    def interpretar(self, percepcion):
        percepcion = percepcion.lower()

        estado = {
            "tipo_aplicacion": None,
            "rendimiento": None,
            "experiencia": None,
            "restricciones": []
        }

        # Tipo de aplicación
        if "web" in percepcion:
            estado["tipo_aplicacion"] = "web"
        elif "movil" in percepcion:
            estado["tipo_aplicacion"] = "movil"
    
        # Rendimiento
        if "alto rendimiento" in percepcion:
            estado["rendimiento"] = "alto"
    
        # Experiencia
        if "principiante" in percepcion:
            estado["experiencia"] = "principiante"
    
        # Restricciones
        if "poco presupuesto" in percepcion:
            estado["restricciones"].append("presupuesto_limitado")
        return estado

    def decidir(self, estado):
        for regla in self.reglas:
            if regla["condicion"](estado):
                 return f"Recomendación: {regla['accion']}"
        return "No tengo suficiente información"

 