# -*- coding: utf-8 -*-

from django.urls import path, include
from . import views

urlpatterns = [
    path('veterinaria/video.html', views.video, name='videos'),
    path('veterinaria/<str:vet_item_id>', views.vet, name='vet_item'),

]
