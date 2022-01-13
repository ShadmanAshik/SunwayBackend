from django.db import models
from django.db import models


class FormBase(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    
    class Meta:
        abstract=True



#contactform model
class ComonDataForm(FormBase):
    fName=models.CharField(max_length=200)
    lName=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    countryCode=models.CharField(max_length=5)
    phone=models.CharField(max_length=15)
    counselingMode=models.CharField(max_length=20)
    studyLevel=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    
    


class ContactUsForm(FormBase):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    message=models.TextField()



class AgentDataForm(models.Model):
    agentType=models.CharField(max_length=200)

