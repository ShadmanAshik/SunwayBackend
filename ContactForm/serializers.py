from django.db.models import fields
from rest_framework import serializers
from .models import ContactFormData
class ContactFormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactFormData
        fields=('id','fName', 'lName', 'email', 
        'countryCode', 'phone','country','studyLevel','counselingMode' )