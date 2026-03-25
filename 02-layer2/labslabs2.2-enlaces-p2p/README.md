
# 🛡️ Lab 01: Enlace P2P Básico y Verificación de Conectividad (ICMP)

## 📋 Resumen Ejecutivo
**Objetivo:** Establecer una conexión física y lógica directa (Peer-to-Peer) entre dos terminales finales y verificar la comunicación bidireccional mediante el protocolo ICMP.
**Herramienta:** Cisco Packet Tracer 9.0
**Conceptos Clave:** Modelo OSI (Capa 1 y Capa 3), Direccionamiento IPv4 Estático, Cableado Cruzado, ICMP (Ping).

---

## 🗺️ Topología de Red
*(Insertar aquí la imagen `topologia.png` de cómo se ven las dos PCs conectadas en Packet Tracer)*
- **PC-A** conectada directamente a **PC-B** mediante la interfaz FastEthernet0.

---

## ⚙️ Tabla de Direccionamiento

| Dispositivo | Interfaz | Dirección IPv4 | Máscara de Subred | Gateway por Defecto |
| :--- | :--- | :--- | :--- | :--- |
| PC-A | FastEthernet0 | 192.168.1.10 | 255.255.255.0 | N/A |
| PC-B | FastEthernet0 | 192.168.1.11 | 255.255.255.0 | N/A |

---

## 🚀 Ejecución Paso a Paso

### 1. Despliegue de Capa 1 (Física)
- Se posicionaron dos terminales (PC) en el espacio de trabajo.
- Se utilizó un **Cable de Cobre Cruzado (Copper Cross-Over)** para conectar los puertos FastEthernet0 de ambos dispositivos, ya que al ser equipos de la misma capa, sus pines de transmisión (TX) y recepción (RX) deben cruzarse.

### 2. Configuración de Capa 3 (Red)
- Se ingresó a la configuración IP estática de la **PC-A** asignando la IP `192.168.1.10` con una máscara `/24` (`255.255.255.0`).
- Se repitió el procedimiento en la **PC-B** asignando la IP adyacente `192.168.1.11` dentro de la misma subred lógica.

---

## ✅ Prueba de Concepto (PoC) / Verificación

Para confirmar que el enlace es operativo, se ejecutó un pulso de sonar (Ping) desde la terminal (Command Prompt) de la PC-A hacia la PC-B.

**Comando ejecutado:**
`ping 192.168.1.11`

**Resultados obtenidos:**
> Reply from 192.168.1.11: bytes=32 time<1ms TTL=128
> Reply from 192.168.1.11: bytes=32 time<1ms TTL=128
> Reply from 192.168.1.11: bytes=32 time<1ms TTL=128
> Reply from 192.168.1.11: bytes=32 time<1ms TTL=128
> 
> Ping statistics for 192.168.1.11:
> Packets: Sent = 4, Received = 4, Lost = 0 (0% loss)

![[Pasted image 20260314193320.png]] 



---

## 🧠 Conclusión Táctica
El enlace P2P fue establecido con éxito. Se comprobó que sin la configuración física (cable correcto) y lógica (IPs en la misma subred), la comunicación ICMP no es posible. No se configuró Default Gateway ya que el tráfico no necesita salir de la red local (LAN) hacia un router.
