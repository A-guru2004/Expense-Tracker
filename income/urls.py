from django.urls import path
from . import views

urlpatterns = [
    path('', views.income_view, name='income'),
    path('edit/<int:pk>/', views.edit_income, name='edit_income'),
    path('delete/<int:pk>/', views.delete_income, name='delete_income'),
    path('export/', views.export_income_excel, name='export_income_excel'),
]
