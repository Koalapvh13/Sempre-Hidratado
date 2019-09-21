from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='accounts/login')
def helloworld(request):
    return render(request, "pedidos/dashboard.html",{'greet': 'Hello world!'})