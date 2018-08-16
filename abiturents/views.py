from django.shortcuts import render, redirect
from django.http import Http404
from django.template import *
from .models import Documents, Abit, Sylka_abit
from glavnaya.models import Address

# Create your views here.

def abit(request, item_id):
    ADDRESS= Address.objects.all()
    abit_list = Abit.objects.order_by("order")
    silka_list = Sylka_abit.objects.order_by("order")
    abit_url = "active"
    try:
        abit_item = Abit.objects.get(pk=item_id)
    except Abit.DoesNotExist:
       raise Http404("Извините, такой страницы не существует!")
    return render(request, 'abiturents/abit_pages.html', locals())

def documents(request):
    documents_url = "active"
    ADDRESS= Address.objects.all()
    docs = Documents.objects.all()
    abit_list = Abit.objects.order_by("order")
    silka_list = Sylka_abit.objects.order_by("order")
    return render(request, 'abiturents/documents.html', locals())

