from django.shortcuts import render
from negocio.models import Empresa, Dispositivo, Pedido
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from negocio.form import *
from django.utils import timezone
from django.utils.dateformat import format


@csrf_exempt
def add_empresa(request):
    if request.method == 'POST':
        e = Empresa(nome=request.POST['empresa'],
                    cnpj=request.POST['cnpj'],
                    telefone=request.POST['telefone']
                    )
        e.save()
        return HttpResponse("Salvo!")


@csrf_exempt
def add_dispositivo(request):
    if request.method == 'POST':
        e = Dispositivo(apelido=request.POST['apelido'],
                        uuid=request.POST['uuid'],
                        empresa=Empresa.objects.get(
                            cnpj=request.POST['empresa'])
                        )
        e.save()
        return HttpResponse("Salvo!")


@csrf_exempt
def add_pedido(request, arduino):
    e = Pedido(estado=0,
               dispositivo=Dispositivo.objects.get(
                   uuid=arduino)
               )
    e.save()
    return HttpResponse(e.dispositivo.apelido + "\n" + str(e.data_pedido))


@csrf_exempt
def close_pedido(request, arduino):
    d = Dispositivo.objects.get(uuid=arduino)
    pedido = Pedido.objects.get(
        dispositivo=d, data_entrega__isnull=True)
    pedido.estado = True
    pedido.data_entrega = timezone.now()
    pedido.save()
    return JsonResponse({
        'status': pedido.dispositivo.apelido,
        'estado': pedido.estado
    })


def status(request, arduino):
    d = Dispositivo.objects.get(uuid=arduino)
    pedido = Pedido.objects.filter(
        dispositivo=d, data_entrega__isnull=True)
    return JsonResponse({'status': 'V' if (len(pedido) > 0)else 'C'})


def lista_pedidos(request):

    std = 200
    json_resp = {}
    pedidos = Pedido.objects.filter(estado=False).order_by('-data_pedido')

    if(len(pedidos) > 0):
        lista = []
        for p in pedidos:
            lista.append({
                'id_pedido': p.pk,
                'empresa': p.dispositivo.empresa.nome,
                'dispositivo': p.dispositivo.apelido,
                'data_pedido': p.data_pedido.strftime('%d/%m/%Y %H:%M')
            })
        json_resp['pedidos'] = lista
        json_resp['status'] = 200

    else:
        json_resp['erro_msg'] = "Não Há Pedidos!"
        json_resp['status'] = 404
        std = 200
    return JsonResponse(json_resp, status=std)


def painel_pedidos(request):
    pedidos = Pedido.objects.filter(estado=False).order_by('-data_pedido')
    return render(request, "negocio/painel.html", {"pedidos":pedidos})

def index_screen(request):
    return render(request, "negocio/index.html")
