# -*- coding: utf-8 -*-

from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('fakultet/team.html', views.team, name='team'),
    path('fakultet/sotrudnik.html', views.sotrudnik, name='sotrudnik'),
    path('fakultet/istoria.html', views.istoria, name="istoria"),
    path('fakultet/gallery.html', views.gallery, name="gallery"),
    path('fakultet/departments.html', views.departments, name="departments"),
    path('fakultet/management.html', views.management, name="management"),
    path('fakultet/departments/<int:Department_name>/', views.department, name='department'),
    path('uch_plan.html', views.uch_plan, name="uch_plan"),

]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

