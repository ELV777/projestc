import os

def contar_palabras(archivo):
  with open(archivo, "r") as f:
    contenido = f.read()
    palabras = contenido.split(" ")
    return len(palabras)

if __name__ == "__main__":
  archivo = input("Escribe el nombre del archivo: ")
  numero_palabras = contar_palabras(archivo)
  print(f"El archivo '{archivo}' tiene {numero_palabras} palabras.")