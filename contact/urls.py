from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.contact),
    path('about', views.contact_about)
]
