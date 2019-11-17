from django.contrib import admin

# Register your models here.
from negocio.models import *

admin.site.register(Empresa)
admin.site.register(Dispositivo)
admin.site.register(Pedido)
