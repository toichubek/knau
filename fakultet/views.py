from django.shortcuts import render
from django.http import Http404
from django.template import *
from .models import Sotrudnik,Sotrudnik_dekanat, Kafedra, History, Manager, Gallery, GalleryImage #  Link_to_univer
from glavnaya.models import Address
# Create your views here.

def team(request):
    team_url = "active"
    ADDRESS= Address.objects.all()
    sotrudnik = Sotrudnik.objects.all()
    kafedra = Kafedra.objects.all()
    return render(request, 'fakultet/team.html', locals())

def sotrudnik(request):
    sotrudnik_url = "active"
    ADDRESS= Address.objects.all()
    sotrudnik = Sotrudnik_dekanat.objects.all()
    return render(request, 'fakultet/sotrudnik.html', locals())

def istoria(request):
    istoria_url = "active"
    post = History.objects.all()
    ADDRESS= Address.objects.all()

    return render(request, 'fakultet/istoria.html', locals())

def departments(request):
    departments_url = "active"
    departments_all = Kafedra.objects.all()
    ADDRESS= Address.objects.all()

    return render(request, 'fakultet/departments.html', locals())

def department(request, Department_name):
    try:
        department_n=Kafedra.objects.get(pk=Department_name)
    except Kafedra.DoesNotExist:
        raise Http404("Извините, такой страницы не существует!")
    ADDRESS= Address.objects.all()
    return render(request, 'fakultet/department.html', {'department_url': "active", 'department': department_n, 'ADDRESS': ADDRESS})

def management(request):
    management_url = "active"
    manager = Manager.objects.all()
    ADDRESS= Address.objects.all()

    return render(request, 'fakultet/management.html', locals())


def gallery(request):
    gallery_url = "active"
    ADDRESS= Address.objects.all()
    image = GalleryImage.objects.order_by('album')
    return render(request, 'fakultet/gallery.html', locals())


def uch_plan(request):
    uch_plan_url = "active"
    ADDRESS= Address.objects.all()

    return render(request, 'fakultet/uch_plan.html', locals())
