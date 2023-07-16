from django.urls import path

from catalog import views
from catalog.views import home

urlpatterns = [
    path('', home),
    path('contacts/', views.contacts, name='contacts')

    ]