# -*- coding: utf-8 -*-

from django.urls import path, include
from . import views

urlpatterns = [
    path('students/doc_students.html', views.doc_students, name="doc_students"),
    path('students/<str:item_id>', views.students, name='stud_item'),
]
