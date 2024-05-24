from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Producto
import logging
from .consumers import consumidor_de_producto

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Producto)
def producto_creado(sender, instance, created, **kwargs):
    if created:
        logger.info(f"Se ha creado un nuevo producto: {instance.nombre} con ID: {instance.id}")



@receiver(post_save, sender=Producto)
def producto_creado(sender, instance, created, **kwargs):
    if created:
        consumidor_de_producto(sender, instance, **kwargs)

