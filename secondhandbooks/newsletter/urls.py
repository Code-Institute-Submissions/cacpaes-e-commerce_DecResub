from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsletter, name='newsletter'),
    path('validate',
         views.validate_email,
         name='validate_email'),
]
