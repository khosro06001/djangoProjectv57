from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('ticketmaster/', views.ticketmaster, name="ticketmaster"),
    path('', views.ticketmaster, name="ticketmaster"),

]
