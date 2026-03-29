# =========================
# CONDICIONES
# =========================

def es_web_startup_rapida(e):
    return (
        e.get("tipo_aplicacion") == "web" and
        e.get("experiencia") == "principiante"
    )


def es_web_alto_rendimiento(e):
    return (
        e.get("tipo_aplicacion") == "web" and
        e.get("rendimiento") == "alto"
    )


def es_web_escalable(e):
    return (
        e.get("tipo_aplicacion") == "web" and
        e.get("escalabilidad") == "alta"
    )


def es_movil_cross_platform(e):
    return (
        e.get("tipo_aplicacion") == "movil" and
        e.get("equipo_pequeno") == True
    )


def es_movil_nativo(e):
    return (
        e.get("tipo_aplicacion") == "movil" and
        e.get("rendimiento") == "alto"
    )


def es_bajo_presupuesto(e):
    return "presupuesto_limitado" in e.get("restricciones", [])


def es_prototipo(e):
    return e.get("tiempo") == "corto"


def es_sistema_empresarial(e):
    return (
        e.get("complejidad") == "alta" and
        e.get("escalabilidad") == "alta"
    )


# =========================
# BASE DE REGLAS
# =========================

reglas = [
    {
        "nombre": "startup_rapida",
        "condicion": es_web_startup_rapida,
        "accion": "Next.js + Firebase + Vercel"
    },
    {
        "nombre": "web_alto_rendimiento",
        "condicion": es_web_alto_rendimiento,
        "accion": "React + Node.js (Express/Fastify) + PostgreSQL"
    },
    {
        "nombre": "web_escalable",
        "condicion": es_web_escalable,
        "accion": "Next.js + Node.js + PostgreSQL + Docker + Kubernetes"
    },
    {
        "nombre": "movil_cross_platform",
        "condicion": es_movil_cross_platform,
        "accion": "Flutter + Firebase"
    },
    {
        "nombre": "movil_nativo",
        "condicion": es_movil_nativo,
        "accion": "Kotlin (Android) + Swift (iOS)"
    },
    {
        "nombre": "bajo_presupuesto",
        "condicion": es_bajo_presupuesto,
        "accion": "Django + PostgreSQL + Railway/Render"
    },
    {
        "nombre": "prototipo",
        "condicion": es_prototipo,
        "accion": "Flask + SQLite o Firebase"
    },
    {
        "nombre": "sistema_empresarial",
        "condicion": es_sistema_empresarial,
        "accion": "Spring Boot + PostgreSQL + Docker + Microservicios"
    },
]