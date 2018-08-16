from django.shortcuts import render
from django.http import Http404
from django.template import *
from .models import New, Sylka, Address, Faq
from abiturents.models import Abiturents, Abit, Sylka_abit
from veterinaria.models import Vet, Sylka_vet

# Create your views here.


def veterinaria(request):
    veterinaria_url = "active"
    ADDRESS = Address.objects.all()
    Silka = Sylka.objects.order_by('id')
    path=request.path
    vet_list = Vet.objects.order_by("order")
    silka_list = Sylka_vet.objects.order_by("order")

    return render(request, 'glavnaya/veterinaria.html', locals())

def news(request):
    news_url = "active"
    ADDRESS= Address.objects.all()
    news_all=New.objects.order_by('-published')
    return render(request, 'glavnaya/news.html', locals())

def new(request, News_id):
    try:
        new_n=New.objects.get(pk=News_id)
    except New.DoesNotExist:
        raise Http404("Извините, такой страницы не существует!")
    ADDRESS= Address.objects.all()
    return render(request, 'glavnaya/new.html', {'new_url': "active",'new': new_n, 'ADDRESS': ADDRESS})

def contacts(request):
    silka_list = Sylka.objects.order_by("order")
    contacts_url = "active"
    ADDRESS = Address.objects.all()
    return render(request, 'glavnaya/contacts.html', locals())

def faq(request):
    silka_list = Sylka.objects.order_by("order")
    faq_url = "active"
    faqs=Faq.objects.all()
    ADDRESS= Address.objects.all()

    return render(request, 'glavnaya/faq.html', locals())

def abiturents(request):
    abiturents_url = "active"
    ADDRESS= Address.objects.all()
    abiturent_info = Abiturents.objects.all()
    abit_list = Abit.objects.order_by("order")
    silka_list = Sylka_abit.objects.order_by("order")
    return render(request, 'glavnaya/abiturents.html', locals())

def students(request):
    students_url = "active"
    ADDRESS= Address.objects.all()
    return render(request, 'glavnaya/students.html', locals())
