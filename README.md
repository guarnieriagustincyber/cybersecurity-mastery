# 🛡️ CYBERSECURITY MASTERY

## Formación Integral en Ciberseguridad de Redes

**Versión del Plan:** V9.5 (Integrada - Freelance Principal)  
**Enfoque:** Sin resúmenes, sin atajos, sin librerías mágicas   
**Alineación:** Licenciatura en Ciberdefensa (FADENA)

---

## 📊 PROGRESO ACTUAL

| Fase | Estado | Progreso | Próximo Hito |
|------|--------|----------|--------------|
| **Fase 0** | ✅ Completada | 100% | — |
| **Fase 1** | 🔄 En curso | 5% | Módulo 1 completo (Sem 3) |
| **Fase 2** | ⬜ Pendiente | 0% | Inicia Jun 8 |
| **Fase 3** | ⬜ Pendiente | 0% | Inicia Sep 1 |

### Certificaciones en Progreso

| Certificación | Proveedor | Progreso | Fecha Objetivo | Estado |
|---------------|-----------|----------|----------------|--------|
| **Cisco Intro to Cybersecurity** | Cisco | 🔄 80% (4/5 módulos) | Mar 2026 | Casi completo |
| **Cisco Basic Network Concepts** | Cisco | 🔄 24% (4/17 módulos) | Abr 2026 | En curso |
| **Linux Essentials** | LPI/Cisco | ⬜ 0% | May 2026 | Pendiente |
| **Cisco Ethical Hacker** | Cisco | ⬜ 0% | Jun 2026 | Pendiente |
| **Fortinet NSE 1-3** | Fortinet | ⬜ 0% | Jun 2026 | Pendiente |
| **Helsinki Python MOOC** | U. Helsinki | ⬜ 0% | Jul 2026 | Pendiente |
| **Helsinki Cyber Security Base** | U. Helsinki | ⬜ 0% | Ago 2026 | Pendiente |
| **ISC2 CC** | ISC2 | ⬜ 0% | Ago 2026 | Pendiente |
| **Security+** | CompTIA | ⬜ 0% | Oct 2026 | Pendiente |

### Métricas de GitHub

| Métrica | Actual | Objetivo (Nov 2026) |
|---------|--------|---------------------|
| Commits | ~10 | 100+ |
| Ejercicios Python | 0 | 60+ |
| PCAPs Documentados | 0 | 15+ |
| Servicios Freelance | 0 | 10 |
| Herramientas Originales | 0 | 3+ |

---

## 🎯 FILOSOFÍA DE APRENDIZAJE

| Principio | Descripción | Aplicación |
|-----------|-------------|------------|
| **Sin Resúmenes** | Todo contenido se enseña con profundidad completa | La IA debe expandir, no condensar |
| **Sin Librerías Mágicas** | Python desde cero, entendiendo cada logica | Construir packets manualmente antes de usar Scapy |
| **Teoría + Práctica Inmediata** | Cada concepto tiene su lab correspondiente |
| **Documentación Obligatoria** | Todo ejercicio se documenta | GitHub como portafolio profesional |
| **Mentalidad Dual** | Cada técnica se aprende desde ataque y defensa | Saber explotar y saber detectar |
| **Android ** | fundamentos | 5% máximo, Mes 8+ |



---

## 🗓️ CRONOGRAMA 

