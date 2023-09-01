from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='home'),
    path('', views.index, name='home'),
    path('<int:my_id>/update', views.update, name="update"),
    path('<int:my_id>/delete', views.delete, name="delete"),
]