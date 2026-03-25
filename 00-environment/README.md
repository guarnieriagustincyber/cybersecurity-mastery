
# 🛡️ 00 - Environment (Laboratorio de Prácticas)

## 📌 Descripción

Este directorio documenta la configuración completa del laboratorio virtual aislado utilizado para todas las prácticas de ciberseguridad de redes. El laboratorio está diseñado para ser **seguro, reproducible y aislado** de redes externas.

---

## 🎯 Objetivos del Laboratorio

- [ ] Proporcionar un entorno seguro para prácticas ofensivas y defensivas
- [ ] Aislar completamente el tráfico de testing de redes externas
- [ ] Permitir captura y análisis de tráfico sin riesgos legales
- [ ] Ser reproducible en caso de necesitar reconstruir el entorno

---

## 🖥️ Configuración del Host

| Componente | Especificación |
|------------|----------------|
| **Sistema Operativo** | Linux Mint 22.3|
| **Hipervisor** | Virt-Manager (KVM/QEMU) |
| **RAM Host** | 16 GB |
| **CPU Host** | 12 núcleos |
| **Almacenamiento** | HDD secundario (/mnt/disco2/vms/) |
| **Ubicación** | Resistencia, Chaco, Argentina |

---

## 🌐 Topología de Red
┌─────────────────────────────────────────────────────────────┐
│ RED DE LABORATORIO │
│ 192.168.100.0/24 (AISLADA) │
│ │
│ ┌─────────────┐ ┌─────────────┐ │
│ │ KALI │ │ METASPLOITABLE 2 │
│ │ (Atacante) │ │ (Víctima) │
│ │192.168.100.76│ │192.168.100.120 │
│ │ 4GB RAM │ │ 2GB RAM │
│ │ 2 vCPU │ │ 2 vCPU │
│ └──────┬──────┘ └──────┬──────┘ │
│ │ │ │
│ └────────────────────┘ │
│ │ │
│ ┌────────────▼────────────┐ │
│ │ Red Virtual: │ │
│ │ kali-lab-net │ │
│ │ (Isolated Mode) │ │
│ │ 192.168.100.0/24 │ │
│ │ SIN NAT/SALIDA │ │
│ └─────────────────────────┘ │
│ │
│ ⚠️ NUNCA usar modo Bridge para laboratorios de ataque │
│ ⚠️ Todo el tráfico debe permanecer aislado │
└─────────────────────────────────────────────────────────────┘


---
