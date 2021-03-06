from django.contrib import admin
from django.urls import path, include
from negocio.views import painel_pedidos, add_pedido, close_pedido, status, lista_pedidos, index_screen
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('add/pedido/<slug:arduino>', add_pedido),
    path('close/pedido/<slug:arduino>', close_pedido),
    path('status/<slug:arduino>', status),
    path('list/pedido/', lista_pedidos, name='list'),
    path('painel/', painel_pedidos, name="painel"),
    path('', index_screen)
]
