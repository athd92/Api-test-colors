from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from .serializers import ColorsSerializer
from django.core import serializers
from .models import Colors

class ColorsViewSet(viewsets.ModelViewSet):
    
    queryset = Colors.objects.all()
    serializer_class = ColorsSerializer
    pagination_class = PageNumberPagination
