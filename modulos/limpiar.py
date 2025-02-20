from os import system
import sys
import os
def borrar_pantalla():
  if sys.platform == "linux" or sys.platform == "darwin":
    system("clear")
  else:
    os.system("cls")

def pausar_pantalla():
  if sys.platform == "linux" or sys.platform == "darwin":
    x=input("Presione un tecla para continuar")
  else:
    os.system("pause")