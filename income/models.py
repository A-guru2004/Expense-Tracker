from django.db import models
from django.contrib.auth.models import User


class Income(models.Model):
    SOURCE_CHOICES = [
        ('salary', 'Salary'),
        ('business', 'Business'),
        ('freelance', 'Freelance'),
        ('investment', 'Investment'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incomes')
    source = models.CharField(max_length=50, choices=SOURCE_CHOICES, default='other')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    notes = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.source} - {self.amount} ({self.user.username})"
