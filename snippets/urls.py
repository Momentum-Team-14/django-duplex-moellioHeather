from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_albums, name='list_albums'),
