from django import forms

from negocio.models import Empresa, Dispositivo, Pedido

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

class DispositivoForm(forms.ModelForm):
    empresa = forms.ModelChoiceField(queryset=Empresa.objects.all())
    class Meta:
        model = Dispositivo
        fields = '__all__'

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'