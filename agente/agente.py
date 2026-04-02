from agente.estado import Estado
from conocimiento.datos.datos_tech import TECNOLOGIAS

PALABRAS_CLAVE = {
    "tipo_aplicacion": {
        "web": ["web", "pagina", "sitio"],
        "movil": ["movil", "app", "android", "ios"],
    },
    "experiencia": {
        "principiante": ["principiante", "novato"],
        "avanzado": ["avanzado", "experto"]
    },
    "rendimiento": {
        "alto": ["alto rendimiento", "alto desempeño"],
        "bajo": ["bajo rendimiento", "lento"]
    },
    "tiempo": {
        "corto": ["rapido", "mvp"],
        "largo": ["lento", "no es urgente"]
    },
    "escalabilidad": {
        "alta": ["escalable", "muchos usuarios"],
        "baja": ["no escalable", "pocos usuarios"]
    },
    "tamanio_equipo": {
        "pequeno": ["equipo pequeño", "pocos desarrolladores"],
        "grande": ["equipo grande", "muchos desarrolladores"]
    },
    "complejidad": {
        "alta": ["complejo", "empresarial"],
        "baja": ["simple", "pequeño proyecto"]
    }
}

class Agente:

    def __init__(self):
        self.estado = Estado()
        # self.historial = []  # para futuro (aprendizaje)

    def interpretar(self, percepcion: str) -> dict:
        texto = percepcion.lower()
    
        percepcion_dict = {}

        for categoria, valores in PALABRAS_CLAVE.items():
            for valor, palabras in valores.items():
                if any(p in texto for p in palabras):
                    percepcion_dict[categoria] = valor
    
        # Tipo de aplicación
        if "web" in texto:
            percepcion_dict["tipo_aplicacion"] = "web"
        elif "movil" in texto:
            percepcion_dict["tipo_aplicacion"] = "movil"
    
        # Rendimiento
        if "alto rendimiento" in texto or "alto desempeño" in texto:
            percepcion_dict["rendimiento"] = "alto"
    
        # Experiencia
        if "principiante" in texto:
            percepcion_dict["experiencia"] = "principiante"
    
        # Restricciones
        restricciones = []
        if "poco presupuesto" in texto:
            restricciones.append("presupuesto_limitado")
        elif "mucho presupuesto" in texto:
            restricciones.append("presupuesto_amplio")
    
        if restricciones:
            percepcion_dict["restricciones"] = restricciones
    
        # Tiempo
        if "rapido" in texto or "mvp" in texto:
            percepcion_dict["tiempo"] = "corto"
        elif "lento" in texto or "no es urgente" in texto:
            percepcion_dict["tiempo"] = "largo"
    
        # Escalabilidad
        if "escalable" in texto or "muchos usuarios" in texto:
            percepcion_dict["escalabilidad"] = "alta"
        elif "no escalable" in texto or "pocos usuarios" in texto:
            percepcion_dict["escalabilidad"] = "baja"
    
        # Equipo
        if "equipo pequeño" in texto:
            percepcion_dict["tamanio_equipo"] = "pequeno"
        elif "equipo grande" in texto:
            percepcion_dict["tamanio_equipo"] = "grande"
    
        # Complejidad
        if "complejo" in texto or "empresarial" in texto:
            percepcion_dict["complejidad"] = "alta"
        elif "simple" in texto or "pequeño proyecto" in texto:
            percepcion_dict["complejidad"] = "baja"

        return percepcion_dict

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

    def actuar(self, entrada):

        percepcion = self.interpretar(entrada)
    
        self.actualizar_estado(percepcion)
    
        accion = self.decidir(self.estado)
    
        # print("ANTES DE INFERIR:", self.estado.__dict__)
        self.inferir()
        # print("DESPUES DE INFERIR:", self.estado.__dict__)
    
        self.validar()
        
        return self.estado
    
    def actualizar_estado(self, percepcion_dict):

        for clave, valor in percepcion_dict.items():

            # Manejo de restricciones
            if clave == "restricciones":
                for r in valor:
                    if r not in self.estado.restricciones:
                        self.estado.restricciones.append(r)

            else:
                setattr(self.estado, clave, valor)

        # Inferencias básicas (modelo del mundo)

        if self.estado.tipo_aplicacion == "web":
            self.estado.posibles_arquitecturas = ["SPA", "SSR", "FullStack"]

        elif self.estado.tipo_aplicacion == "movil":
            self.estado.posibles_arquitecturas = ["Nativa", "Hibrida", "CrossPlatform"]

        # Inferencia basada en restricciones 
        if self.estado.tiempo == "corto":
            self.estado.prioridad = "rapidez"

        if self.estado.escalabilidad == "alta":
            self.estado.prioridad = "escalabilidad"

        #print("DEBUG estado:", self.estado.__dict__)
        return self.estado
    
    def validar(self):
        for tech_name in self.estado.stack:
            tech = TECNOLOGIAS.get(tech_name)

            if tech is None:
                print(f"⚠ Tecnología no registrada: {tech_name}")
                continue  
    
            # validar incompatibilidades
            for incompatible in tech.incompatible_con:
                if incompatible in self.estado.stack:
                    raise Exception(f"{tech_name} es incompatible con {incompatible}")
    
            # validar requerimientos
            for req in tech.requiere:
                if req not in self.estado.stack:
                    print(f"⚠ {tech_name} requiere {req} (resolviendo automáticamente)")

        self.estado.validado = True

    def inferir(self):

        # Defaults
        if self.estado.prioridad is None:
            self.estado.prioridad = "rapidez"

        if self.estado.tipo_aplicacion == "web":

            # Elegir arquitectura
            if self.estado.prioridad == "rapidez":
                self.estado.arquitectura = "SPA"

            elif self.estado.escalabilidad == "alta":
                self.estado.arquitectura = "SSR"

            # Generar stack coherente
            if self.estado.arquitectura == "SPA":
                self.estado.stack = ["React", "Node.js", "Firebase"]

            elif self.estado.arquitectura == "SSR":
                self.estado.stack = ["Next.js", "Node.js", "PostgreSQL"]

        elif self.estado.tipo_aplicacion == "movil":

            if self.estado.prioridad == "rapidez":
                self.estado.stack = ["Flutter"]

            elif self.estado.escalabilidad == "alta":
                self.estado.stack = ["React Native", "Node.js", "MongoDB"]
    
    def mostrar_recomendacion(self):
        if not self.estado.stack:
            print("⚠ No tengo suficiente información, usando valores por defecto")
        return (
            f"\n🚀 Recomendación:\n Arquitectura: {self.estado.arquitectura}\n Stack: {' + '.join(self.estado.stack)}\n Prioridad: {self.estado.prioridad}\n"
        )