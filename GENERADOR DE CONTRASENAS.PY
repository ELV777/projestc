import string

def generar_contrasena():
  caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*()-_=+,./?"
  contraseña = "".join(random.choice(caracteres) for _ in range(12))
  return contraseña

if __name__ == "__main__":
  print(generar_contrasena())