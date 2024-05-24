from rest_framework import generics
from .models import Cliente , Almacen ,Producto ,BolsaOrdenes,CentroDistribucion,OrdenCompra
from .serializers import BolsaOrdenesSerializer ,ClienteSerializer, AlmacenSerializer ,CentroDistribucionSerializer, ProductoSerializer ,OrdenCompraSerializer 
import uuid
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import render,redirect, get_object_or_404
from .form import OrdenCompraForm

class ClienteListCreate(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class AlmacenListCreate(generics.ListCreateAPIView):
    queryset = Almacen.objects.all()
    serializer_class = AlmacenSerializer

class AlmacenDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Almacen.objects.all()
    serializer_class = AlmacenSerializer

class ProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class BolsaOrdenesCreate(generics.CreateAPIView):
    serializer_class = BolsaOrdenesSerializer

    def perform_create(self, serializer):
        codigo_unico = str(uuid.uuid4())
        serializer.save(codigo=codigo_unico)


class CentroDistribucionUpdate(generics.UpdateAPIView):
    queryset = CentroDistribucion.objects.all()
    serializer_class = CentroDistribucionSerializer

    def perform_update(self, serializer):
        serializer.save(fecha_entrega=timezone.now())
        
class BolsaOrdenesDetalle(generics.RetrieveAPIView):
    queryset = BolsaOrdenes.objects.all()
    serializer_class = BolsaOrdenesSerializer
    lookup_field = 'codigo'

class BolsaOrdenesDetailView(generics.RetrieveAPIView):
    queryset = BolsaOrdenes.objects.all()
    serializer_class = BolsaOrdenesSerializer
    lookup_field = 'codigo'

class OrdenCompraListCreate(generics.ListCreateAPIView):
    queryset = OrdenCompra.objects.all()
    serializer_class = OrdenCompraSerializer

class OrdenCompraDetail(generics.RetrieveAPIView):
    queryset = OrdenCompra.objects.all()
    serializer_class = OrdenCompraSerializer
    

def crear_orden_compra(request):
    if request.method == 'POST':
        form = OrdenCompraForm(request.POST)
        if form.is_valid():
            # Asegúrate de obtener el ID del cliente, no el objeto completo
            cliente_id = form.cleaned_data['cliente_id'].id
            cliente = Cliente.objects.get(id=cliente_id)
            
            # Crear la orden de compra con el ID del cliente
            orden_compra = OrdenCompra(
                cliente=cliente,
                fecha_compra=timezone.now(),
                fecha_aprobacion=timezone.now(),
                provincia=form.cleaned_data['provincia'],
                municipio=form.cleaned_data['municipio'],
                direccion=form.cleaned_data['direccion'],
                total_items=form.cleaned_data['total_items'],
                total_importe=form.cleaned_data['total_importe'],
                cd=form.cleaned_data['cd']
            )
            orden_compra.save()
            
            # Añadir productos a la orden de compra
            for producto in form.cleaned_data['productos']:
                orden_compra.productos.add(producto)
            
            # Redirigir a la página de detalle de la orden de compra
            return redirect('orden-compra-detail', pk=orden_compra.pk)
    else:
        form = OrdenCompraForm()
    return render(request, 'crear_orden_compra.html', {'form': form})

def home(request):
    return render(request, 'home.html')
