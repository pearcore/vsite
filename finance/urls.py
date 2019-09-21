from django.urls import path

from . import views
app_name = 'finance'

urlpatterns = [
    path('typelist', views.typelist , name= 'typelist'),
    path('typedelete', views.typedelete , name= 'typelist'),
]