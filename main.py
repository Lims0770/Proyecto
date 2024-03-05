import sys
import os
import socket
import threading
import argparse


def main():
  """
  Función principal del programa.
  """

  parser = argparse.ArgumentParser(description="Analizador de Puertos Simplificado")
  parser.add_argument("-d", "--direccion", help="La dirección IP o nombre del host", required=True)
  parser.add_argument("-p", "--puertos", help="Los puertos a analizar (separados por comas)", required=True)
  parser.add_argument("-t", "--hilos", help="Número de hilos a usar (por defecto: 10)", type=int, default=10)

  args = parser.parse_args()

  direccion = args.direccion
  puertos = args.puertos.split(",")
  hilos = args.hilos

  def analizar_puerto(puerto):
    try:
      puerto = int(puerto)
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.connect((direccion, puerto))
      print(f"Puerto {puerto}: Abierto")
      sock.close()
    except socket.error:
      print(f"Puerto {puerto}: Cerrado")

  hilos_activos = []
  for puerto in puertos:
    hilo = threading.Thread(target=analizar_puerto, args=(puerto,))
    hilos_activos.append(hilo)
    hilo.start()

  for hilo in hilos_activos:
    hilo.join()


if __name__ == "__main__":
  main()
