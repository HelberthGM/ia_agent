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

    def interpretar(self, percepcion: str) -> dict:

        texto = percepcion.lower()
        percepcion_dict = {}

        for categoria, valores in PALABRAS_CLAVE.items():
            for valor, palabras in valores.items():
                if any(p in texto for p in palabras):
                    percepcion_dict[categoria] = valor

        restricciones = []

        if "poco presupuesto" in texto:
            restricciones.append("presupuesto_limitado")

        elif "mucho presupuesto" in texto:
            restricciones.append("presupuesto_amplio")

        if restricciones:
            percepcion_dict["restricciones"] = restricciones

        return percepcion_dict

    def decidir(self, estado):

        if not estado.tipo_aplicacion:
            return "pedir_tipo"

        if not estado.stack:
            return "buscar_solucion"

        if not estado.validado:
            return "validar"

        return "finalizado"

    def actuar(self, entrada):

        percepcion = self.interpretar(entrada)

        self.actualizar_estado(percepcion)

        accion = self.decidir(self.estado)

        if accion == "buscar_solucion":
            self.inferir()

        if accion == "validar":
            self.validar()

        return self.estado

    def actualizar_estado(self, percepcion_dict):

        for clave, valor in percepcion_dict.items():

            if clave == "restricciones":

                for r in valor:
                    if r not in self.estado.restricciones:
                        self.estado.restricciones.append(r)

            else:
                setattr(self.estado, clave, valor)

        # Modelo interno

        if self.estado.tipo_aplicacion == "web":
            self.estado.posibles_arquitecturas = [
                "SPA",
                "SSR",
                "FullStack"
            ]

        elif self.estado.tipo_aplicacion == "movil":
            self.estado.posibles_arquitecturas = [
                "Nativa",
                "Hibrida",
                "CrossPlatform"
            ]

        # OBJETIVO DEL AGENTE

        if self.estado.escalabilidad == "alta":
            self.estado.objetivo = "maximizar_escalabilidad"

        elif self.estado.tiempo == "corto":
            self.estado.objetivo = "minimizar_tiempo"

        elif self.estado.tamanio_equipo == "pequeno":
            self.estado.objetivo = "facilidad_mantenimiento"

        else:
            self.estado.objetivo = "balanceado"

        return self.estado

    def validar(self):

        for tech_name in self.estado.stack:

            tech = TECNOLOGIAS.get(tech_name)

            if tech is None:
                continue

            for incompatible in tech.incompatible_con:

                if incompatible in self.estado.stack:

                    raise Exception(
                        f"{tech_name} es incompatible con {incompatible}"
                    )

            for req in tech.requiere:

                if req not in self.estado.stack:

                    print(
                        f"⚠ {tech_name} requiere {req}"
                    )

        self.estado.validado = True

    def es_meta(self, score):

        if self.estado.objetivo == "maximizar_escalabilidad":
            return score >= 6

        elif self.estado.objetivo == "minimizar_tiempo":
            return score >= 5

        elif self.estado.objetivo == "facilidad_mantenimiento":
            return score >= 5

        return score >= 4

    def inferir(self):

        stacks = self.generar_stacks(self.estado)

        stacks_validos = []

        for stack in stacks:

            try:

                self.estado.stack = stack
                self.estado.validado = False

                self.validar()

                stacks_validos.append(stack)

            except:
                continue

        mejor_stack = None
        mejor_score = -1

        for stack in stacks_validos:

            score = self.evaluar_stack(
                stack,
                self.estado
            )

            if score > mejor_score:

                mejor_score = score
                mejor_stack = stack

            # Si ya cumple la meta podemos detenernos
            if self.es_meta(score):

                mejor_stack = stack
                break

        if mejor_stack:

            self.estado.stack = mejor_stack
            self.estado.validado = True

        else:

            self.estado.stack = [
                "React",
                "Node.js",
                "Firebase"
            ]

    def evaluar_stack(self, stack, estado):

        score = 0

        techs = [TECNOLOGIAS[t] for t in stack]

        if estado.escalabilidad == "alta":

            if any(
                t.nombre == "Spring Boot"
                for t in techs
            ):
                score += 3

            if any(
                t.nombre == "PostgreSQL"
                for t in techs
            ):
                score += 3

        if estado.tiempo == "corto":

            if any(
                t.nombre == "Firebase"
                for t in techs
            ):
                score += 2

            if any(
                t.nombre == "React"
                for t in techs
            ):
                score += 2

        if estado.tamanio_equipo == "pequeno":

            if any(
                t.nombre == "Firebase"
                for t in techs
            ):
                score += 2

            if any(
                t.nombre == "Node.js"
                for t in techs
            ):
                score += 1

        if "presupuesto_limitado" in estado.restricciones:

            if any(
                t.nombre == "PostgreSQL"
                for t in techs
            ):
                score -= 1

        return score

    def generar_stacks(self, estado):

        frontends = []
        backends = []
        dbs = []

        for tech in TECNOLOGIAS.values():

            if tech.tipo == "frontend":
                frontends.append(tech.nombre)

            elif tech.tipo == "backend":
                backends.append(tech.nombre)

            elif tech.tipo == "database":
                dbs.append(tech.nombre)

        stacks = []

        for f in frontends:
            for b in backends:
                for d in dbs:

                    stacks.append([f, b, d])

        return stacks

    def mostrar_recomendacion(self):

        if not self.estado.stack:
            return "No hay recomendación disponible."

        return (
            f"\nObjetivo: {self.estado.objetivo}\n"
            f"Stack: {' + '.join(self.estado.stack)}\n"
            f"Validado: {self.estado.validado}\n"
        )