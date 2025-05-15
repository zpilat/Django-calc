from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('factorial/', views.factorial_modal, name='factorial_modal'),
    path('factorial/result/', views.calc_factorial, name='factorial_result'),
]
