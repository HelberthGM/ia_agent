# Agente Inteligente para Selección de Stack Tecnológico

### 📌 Acceso rápido a las versiones

Puedes explorar las diferentes implementaciones del agente directamente en sus respectivas ramas:

  * 🔗 **[Agente Reactivo Simple](https://github.com/HelberthGM/ia_agent/tree/agente_reactivo_simple)**: Implementación basada en reglas directas de condición-acción.
  * 🔗 **[Agente Reactivo Basado en Modelos](https://github.com/HelberthGM/ia_agent/tree/agente-reactivo-modelos)**: Versión que incorpora un estado interno para manejar entornos con visibilidad parcial.
  * 🔗 **[Agente Basado en Objetivos](https://github.com/HelberthGM/ia_agent/tree/agente_basado_objetivos)**: Implementación que utiliza búsqueda y planificación para alcanzar metas específicas.

-----

## 📖 Descripción

Este repositorio contiene el desarrollo de agentes inteligentes diseñados para operar en entornos simulados. El objetivo es comparar el desempeño de un agente que solo reacciona al presente frente a uno que mantiene memoria de sus acciones y del entorno.

## 🛠️ Requisitos

  * Python 3.10+
  * Entorno virtual (recomendado)
  * Dependencias listadas en `requirements.txt`

## 🚀 Ejecución

Para ejecutar el proyecto, primero clona el repositorio y muévete a la rama que desees probar:

1.  **Clonar el repositorio:**

    ```bash
    git clone https://github.com/HelberthGM/ia_agent.git
    cd ia_agent
    ```

2.  **Cambiar a una rama específica:**

    ```bash
    # Para el agente simple
    git checkout agente_reactivo_simple

    # O para el agente basado en modelos
    git checkout agente-reactivo-modelos
    ```

3.  **Instalar dependencias y correr:**

    ```bash
    pip install -r requirements.txt
    python main.py
    ```
-----
## Ejemplo de uso
Entrada:
"Aplicación web con alto rendimiento y bajo presupuesto"

Salida:
Recomendación: Usa React + Node.js + MongoDB
