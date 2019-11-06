from django.db import models

# Create your models here.


class Empresa(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=50)
    cnpj = models.CharField(verbose_name='CNPJ', max_length=25)
    telefone = models.CharField(verbose_name='Telefone', max_length=30)


    def __str__(self):
        return self.nome

class Dispositivo (models.Model):
    apelido = models.CharField(verbose_name="Nome Dispositivo", max_length=50)
    uuid = models.CharField(verbose_name='Arduino ID', max_length=50)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.apelido

class Pedido (models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    estado = models.BooleanField(verbose_name='Entregue?', default=True)
    data_pedido = models.DateTimeField(verbose_name='Data Solicitação', auto_now=True)
    data_entrega = models.DateTimeField(verbose_name='Data Entrega', null=True, blank=True)
    def __str__(self):
        situacao = "[OK] " if self.estado else "[OPEN] "
        return situacao + self.dispositivo.empresa.nome + "_" + self.dispositivo.apelido + "_" + str(self.data_pedido)