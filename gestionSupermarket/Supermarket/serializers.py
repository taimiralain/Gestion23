from rest_framework import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Cliente, Producto, OrdenCompra ,Almacen ,BolsaOrdenes, CentroDistribucion,OrdenCompraProducto

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class AlmacenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Almacen
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class OrdenCompraSerializer(serializers.ModelSerializer):
    productos = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Producto.objects.all()
    )

    class Meta:
        model = OrdenCompra
        fields = ['cliente', 'fecha_compra', 'fecha_aprobacion', 'provincia', 'municipio', 'direccion', 'total_items', 'total_importe', 'productos', 'cd']   

class BolsaOrdenesSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=True, read_only=True)
    
    class Meta:
        model = BolsaOrdenes
        fields = ['codigo', 'fecha', 'codigo_qr', 'orden_compra', 'productos']    

class CentroDistribucionSerializer(serializers.ModelSerializer):
    bolsas_entregadas = BolsaOrdenesSerializer(many=True, read_only=True)

    class Meta:
        model = CentroDistribucion
        fields = ['nombre', 'responsable', 'bolsas_entregadas', 'fecha_entrega']

class OrdenCompraProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenCompraProducto
        fields = ['producto', 'cantidad']

class OrdenCompraSerializer(serializers.ModelSerializer):
    productos = OrdenCompraProductoSerializer(source='ordencompraproducto_set', many=True)

    class Meta:
        model = OrdenCompra
        fields = ['cliente', 'fecha_compra', 'fecha_aprobacion', 'provincia', 'municipio', 'direccion', 'total_items', 'total_importe', 'productos', 'cd']

    def create(self, validated_data):
        productos_data = validated_data.pop('ordencompraproducto_set')
        orden_compra = OrdenCompra.objects.create(**validated_data)
        for producto_data in productos_data:
            OrdenCompraProducto.objects.create(orden_compra=orden_compra, **producto_data)
        return orden_compra

