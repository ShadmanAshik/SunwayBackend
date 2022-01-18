from distutils.command.upload import upload
from turtle import mode

from django.db import models


class AgentDataForm(models.Model):
    agentType=models.CharField(max_length=200)
    fName=models.CharField(max_length=200)
    lName=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    websiteaddress=models.CharField(max_length=200)
    bestway=models.CharField(max_length=200)
    agentphoto=models.ImageField(upload_to='agentphotos')



class Snippet(models.Model):
    name = models.CharField(max_length=10, default=None, blank=True, null=True)
    photo = models.FileField(upload_to="snippets", default=None, null=True)


