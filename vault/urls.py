from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_password, name='add_password'),
    path('passwords/', views.password_list, name='password_list'),
    path('edit/<int:pk>/', views.edit_password, name='edit_password'),
    path('delete/<int:pk>/', views.delete_password, name='delete_password'),



]
