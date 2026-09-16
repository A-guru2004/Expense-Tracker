from django.urls import path
from . import views

urlpatterns = [
    path('', views.expenses_view, name='expenses'),
    path('edit/<int:pk>/', views.edit_expense, name='edit_expense'),
    path('delete/<int:pk>/', views.delete_expense, name='delete_expense'),
    path('export/', views.export_expense_excel, name='export_expense_excel'),
]
