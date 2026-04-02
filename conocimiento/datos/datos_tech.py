from conocimiento.frames.tecnologia import Tecnologia

# ========================
# FRONTEND
# ========================

React = Tecnologia(
    "React",
    tipo="frontend",
    compatible_con=["Node.js", "Firebase"],
    requiere=["JavaScript"]
)

NextJS = Tecnologia(
    "Next.js",
    tipo="frontend",
    compatible_con=["Node.js"],
    requiere=["React"],
)

Flutter = Tecnologia(
    "Flutter",
    tipo="frontend",
    incompatible_con=["React"],
    requiere=["Dart"]
)

ReactNative = Tecnologia(
    "React Native",
    tipo="frontend",
    requiere=["JavaScript"]
)

# ========================
# BACKEND
# ========================

Node = Tecnologia(
    "Node.js",
    tipo="backend"
)

Spring = Tecnologia(
    "Spring Boot",
    tipo="backend",
    restricciones=["alto_consumo_memoria"]
)

Firebase = Tecnologia(
    "Firebase",
    tipo="backend",
    restricciones=["menos_control_backend"],
)

# ========================
# BASES DE DATOS
# ========================

PostgreSQL = Tecnologia(
    "PostgreSQL",
    tipo="database",
    restricciones=["configuracion_compleja"]
)

MongoDB = Tecnologia(
    "MongoDB",
    tipo="database",
    restricciones=["menos_consistencia"]
)

# ========================
# REGISTRO GLOBAL
# ========================

TECNOLOGIAS = {
    "React": React,
    "Next.js": NextJS,
    "Node.js": Node,
    "Spring Boot": Spring,
    "Firebase": Firebase,
    "Flutter": Flutter,
    "React Native": ReactNative,
    "PostgreSQL": PostgreSQL,
    "MongoDB": MongoDB,
}