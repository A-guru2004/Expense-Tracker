import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from income.models import Income
from expenses.models import Expense


@login_required
def dashboard_view(request):
    total_income = Income.objects.filter(user=request.user).aggregate(total=Sum('amount'))['total'] or 0
    total_expenses = Expense.objects.filter(user=request.user).aggregate(total=Sum('amount'))['total'] or 0
    balance = total_income - total_expenses

    recent_income = Income.objects.filter(user=request.user).order_by('-date')[:5]
    recent_expenses = Expense.objects.filter(user=request.user).order_by('-date')[:5]

    # ---- Pie chart data: Income vs Expenses ----
    pie_labels = json.dumps(['Income', 'Expenses'])
    pie_totals = json.dumps([float(total_income), float(total_expenses)])

    context = {
        'total_income': total_income,
        'total_expenses': total_expenses,
        'balance': balance,
        'recent_income': recent_income,
        'recent_expenses': recent_expenses,
        'pie_labels': pie_labels,
        'pie_totals': pie_totals,
    }
    return render(request, 'dashboard/dashboard.html', context)
