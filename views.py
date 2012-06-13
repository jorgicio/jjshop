from django.shortcuts import render_to_response

def home(request):
	return render_to_response('index.html')

from models import Productos

def catalogo(request):
	cata = Productos.objects.using('remota').all()
	return render_to_response('catalogo.html',{'Catalogo':cata})
