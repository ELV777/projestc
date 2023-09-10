def convertir_unidades(valor, unidad_origen, unidad_destino):
  if unidad_origen == "metro" and unidad_destino == "centímetro":
    return valor * 100
  elif unidad_origen == "metro" and unidad_destino == "kilómetro":
    return valor / 1000
  elif unidad_origen == "centímetro" and unidad_destino == "metro":
    return valor / 100
  elif unidad_origen == "centímetro" and unidad_destino == "kilómetro":
    return valor / 100000
  elif unidad_origen == "kilómetro" and unidad_destino == "metro":
    return valor * 1000
  elif unidad_origen == "kilómetro" and unidad_destino == "centímetro":
    return valor * 100000

def conversor_unidades():
  valor = float(input("Ingrese el valor: "))
  unidad_origen = input("Ingrese la unidad de medida de origen: ")
  unidad_destino = input("Ingrese la unidad de medida de destino: ")

  print(f"{valor} {unidad_origen} = {convertir_unidades(valor, unidad_origen, unidad_destino)} {unidad_destino}")

if __name__ == "__main__":
  conversor_unidades()