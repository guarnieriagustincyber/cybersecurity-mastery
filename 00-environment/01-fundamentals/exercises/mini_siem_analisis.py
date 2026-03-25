"""
Analizador Lógico de Tráfico de Red (Mini-SIEM)
Autor: Agustín
Descripción: Script core para la detección de anomalías en red (Exfiltración y Reverse Shells)
basado en la evaluación de puertos y volumen de datos, utilizando estructuras de control nativas.
"""

# 1. Base de datos simulada (Ingesta de logs en bruto)
trafico_red = [
    {"ip_origen": "10.10.50.2", "puerto": 80, "bytes_enviados": 1500},
    {"ip_origen": "192.168.1.100", "puerto": 4444, "bytes_enviados": 300},
    {"ip_origen": "172.16.0.5", "puerto": 22, "bytes_enviados": 85000},
]

# 2. Inicialización de estructuras de contención
lista_negra_ips = []

# 3. Motor de análisis lógico (Reglas de detección)
for trafico in trafico_red:
    # Regla A: Detección de posible exfiltración por SSH (Volumen anómalo)
    if trafico["puerto"] == 22 and trafico["bytes_enviados"] > 50000:
        lista_negra_ips.append(trafico["ip_origen"])
        print(f"[CRÍTICO] Exfiltración de datos detectada desde {trafico['ip_origen']}")

    # Regla B: Detección de puertos maliciosos conocidos (Ej: Metasploit default)
    elif trafico["puerto"] == 4444:
        lista_negra_ips.append(trafico["ip_origen"])
        print(f"[ALERTA] Posible Reverse Shell detectada desde {trafico['ip_origen']}")

    # Regla C: Tráfico benigno
    else:
        print(f"[INFO] Tráfico normal desde {trafico['ip_origen']}")

# 4. Resolución y mitigación (Verificación Truthiness)
print("-" * 40)  # Separador visual en consola

if lista_negra_ips:
    print("🚨 INICIANDO PROTOCOLO DE BLOQUEO 🚨")
    for ip_aislada in lista_negra_ips:
        print(f"-> IP comprometida y enviada a Firewall: {ip_aislada}")
else:
    print("✅ Red segura. No se detectaron anomalías.")
