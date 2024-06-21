from django.urls import path
from . import views

urlpatterns = [
    path('', views.about),
    path('menu', views.menu),
    path('contact', views.contact),
]
