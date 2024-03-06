import sys
import os
import socket
import threading
import argparse


def main():
    parser = argparse.ArgumentParser(description="Analizador de Puertos Simplificado")
    parser.add_argument("-d", "--direccion", help="La dirección IP o nombre del host", required=True)
    parser.add_argument("-p", "--puertos", help="Los puertos a analizar (separados por comas)", required=True)
    parser.add_argument("-t", "--hilos", help="Número de hilos a usar (por defecto: 10)", type=int, default=10)
    parser.add_argument("-a", "--todos", help="Analizar todos los puertos (ignora la opción -p)", action="store_true")

    args = parser.parse_args()

    direccion = args.direccion
    hilos = args.hilos

    # Imprimir información del sistema usando sys y os
    print(f"Sistema Operativo: {os.name}")
    print(f"Versión de Python: {sys.version}")

    if args.todos:
        analizar_todos_puertos(direccion, hilos)
    else:
        puertos = args.puertos.split(",")
        analizar_puertos_especificos(direccion, puertos, hilos)


def analizar_puerto(direccion, puerto):
    try:
        puerto = int(puerto)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((direccion, puerto))
        print(f"Puerto {puerto}: Abierto")
        sock.close()
    except socket.error:
        print(f"Puerto {puerto}: Cerrado")


def analizar_todos_puertos(direccion, hilos):
    for puerto in range(1, 65536):  # Rango de puertos válidos
        hilo = threading.Thread(target=analizar_puerto, args=(direccion, puerto))
        hilo.start()


def analizar_puertos_especificos(direccion, puertos, hilos):
    hilos_activos = []
    for puerto in puertos:
        hilo = threading.Thread(target=analizar_puerto, args=(direccion, puerto))
        hilos_activos.append(hilo)
        hilo.start()

    for hilo in hilos_activos:
        hilo.join()


if __name__ == "__main__":
    main()



