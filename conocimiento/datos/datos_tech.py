from conocimiento.frames.tecnologia import Tecnologia

React = Tecnologia(
    "React",
    tipo="frontend",
    compatible_con=["Node.js"],
    requiere=["JavaScript"]
)

Node = Tecnologia(
    "Node.js",
    tipo="backend"
)

TECNOLOGIAS = {
    "React": React,
    "Node.js": Node
}