# 🛡️ Motor Lógico de Detección de Anomalías (Mini-SIEM)

Este laboratorio es una demostración de **pensamiento computacional** aplicado a la ciberdefensa. El objetivo principal es construir la lógica central de un SIEM (Security Information and Event Management) utilizando exclusivamente estructuras de control nativas, sin depender de librerías externas.

## 🎯 Objetivo del Laboratorio

- Evaluar un diccionario de datos (simulando logs de red en bruto).
- Aplicar filtrado de amenazas mediante operadores lógicos compuestos (`and`).
- Aislar atacantes utilizando listas dinámicas y estructuras iterativas (`for` / `if-elif-else`).
- Priorizar la eficiencia del código mediante la evaluación de _Truthiness_ (`if lista:`).

## 🧠 Lógica de Detección Implementada

El script evalúa dos escenarios principales de ataque:

1.  **Exfiltración de Datos:** Detecta si el puerto 22 (SSH) está transfiriendo un volumen de bytes superior al umbral normal (>50,000 bytes).
2.  **Comunicaciones Maliciosas (C2):** Detecta conexiones a puertos históricamente asociados a _Reverse Shells_ o troyanos (Ej: Puerto 4444).

## 🚀 Cómo ejecutarlo

No requiere instalación de dependencias. Solo necesitas tener Python instalado.

```bash
python mini_siem_analisis.py
```
