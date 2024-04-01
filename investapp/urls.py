from django.urls import path
from . import views

urlpatterns = [
    path('accounts/profile/', views.index, name='index'),
]