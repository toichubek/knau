# -*- coding: utf-8 -*-

from django.urls import path, include
from . import views


urlpatterns = [
    path('abiturents/documents.html', views.documents, name="documents"),
    path('abiturents/<str:item_id>', views.abit, name='abit_item'),

]
