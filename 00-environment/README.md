# 🛡️ 00 - Environment (Laboratorio de Prácticas)

## 📌 Descripción

Este directorio documenta la configuración completa del laboratorio virtual aislado utilizado para todas las prácticas de ciberseguridad de redes. El laboratorio está diseñado para ser **seguro, reproducible y aislado** de redes externas.

---

## 🎯 Objetivos del Laboratorio

- [x ] Proporcionar un entorno seguro para prácticas ofensivas y defensivas
- [ x] Aislar completamente el tráfico de testing de redes externas
- [ x] Permitir captura y análisis de tráfico sin riesgos legales
- [ x] Ser reproducible en caso de necesitar reconstruir el entorno

---

## 🖥️ Configuración del Host

| Componente | Especificación |
|------------|----------------|
| **Sistema Operativo** | Linux Mint 21.x |
| **Hipervisor** | Virt-Manager (KVM/QEMU) |
| **RAM Host** | 8 GB+ |
| **CPU Host** | 4+ núcleos |
| **Almacenamiento** | HDD secundario (/mnt/disco2/vms/) |

---

---

## 📋 Máquinas Virtuales

### 1. Kali Linux (Atacante)

| Campo | Valor |
|-------|-------|
| **Nombre VM** | `Kali-Linux-Attacker` |
| **IP** | `192.168.100.76` (DHCP) |
| **RAM** | 4096 MB |
| **vCPU** | 2 |
| **Disco** | 50 GB (qcow2) |
| **Red** | `kali-lab-net` (aislada) |
| **Usuario** | `kali` |
| **Contraseña** | `kali` |
| **Propósito** | Herramientas de testing, análisis, desarrollo Python |

**Comandos de Verificación:**
```bash
# Verificar IP
ip addr show eth0

# Verificar conectividad con víctima
ping -c 4 192.168.100.120

# Verificar AISLAMIENTO (debe FALLAR)
ping -c 4 8.8.8.8

```
### 2. metasploitable2(Victima)
| Campo | Valor |
| Nombre VM | Metasploitable2-victim |
| IP | 192.168.120 (DHCP)|
| RAM | 2048 MB|
| vCPU | 2 |
| Disco | 8 Gb (vmdk) |
| Red | kali-lab-net (aislada) |
| Uuario | msfadmin |
| Contraseña | msfadmin |
| Proposito | Servicios vulnerables para testing |

### Comandos de Verificacion 
``` Bash
# Verificar IP
ifconfig eth0

# Verificar conectividad con Kali
ping -c 4 192.168.100.76

# Verificar servicios abiertos
netstat -tulpn
```
| Puerto     | Servicio      | Versión       | Vulnerabilidad | 
| 21/tcp     |   FTP    |  vsftpd 2.3.4      |  backdor (CVE-2011-2523) |
| 22/tcp      | SSH      | OpenSSH 4.7p1       |  Versión obsoleta |
| 23/tcp     |  telnet     |  Linux talnetd      |  sin enciptación | 
|   80/tcp   |    HTTP   |    Apache 2.2.8    |  Múltiples CVEs |
|   3306/tcp   |    MySQL   |   5.0.51a     |   Versión obsoleta   |
|    5432/tcp  |    PostgreSQL   |  8.3.x   |   Versión obsoleta   |
|  1524/tcp    |    Bindshell   |    Metasploitable    |  Shell root directa    |



### COnfiguracion de Red Virtual
Red: kali-lab-net
| Nombre    | kali-lab-net      |
|  Tipo      |  isolated (sin NAT)     |
| Subnet       |   192.168.100.0/24    |
| Getway       | 192.158.100.1      |
| DHCP Range       | 192.168.100.2 - 192.168.100.254      |
| Salida a internet       | Desactivado      |
| Forwarding       |  Desactivado     |

### Comandos de Verificacion (Host):
``` Bash
# Listar redes virtuales
virsh net-list --all

# Ver detalles de la red
virsh net-dumpxml kali-lab-net

# Verificar que está activa
virsh net-info kali-lab-net
```


