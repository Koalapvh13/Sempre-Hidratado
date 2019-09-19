from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class pedido(models.Model):
    SPEDIDOS  = [
        ('W', 'Aguardo'),
        ('D', 'Entrega'),
        ('F', 'Finalizado')
        ]
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    pedido = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=SPEDIDOS, default='W')
    entregador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entregador')
    