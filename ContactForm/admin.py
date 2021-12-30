from django.contrib import admin
from .models import ContactFormData


class ContactFormDataAdmin(admin.ModelAdmin):
    list_display=['fName', 'lName', 'email', 
    'countryCode', 'phone','studyLevel','country','counselingMode']
admin.site.register(ContactFormData,ContactFormDataAdmin )
# Register your models here.
