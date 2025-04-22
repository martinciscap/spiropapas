
<p align="center">
  <img src="logo.png" alt="Spiropapas Logo" width="200"/>
</p>

# 🧂 Spiropapas

**Spiropapas** es una herramienta simple y poderosa en Python para escanear todos los puertos abiertos de un dispositivo dentro de tu red local.  
Ideal para cuando olvidas qué puerto dejaste abierto (¡como el SSH! 🤦‍♂️) o simplemente quieres hacer un chequeo de accesos disponibles.

---

## 🔍 ¿Qué hace?

- Valida si la IP es correcta antes de hacer cualquier cosa.
- Hace ping para verificar si el host responde.
- Escanea **todos los puertos (1–65535)** para ver cuáles están abiertos.
- Usa múltiples hilos para hacerlo rápido.
- Muestra en consola los puertos abiertos.

---

## ⚙️ Requisitos

- Python 3.x
- Acceso a la red local del dispositivo que deseas escanear

---

## 🚀 Cómo ejecutar

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/spiropapas.git
   cd spiropapas
   ```

2. Ejecuta el escáner:
   ```bash
   python scanner.py
   ```

3. Escribe la IP del dispositivo cuando se te pida.

---

## 📁 Estructura del Proyecto

```
spiropapas/
├── assets/
│   └── spiropapas_logo_16bit.png  # Logo retro del proyecto
├── scanner.py                     # Código principal del escáner
├── README.md                      # Este archivo
```

---

## 🧪 Ejemplo de uso

```bash
Introduce la IP del dispositivo a escanear: 192.168.1.42

Iniciando escaneo de puertos en 192.168.1.42...

[+] Puerto abierto: 22
[+] Puerto abierto: 80
[+] Puerto abierto: 1883

Puertos abiertos encontrados:
[22, 80, 1883]
```

---

## 📜 Licencia

MIT License. Puedes usarlo, modificarlo o hacerle una versión con sabor a chipotle si quieres. Solo no lo uses con fines maliciosos.

---

## 🌮 ¿Por qué se llama Spiropapas?

Porque escanea en espiral, de forma ordenada, y porque suena chido 😎  
Y sí, nos gusta comer papas en la feria mientras hackeamos cosas.

---
