from django.urls import path
from . import views

urlpatterns = [
    path('factorial2/', views.factorial2, name='factorial2'),
]