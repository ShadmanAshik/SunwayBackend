from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated

from .models import ContactFormData
from .serializers import ContactFormDataSerializer


class IsAgent(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_agent

class ContactFormDataViewSet(viewsets.ModelViewSet):
    authentication_classes = [] 
    permission_classes = []

    queryset=ContactFormData.objects.all().order_by('-id')
    serializer_class=ContactFormDataSerializer
    