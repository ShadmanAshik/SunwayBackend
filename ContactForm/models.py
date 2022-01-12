from django.db import models


class ContactFormData(models.Model):
    fName=models.CharField(max_length=200)
    lName=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    countryCode=models.CharField(max_length=5)
    phone=models.CharField(max_length=15)
    counselingMode=models.CharField(max_length=20)
    studyLevel=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.email
    