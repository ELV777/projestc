  Este código crea un nuevo modelo llamado "Cliente"
class Customer(models.Model):
    _name = 'res.partner'

    name = fields.Char('Nombre')
    address = fields.Char('Dirección')
    phone = fields.Char('Teléfono')

# Este código crea un nuevo registro en el modelo "Cliente"
customer = Customer()
customer.name = 'Cliente 1'
customer.address = 'Calle 1, número 1'
customer.phone = '123456789'
customer.save()

# Este código recupera todos los registros del modelo "Cliente"
customers = Customer.search([])

# Este código imprime todos los registros del modelo "Cliente"
for customer in customers:
    print(customer.name, customer.address, customer.phone)