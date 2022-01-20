# from distutils.command.upload import upload
# from re import L
# from turtle import mode

from django.db import models

# class Snippet(models.Model):
#     name = models.CharField(max_length=10, default=None, blank=True, null=True)
#     photo = models.FileField(upload_to="snippets", default=None, null=True)



class CommonFields(models.Model):
    fName=models.CharField(max_length=200)
    lName=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=25)


class ContactUs(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    message=models.TextField(max_length=1000)
    phone=models.CharField(max_length=25)
    


class Scholarship(CommonFields):
    studywhen=models.CharField(max_length=100)
    studycountry=models.CharField(max_length=100)
    counselMode=models.CharField(max_length=40)
    studyLevel=models.CharField(max_length=40)



class LanguageProficiency(CommonFields):
    counselMode=models.CharField(max_length=40)
    language=models.CharField(max_length=40)
    country=models.CharField(max_length=40)


class DevelopingSkills(CommonFields):
    counselMode=models.CharField(max_length=40)
    skill=models.CharField(max_length=40)
    country=models.CharField(max_length=40)



class BecomeTutor(CommonFields):
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    degreeobtained=models.CharField(max_length=70)
    EducationOrganization=models.CharField(max_length=70)
    EducationBackground=models.CharField(max_length=70)
    gender=models.CharField(max_length=40)
    tuitionarea=models.CharField(max_length=200)
    password=models.CharField(max_length=40)
    confirmpassword=models.CharField(max_length=40)



class LookingTutor(models.Model):
    yourName=models.CharField(max_length=200)
    studentName=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=25)
    address=models.CharField(max_length=200)
    medium=models.CharField(max_length=40)
    requirements=models.TextField(max_length=800)
    Class=models.CharField(max_length=200)
    institution=models.CharField(max_length=200)


#Indivisual Agent
class AgentDataForm(CommonFields):
    country=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    websiteaddress=models.CharField(max_length=200)
    bestway=models.CharField(max_length=200)
    agentphoto=models.ImageField(upload_to='agentphotos')
    nID=models.FileField(upload_to='agentnID')
    passport=models.FileField(upload_to='agentnPassport')


class BusinessAgent(AgentDataForm):
    businessNum=models.CharField(max_length=25)
    businessemail=models.CharField(max_length=200)
    businessAddress=models.CharField(max_length=200)


class CommonForm(CommonFields):
    studyLevel=models.CharField(max_length=25)
    country=models.CharField(max_length=25)
    counselMode=models.CharField(max_length=25)
    