from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.query, name='querybb-home'),
]