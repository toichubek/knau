from django.shortcuts import render
from django.http import Http404
from django.template import *
from .models import Vet, Sylka_vet, Videos
from glavnaya.models import Address
# Create your views here.

def vet(request, vet_item_id):
    vet_url = "active"
    ADDRESS= Address.objects.all()
    vet_list = Vet.objects.order_by("order")
    silka_list = Sylka_vet.objects.order_by("order")
    try:
       vet_item = Vet.objects.get(pk=vet_item_id)
    except Vet.DoesNotExist:
       raise Http404("Извините, такой страницы не существует!")
    return render(request, 'veterinaria/vet.html', locals())




def video(request):
    video_url = "active"
    ADDRESS = Address.objects.all()
    videos = Videos.objects.order_by('album')
    vet_list = Vet.objects.order_by("order")
    silka_list = Sylka_vet.objects.order_by("order")

    return render(request, 'veterinaria/video.html', locals())

