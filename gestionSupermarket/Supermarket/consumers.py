import logging

logger = logging.getLogger(__name__)

def consumidor_de_producto(sender, instance, **kwargs):
    # Lógica que se ejecutará cuando se reciba la señal
    logger.info(f"Producto consumido: {instance.nombre}")
