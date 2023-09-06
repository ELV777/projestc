 Este código crea un nuevo modelo llamado "Producto"
class Product(models.Model):
    _name = 'product.product'

    name = fields.Char('Nombre')
    price = fields.Float('Precio')

# Este código crea un nuevo registro en el modelo "Producto"
product = Product()
product.name = 'Producto 1'
product.price = 100
product.save()

# Este código recupera todos los registros del modelo "Producto"
products = Product.search([])

# Este código imprime todos los registros del modelo "Producto"
for product in products:
    print(product.name, product.price)