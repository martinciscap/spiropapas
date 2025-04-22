import socket
import platform
import subprocess
import re
from concurrent.futures import ThreadPoolExecutor

# Función para validar una IP IPv4
def es_ip_valida(ip):
    patron = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    if re.match(patron, ip):
        partes = ip.split(".")
        return all(0 <= int(parte) <= 255 for parte in partes)
    return False

# Función para hacer ping
def host_responde(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    comando = ["ping", param, "1", ip]
    try:
        resultado = subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return resultado.returncode == 0
    except Exception:
        return False

# Pedir IP al usuario
ip = input("Introduce la IP del dispositivo a escanear: ").strip()

# Validar IP
if not es_ip_valida(ip):
    print("\n[!] La IP introducida no es válida. Asegúrate de usar el formato correcto (ej. 192.168.1.1).")
    exit()

# Verificar si el host responde
if not host_responde(ip):
    print(f"\n[!] El host {ip} no responde al ping. Revisa la IP y vuelve a intentarlo.")
    exit()

# Configuración del escaneo
start_port = 1
end_port = 65535
timeout = 0.5
open_ports = []

def scan_port(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"[+] Puerto abierto: {port}")
                open_ports.append(port)
    except:
        pass

print(f"\nIniciando escaneo de puertos en {ip}...\n")
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(start_port, end_port + 1))

print("\nPuertos abiertos encontrados:")
print(open_ports)