| Mes | Fase | Enfoque Principal | Certificaciones | Entregables |
|-----|------|-------------------|-----------------|-------------|
| **Mar** | Fase 0-1 | Laboratorio + Módulo 1 | Cisco Intro Cyber (80%) | 00-environment + Ej 1.1-1.3 |
| **Abr** | Fase 1 | Módulo 2 (Capa 2) | Cisco Networks (4/17) + Linux Essentials | Ej 2.1-2.8 + 4 PCAPs |
| **May** | Fase 1 | Módulo 3 (Capa 3) | Fortinet NSE 1-3 | Ej 3.1-3.8 + 3 PCAPs |
| **Jun** | Fase 2 | Módulo 4 (Capa 4) | Cisco Ethical Hacker | Ej 4.1-4.4 + 3 PCAPs |
| **Jul** | Fase 2 | Módulo 4.5 (Tráfico) | Helsinki Python ✅ | 1 herramienta + 3 PCAPs |
| **Ago** | Fase 2 | Módulo 5-6 (App + Blue) | ISC2 CC + Helsinki CyberSec | 2 herramientas + 3 PCAPs |
| **Sep** | Fase 3 | Freelance Setup | Security+ (prep) | 10 servicios documentados |
| **Oct** | Fase 3 | Freelance Activo | Security+ ✅ | 2-3 gigs completados |
| **Nov** | Fase 3 | Consolidación | eJPT (prep) | $500-1500 USD/mes |

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
│         │   SIN NAT/SALIDA        │                          │
│         └─────────────────────────┘                          │
│                                                             │
│  Host: Linux Mint + Virt-Manager (KVM)                      │
│  Wireshark: Instalado en Host                               │
└─────────────────────────────────────────────────────────────┘
```

### Estado del Laboratorio

| Componente | Estado | Última Verificación |
|------------|--------|---------------------|
| Kali Linux | ✅ Funcional | 2026-03-25 |
| Metasploitable 2 | ✅ Funcional | 2026-03-25 |
| Red Aislada | ✅ Funcional | 2026-03-25 |
| Wireshark (Host) | ✅ Funcional | 2026-03-25 |
| Internet desde VMs | ❌ Bloqueado | 2026-03-25 |
| Conectividad entre VMs | ✅ Funcional | 2026-03-25 |

---

## ✅ MÉTRICAS DE ÉXITO 
### Fundamentos
- [ ] 6 Módulos del Plan Maestro completados
- [ ] 60+ ejercicios Python en GitHub
- [ ] 15+ PCAPs documentados y analizados
- [ ] 3+ herramientas originales funcionales

### Certificaciones
- [ ] 7-8 certificaciones completadas
- [ ] Badges documentados en GitHub
- [ ] Security+ (completo o en proceso)

### Freelance
- [ ] 10 servicios de red documentados
- [ ] Perfiles Workana/Fiverr/Upwork activos
- [ ] 5+ gigs completados (o 1 empleo junior)
- [ ] 2-3 clientes recurrentes

### Portafolio
- [ ] GitHub público y limpio
- [ ] README principal actualizado
- [ ] 100+ commits totales


### Habilidades Adicionales 
- [ ] Android Security Básico
---

## 📚 RECURSOS PRINCIPALES

### Libros Fundamentales
| Libro | Autor | Prioridad |
|-------|-------|-----------|
| Computer Networks | Andrew Tanenbaum | ⭐⭐⭐⭐⭐ |
| TCP/IP Illustrated Vol 1 | W. Richard Stevens | ⭐⭐⭐⭐⭐ |
| Network Security Assessment | Chris McNab | ⭐⭐⭐⭐ |
| The Practice of Network Security Monitoring | Richard Bejtlich | ⭐⭐⭐⭐ |

### RFCs Esenciales
| RFC | Título | Relevancia |
|-----|--------|------------|
| RFC 791 | Internet Protocol | IP Header |
| RFC 792 | ICMP | Ping, errores |
| RFC 793 | TCP | Handshake, flags |
| RFC 826 | ARP | Resolución MAC |
| RFC 1918 | Private Address Space | IPs privadas |

### Herramientas Esenciales
| Categoría | Herramienta | Uso |
|-----------|-------------|-----|
| Virtualización | Virt-Manager (KVM) | Laboratorio aislado |
| Análisis PCAP | Wireshark, tcpdump | Captura y análisis |
| Escaneo | Nmap | Descubrimiento de red |
| IDS/IPS | Snort, Suricata | Detección de intrusiones |
| Firewall | pfSense, iptables | Filtrado de tráfico |

---

## 🔗 ENLACES IMPORTANTES

| Recurso | Link |
|---------|------|
| **Cisco Networking Academy** | https://www.netacad.com/ |
| **Helsinki MOOC** | https://www.mooc.fi/en/courses/ |
| **Fortinet Training** | https://www.fortinet.com/resources/cybersecurity/cybersecurity-training |
| **ISC2 CC** | https://www.isc2.org/Certifications/CC |
| **OWASP** | https://owasp.org/ |
| **GitHub Repo** | https://github.com/guarnieriagustincyber/cybersecurity-mastery |

---

