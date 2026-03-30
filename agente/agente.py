class Agente:

    def __init__(self, reglas):
        self.reglas = reglas
        # self.historial = []  # para futuro (aprendizaje)

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
        # Información incompleta
        if not estado.tipo_aplicacion:
            return "pedir_tipo"

        if not estado.arquitectura:
            return "pedir_arquitectura"

        # Aún no hay stack generado
        if not estado.stack:
            return "inferir_stack"

        # Hay stack pero no validado
        if not estado.validado:
            return "validar"

        # Estado final
        return "finalizado"

    def actuar(self, percepcion):
        estado = self.interpretar(percepcion)
        accion = self.decidir(estado)

        # self.historial.append((estado, accion))  # memoria simple

        return accion
    
    def actualizar_estado(estado, percepcion):
        if percepcion.get("tipo_aplicacion"):
            estado.tipo_aplicacion = percepcion["tipo_aplicacion"]

        if estado.tipo_aplicacion == "web":
            estado.posibles_arquitecturas = ["SPA", "SSR", "FullStack"]

        return estado
    