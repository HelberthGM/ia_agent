# Agente Inteligente para Selección de Stack Tecnológico

## Agente Reactivo Basado en Modelos

El sistema implementado corresponde a un **agente reactivo basado en modelos**, siguiendo la clasificación presentada en el libro *Artificial Intelligence: A Modern Approach (Russell & Norvig)*.

A diferencia de un agente reactivo simple, este agente mantiene un **estado interno** que le permite representar información parcial del entorno y tomar decisiones más informadas.

---

### 1. Arquitectura del Agente

El agente está compuesto por los siguientes elementos principales:

- **Percepción (`interpretar`)**: procesa la entrada del usuario en lenguaje natural y extrae información relevante mediante palabras clave.
- **Estado interno (`Estado`)**: estructura que almacena características del problema, como:
  - tipo de aplicación (web, móvil)
  - requisitos de escalabilidad
  - restricciones (presupuesto, tiempo)
  - tamaño del equipo
- **Actualización del estado (`actualizar_estado`)**: integra la nueva información percibida con el estado previo, permitiendo mantener memoria entre interacciones.
- **Inferencia (`inferir`)**: utiliza reglas y conocimiento del dominio para determinar una arquitectura y un stack tecnológico adecuado.
- **Validación (`validar`)**: verifica compatibilidad entre tecnologías y consistencia del stack generado.

---

### 2. Modelo del Mundo

El agente utiliza un **modelo del mundo simplificado** representado mediante:

- Un conjunto de atributos en la clase `Estado`
- Un sistema de conocimiento basado en **frames (`Tecnologia`)**, donde cada tecnología incluye:
  - tipo (frontend, backend, base de datos)
  - dependencias (`requiere`)
  - compatibilidades e incompatibilidades
  - restricciones

Este modelo permite al agente razonar sobre combinaciones tecnológicas sin depender exclusivamente de reglas rígidas.

---

### 3. Funcionamiento

El flujo de operación del agente es el siguiente:

1. El usuario describe un proyecto en lenguaje natural.
2. El agente interpreta la entrada y genera una percepción estructurada.
3. Se actualiza el estado interno del agente.
4. Se realiza un proceso de inferencia para seleccionar:
   - arquitectura (SPA, SSR, etc.)
   - stack tecnológico
5. Se resuelven dependencias automáticamente.
6. Se valida la coherencia del resultado.
7. Se presenta una recomendación final.

---

### 4. Características del Enfoque

Este agente presenta las siguientes propiedades:

- **Memoria interna**: mantiene información acumulada del problema.
- **Razonamiento basado en conocimiento**: utiliza estructuras tipo frame para modelar tecnologías.
- **Reactividad**: responde directamente a las percepciones del usuario sin planificación compleja.
- **Extensibilidad**: permite agregar nuevas tecnologías sin modificar la lógica central.

---

### 5. Limitaciones

- La inferencia está basada en reglas heurísticas (uso de condicionales).
- No se realiza planificación ni optimización global.
- No utiliza aprendizaje automático ni modelos probabilísticos.

---

En conclusión, el agente desarrollado representa una implementación funcional de un **agente reactivo basado en modelos**, capaz de mantener contexto, razonar sobre información parcial y generar recomendaciones tecnológicas coherentes.

