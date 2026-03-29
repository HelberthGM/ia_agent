class Agente:

    def __init__(self, reglas):
        self.reglas = reglas
        self.historial = []  # para futuro (aprendizaje)

    def interpretar(self, percepcion):
        percepcion = percepcion.lower()

        estado = {
            "tipo_aplicacion": None,
            "rendimiento": None,
            "experiencia": None,
            "restricciones": []
        }

        if "web" in percepcion:
            estado["tipo_aplicacion"] = "web"
        elif "movil" in percepcion:
            estado["tipo_aplicacion"] = "movil"
    
        if "alto rendimiento" in percepcion:
            estado["rendimiento"] = "alto"
    
        if "principiante" in percepcion:
            estado["experiencia"] = "principiante"
   
        if "poco presupuesto" in percepcion:
            estado["restricciones"].append("presupuesto_limitado")
        
        if "rapido" in percepcion or "mvp" in percepcion:
            estado["tiempo"] = "corto"

        if "escalable" in percepcion or "muchos usuarios" in percepcion:
            estado["escalabilidad"] = "alta"

        if "equipo pequeño" in percepcion:
            estado["equipo_pequeno"] = True

        if "complejo" in percepcion or "empresarial" in percepcion:
            estado["complejidad"] = "alta"
        return estado

    def decidir(self, estado):
        for regla in self.reglas:
            if regla["condicion"](estado):
                 return f"Recomendación: {regla['accion']}"
        return "No tengo suficiente información"

    def actuar(self, percepcion):
        estado = self.interpretar(percepcion)
        accion = self.decidir(estado)

        self.historial.append((estado, accion))  # memoria simple

        return accion