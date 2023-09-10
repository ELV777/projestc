def sumar(a, b):
  return a + b

def restar(a, b):
  return a - b

def multiplicar(a, b):
  return a * b

def dividir(a, b):
  return a / b

def calculadora():
  a = float(input("Ingrese el primer número: "))
  b = float(input("Ingrese el segundo número: "))
  operador = input("Ingrese el operador (+, -, *, /): ")

  if operador == "+":
    print(f"{a} {operador} {b} = {sumar(a, b)}")
  elif operador == "-":
    print(f"{a} {operador} {b} = {restar(a, b)}")
  elif operador == "*":
    print(f"{a} {operador} {b} = {multiplicar(a, b)}")
  elif operador == "/":
    print(f"{a} {operador} {b} = {dividir(a, b)}")

if __name__ == "__main__":
  calculadora()