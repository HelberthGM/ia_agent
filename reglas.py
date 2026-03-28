# reglas.py

def es_web_alto_rendimiento(e):
    return e["tipo"] == "web" and e["rendimiento"] == "alto"

def es_movil_principiante(e):
    return e["tipo"] == "movil" and e["experiencia"] == "principiante"


reglas = [
    {
        "nombre": "web_alto_rendimiento",
        "condicion": es_web_alto_rendimiento,
        "accion": "Usa React + Node.js + MongoDB"
    },
    {
        "nombre": "movil_principiante",
        "condicion": es_movil_principiante,
        "accion": "Usa Flutter + Firebase"
    },
    {
        "nombre": "web_alto_rendimiento",
        "condicion": es_web_alto_rendimiento,
        "accion": "React + Node.js + MongoDB"
    },
    {
        "nombre": "movil_principiante",
        "condicion": es_movil_principiante,
        "accion": "Usa Flutter + Firebase"
    }
]