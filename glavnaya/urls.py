# -*- coding: utf-8 -*-

from django.urls import path
from . import views

urlpatterns = [
    path('veterinaria/', views.veterinaria, name='veterinaria'),
    path('', views.news, name='new'),
    path('news/', views.news, name='news'),
    path('news/<int:News_id>', views.new, name='new'),
    path('contacts.html', views.contacts, name='contacts'),
    path('abiturents/', views.abiturents, name='abiturents'),
    path('faq.html', views.faq, name='faq'),
    path('students/', views.students, name='students'),

]
