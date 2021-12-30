from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContactFormDataSerializer
from .models import ContactFormData

class ContactFormDataViewSet(viewsets.ModelViewSet):
    queryset=ContactFormData.objects.all().order_by('-id')
    serializer_class=ContactFormDataSerializer
    