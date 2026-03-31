from conocimiento.frames.tecnologia import Tecnologia

React = Tecnologia(
    "React",
    tipo="frontend",
    compatible_con=["Node.js", "Firebase"],
    requiere=["JavaScript"]
)

Node = Tecnologia(
    "Node.js",
    tipo="backend"
)


Spring = Tecnologia(
    "Spring Boot",
    tipo="backend",
    restricciones=["alto_consumo_memoria"]
)

Flutter = Tecnologia(
    "Flutter",
    tipo="frontend",
    incompatible_con=["React"],
    requiere=["Dart"]
)

TECNOLOGIAS = {
    "React": React,
    "Node.js": Node,
    "Spring Boot": Spring,
    "Flutter": Flutter
}