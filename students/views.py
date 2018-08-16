from django.shortcuts import render
from django.http import Http404
from django.template import *
from .models import Doc,  Stud, Sylka_stud
from glavnaya.models import Address
# Create your views here.

def doc_students(request):
    doc_students_url = "active"
    docs = Doc.objects.all()
    ADDRESS= Address.objects.all()
    student_list = Stud.objects.order_by("order")
    silka_list = Sylka_stud.objects.order_by("order")

    return render(request, 'students/doc_students.html', locals())

def students(request, item_id):
    students_url = "active"
    ADDRESS= Address.objects.all()
    student_list = Stud.objects.order_by("order")
    silka_list = Sylka_stud.objects.order_by("order")
    try:
        stud_item = Stud.objects.get(pk=item_id)
    except Stud.DoesNotExist:
       raise Http404("Извините, такой страницы не существует!")

    return render(request, 'students/student_pages.html', locals())