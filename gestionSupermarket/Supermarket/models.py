from django.db import models

# Modelo para Cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion_entrega = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    def __str__(self):
            return self.nombre

# Modelo para Producto
class Producto(models.Model):
    codigo = models.CharField(max_length=100, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=100)
    nombre_translate = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    volumen = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.CharField(max_length=100)
    descripcion = models.TextField()
    TEMPERATURA_CHOICES = [
        ('Ambient', 'Ambiente o Seco'),
        ('Chilled', 'Refrigerado'),
        ('Frozen', 'Congelado'),
    ]
    temperatura = models.CharField(max_length=10, choices=TEMPERATURA_CHOICES)
    def __str__(self):
            return self.nombre

# Modelo para Orden de Compra
class OrdenCompra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField()
    fecha_aprobacion = models.DateTimeField()
    provincia = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    total_items = models.IntegerField()
    total_importe = models.DecimalField(max_digits=10, decimal_places=2)
    productos = models.ManyToManyField(Producto, through='OrdenCompraProducto')
    cd = models.CharField(max_length=100)  # Asumiendo que CD es un campo de texto
    def __str__(self):
            return self.cliente.nombre

class BolsaOrdenes(models.Model):
    codigo = models.CharField(max_length=100, unique=True)
    fecha = models.DateTimeField(auto_now_add=True)
    codigo_qr = models.CharField(max_length=200, unique=True)
    orden_compra = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)


class Almacen(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    activo = models.BooleanField(default=True)
    latitud = models.DecimalField(max_digits=10, decimal_places=6)
    longitud = models.DecimalField(max_digits=10, decimal_places=6)

class CentroDistribucion(models.Model):
    nombre = models.CharField(max_length=100)
    responsable = models.CharField(max_length=100)
    bolsas_entregadas = models.ManyToManyField('BolsaOrdenes', related_name='centros_distribucion')
    fecha_entrega = models.DateTimeField(null=True, blank=True)

class OrdenCompraProducto(models.Model):
    orden_compra = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)