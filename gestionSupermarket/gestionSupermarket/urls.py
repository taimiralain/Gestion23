"""
URL configuration for gestionSupermarket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Supermarket.views import crear_orden_compra,BolsaOrdenesDetailView,OrdenCompraListCreate,OrdenCompraDetail,home,ClienteListCreate,BolsaOrdenesDetalle ,CentroDistribucionUpdate,BolsaOrdenesCreate, AlmacenListCreate, AlmacenDetailUpdateDelete ,ProductoListCreate, ProductoDetailUpdateDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('clientes/', ClienteListCreate.as_view(), name='cliente-list-create'),
    path('almacenes/', AlmacenListCreate.as_view(), name='almacen-list-create'),
    path('almacenes/<int:pk>/', AlmacenDetailUpdateDelete.as_view(), name='almacen-detail-update-delete'),
    path('productos/', ProductoListCreate.as_view(), name='producto-list-create'),
    path('productos/<int:pk>/', ProductoDetailUpdateDelete.as_view(), name='producto-detail-update-delete'),
    path('orden-compra/', OrdenCompraListCreate.as_view(), name='orden-compra-list-create'),
    path('orden-compra/<int:pk>/', OrdenCompraDetail.as_view(), name='orden-compra-detail'),
    path('orden-compra/nueva/', crear_orden_compra, name='crear-orden-compra'),
    path('bolsa-ordenes/<str:codigo>/', BolsaOrdenesDetailView.as_view(), name='bolsa-ordenes-detail'),
    path('bolsa-ordenes/crear/add/', BolsaOrdenesCreate.as_view(), name='bolsa-ordenes-crear'),
    path('centro-distribucion/<int:pk>/actualizar/', CentroDistribucionUpdate.as_view(), name='centro-distribucion-actualizar'),
    path('bolsa-ordenes/<str:codigo>/', BolsaOrdenesDetalle.as_view(), name='bolsa-ordenes-detalle'),


]
