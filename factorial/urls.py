from django.urls import path
from . import views

urlpatterns = [
    path('factorial/', views.factorial, name='factorial'),
    path('factorial/result/', views.calc_factorial, name='factorial_result'),
]
