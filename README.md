# 🛡️ CYBERSECURITY MASTERY

## Formación Integral en Ciberseguridad de Redes

**Enfoque:** Sin resúmenes, sin atajos, sin librerías mágicas  
**Duración:** 9 meses (Mar 2026 - Nov 2026) 
**Estado:** 🔄 En Progreso (Semana 1)  
**Alineación:** Licenciatura en Ciberdefensa (FADENA)

---

## 👤 

| Campo | Valor |
|-------|-------|
| **Ubicación** | Argentina |
| **Formación** | Licenciatura en Ciberdefensa (FADENA) |
| **GitHub** | [guarnieriagustincyber](https://github.com/guarnieriagustincyber) |
| **LinkedIn** | [agustin-guarnieri](https://www.linkedin.com/in/agustin-guarnieri-19702a228/) |
| **Email** | [Contactar vía LinkedIn] |

---

## 📊 PROGRESO ACTUAL

| Fase | Estado | Progreso | Próximo Hito |
|------|--------|----------|--------------|
| **Fase 0** | ✅ Completada | 100% | — |
| **Fase 1** | 🔄 En curso | 5% | Módulo 1 + Proyecto 1 (Sem 3) |
| **Fase 2** | ⬜ Pendiente | 0% | Inicia Jun 8 |
| **Fase 3** | ⬜ Pendiente | 0% | Inicia Sep 1 |

### Certificaciones

| Certificación | Proveedor | Estado |
|---------------|-----------|--------|
| Cisco Intro to Cybersecurity | Cisco | ✅ Completada |
| Cisco Basic Network Concepts | Cisco | 🔄 24% |
| Linux Essentials | LPI/Cisco | ⬜ Pendiente |
| Cisco Ethical Hacker | Cisco | ⬜ Pendiente |
| Fortinet NSE 1-3 | Fortinet | ⬜ Pendiente |
| ISC2 CC | ISC2 | ⬜ Pendiente |
| Security+ | CompTIA | ⬜ Pendiente |

---

## 🎯 FILOSOFÍA DE APRENDIZAJE

| Principio | Descripción |
|-----------|-------------|
| **Sin Resúmenes** | Todo contenido se estudia con profundidad completa |
| **Sin Librerías Mágicas** | Python desde cero, entendiendo cada byte |
| **Teoría + Práctica Inmediata** | Cada concepto tiene su lab correspondiente |
| **Documentación Obligatoria** | Todo ejercicio/proyecto se documenta como evidencia |
| **Mentalidad Dual** | Cada técnica se aprende desde ataque y defensa |
| **Proyectos > Ejercicios** | Transición gradual: 80/20 → 50/50 → 20/80 |

---

## 📁 ESTRUCTURA DEL REPOSITORIO

```
cybersecurity-mastery/
├── README.md                      # Este archivo
├── tracking.md                    # Progreso – Faro de Ruta
│
├── 00-environment/                # Configuración del laboratorio
│   ├── README.md
│   ├── kali-setup.md
│   ├── metasploitable-setup.md
│   ├── network-config.md
│   ├── network-topology.png
│   ├── screenshots/
│   └── verification-scripts/
│
├── 01-fundamentals/               # Módulo 1 – Fundamentos
│   ├── exercises/
│   └── projects/
│
├── 02-ip-addressing/              # Módulo 2 – Direccionamiento IP
├── 03-subnetting/                 # Módulo 3 – Subnetting
├── 04-transport/                  # Módulo 4 – Transporte
│   └── labs/
│       └── traffic-analysis/      # (ex 04.5-traffic-analysis)
│
├── 05-application/                # Módulo 5 – Aplicación
├── 06-routing-switching/          # Módulo 6 – Routing & Switching
│   ├── exercises/
│   └── labs/
│
├── 07-network-security/           # Módulo 7 – Seguridad de Red
├── 08-consolidation/              # Módulo 8 – Consolidación
│   └── project/
│
├── certifications/                # Evidencia de certificaciones
│   ├── cisco/
│   └── helsinki/
│
└── _optional/                     # Contenido opcional
    └── android-security/
```

---

## 🗓️ CRONOGRAMA HÍBRIDO (9 MESES)

| Mes | Fase | Ejercicios | Proyectos | Certificaciones |
|-----|------|------------|-----------|-----------------|
| **Mar** | 0-1 | 10 | 1 pequeño | Cisco Intro Cyber ✅ | 
| **Abr** | 1 | 10 | 1 pequeño | Cisco Networks + Fundamentos I |
| **May** | 1 | 10 | 1 pequeño | Linux Essentials + Fundamentos II | 
| **Jun** | 2 | 5 | 1 mediano | Cisco Ethical Hacker | 
| **Jul** | 2 | 5 | 1 mediano | Helsinki Python ✅ | 
| **Ago** | 2 | 5 | 1 mediano | ISC2 CC + SOC + Helsinki CyberSec | 
| **Sep** | 3 | 2 | 1 grande | Security+ (prep) | 
| **Oct** | 3 | 2 | 1 grande | Security+ ✅ + AWS Cloud | 
| **Nov** | 3 | 0 | 1 grande | eJPT (prep) | 

---

## 🛠️ LABORATORIO

### Topología de Red

```
┌─────────────────────────────────────────────────────────────┐
│                    RED DE LABORATORIO                       │
│                  192.168.100.0/24 (AISLADA)                 │
│                                                             │
│  ┌─────────────┐      ┌─────────────┐                       │
│  │   KALI      │      │ METASPLOITABLE 2                   │
│  │  (Atacante) │      │   (Víctima)                        │
│  │192.168.100.76│     │192.168.100.120                     │
│  │  4GB RAM    │      │   2GB RAM                          │
│  │  2 vCPU     │      │   2 vCPU                           │
│  └──────┬──────┘      └──────┬──────┘                       │
│         │                    │                               │
│         └────────────────────┘                               │
│                      │                                       │
│         ┌────────────▼────────────┐                          │
│         │   Red Virtual:          │                          │
│         │   kali-lab-net          │                          │
│         │   (Isolated Mode)       │                          │
│         │   192.168.100.0/24      │                          │
│         │   SIN NAT/SALIDA        │                          │
│         └─────────────────────────┘                          │
│                                                             │
│  Host: Linux Mint + Virt-Manager (KVM)                      │
│  Wireshark: Instalado en Host                               │
└─────────────────────────────────────────────────────────────┘
```

---

## 📚 RECURSOS PRINCIPALES

### Libros Fundamentales

| Libro | Autor | Prioridad | Estado |
|-------|-------|-----------|--------|
| Computer Networks | Andrew Tanenbaum | ⭐⭐⭐⭐⭐ | 📖 En estudio |
| TCP/IP Illustrated Vol 1 | W. Richard Stevens | ⭐⭐⭐⭐⭐ | 📖 En estudio |
| Network Security Assessment | Chris McNab | ⭐⭐⭐⭐ | ⬜ Pendiente |
| The Practice of Network Security Monitoring | Richard Bejtlich | ⭐⭐⭐⭐ | ⬜ Pendiente |

### RFCs Esenciales

| RFC | Título | Relevancia |
|-----|--------|------------|
| RFC 791 | Internet Protocol | IP Header |
| RFC 792 | ICMP | Ping, errores |
| RFC 793 | TCP | Handshake, flags |
| RFC 826 | ARP | Resolución MAC |
| RFC 1918 | Private Address Space | IPs privadas |

---

## 🔗 ENLACES IMPORTANTES

| Recurso | Link |
|---------|------|
| **GitHub Repo** | https://github.com/guarnieriagustincyber/cybersecurity-mastery |
| **Cisco Networking Academy** | https://www.netacad.com/ |
| **Helsinki MOOC** | https://www.mooc.fi/en/courses/ |
| **Helsinki Python MOOC 2026** | https://programming-26.mooc.fi/ |
| **Helsinki Cyber Security Base** | https://cybersecuritybase.mooc.fi/ |
| **Fortinet Training** | https://www.fortinet.com/resources/cybersecurity/cybersecurity-training |
| **ISC2 CC** | https://www.isc2.org/Certifications/CC |
| **LinkedIn** | https://www.linkedin.com/in/agustin-guarnieri-19702a228/ |

---

## ⚠️ AVISO LEGAL Y ÉTICO

```
╔═══════════════════════════════════════════════════════════╗
║  Todo el conocimiento debe usarse                         ║
║  EXCLUSIVAMENTE en entornos controlados y propios.        ║
║                                                           ║
║  ❌ NUNCA uses estas técnicas en:                         ║
║     - Redes que no te pertenecen                          ║
║     - Sistemas sin autorización escrita                   ║
║     - Infraestructura crítica                             ║
║                                                           ║
║  ✅ SOLO usa estas técnicas en:                           ║
║     - Tu laboratorio virtual aislado                      ║
║     - Máquinas que poseés y controlás                     ║
║     - Entornos de testing autorizados                     ║
║                                                           ║
║  El uso no autorizado es ILEGAL y puede tener             ║
║  consecuencias penales graves.                            ║
╚═══════════════════════════════════════════════════════════╝
```
---

> 🚀 **"El camino es largo pero cada paso te hará más fuerte como profesional. La constancia vence al talento cuando el talento no es constante."**
