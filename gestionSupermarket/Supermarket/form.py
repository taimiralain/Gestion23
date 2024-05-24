from django import forms
from .models import Producto, Cliente

class OrdenCompraForm(forms.Form):
    cliente_id = forms.ModelChoiceField(queryset=Cliente.objects.all())
    provincia = forms.CharField()
    municipio = forms.CharField()
    direccion = forms.CharField()
    total_items = forms.IntegerField()
    total_importe = forms.DecimalField()
    cd = forms.CharField()
    productos = forms.ModelMultipleChoiceField(queryset=Producto.objects.all())
    cantidad = forms.IntegerField()

    def clean(self):
        cleaned_data = super().clean()
        productos = cleaned_data.get('productos')
        cantidad = cleaned_data.get('cantidad')
        if productos and cantidad:
            cleaned_data['productos'] = {producto.id: cantidad for producto in productos}
        return cleaned_data
