from django.shortcuts import render
from rest_framework import viewsets
from .models import Expense
from .serializers import ExpenseSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
