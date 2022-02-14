
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
    email=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=25)
    address=models.CharField(max_length=200)
    medium=models.CharField(max_length=40)
    requirements=models.TextField(max_length=800,null=True)
    Class=models.CharField(max_length=200)
    institution=models.CharField(max_length=200)


class AgentDataForm(models.Model):
    fName=models.CharField(max_length=200)
    lName=models.CharField(max_length=200)
    email=models.CharField(max_length=200,blank=True,null=True)
    phone=models.CharField(max_length=25,blank=True,null=True)
    country=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    webaddress=models.CharField(max_length=200,blank=True,null=True)
    whatsappnumber=models.CharField(max_length=25,blank=True,null=True)
    bestway=models.CharField(max_length=200,blank=True,null=True)
    agentType=models.CharField(max_length=40)


#Indivisual Agent
class IndivisualAgent(AgentDataForm):
    occupation=models.CharField(max_length=100)
    agentphoto=models.ImageField(upload_to='agentphotos')
    agentnid=models.FileField(upload_to='agentnID')
    academicCertificate=models.FileField(upload_to='academic')


class BusinessAgent(AgentDataForm):
    businessName=models.CharField(max_length=100)
    tradeNum=models.CharField(max_length=100)
    businessAddress=models.CharField(max_length=200)
    businessNum=models.CharField(max_length=25)
    businessemail=models.CharField(max_length=200)
    agentphoto=models.ImageField(upload_to='agentphotos')
    agentnid=models.FileField(upload_to='agentnID')
    tradelicense=models.FileField(upload_to='trade')
    tinbin=models.FileField(upload_to='tin')


class CommonForm(CommonFields):
    studyLevel=models.CharField(max_length=25)
    country=models.CharField(max_length=25)
    counselMode=models.CharField(max_length=25)
    

class AdmissionForm(CommonFields):
    profilephoto=models.ImageField(upload_to="AdmissionForm", default=None)
    passportno=models.CharField(max_length=40,blank=True,null=True)
    passportExpireDate=models.CharField(max_length=40,blank=True,null=True)
    nationality=models.CharField(max_length=40)
    nID_birthNumber=models.CharField(max_length=40)
    gender=models.CharField(max_length=40)
    dateofbirth=models.DateField()
    placeofbirth=models.CharField(max_length=40)
    maritalstatus=models.CharField(max_length=40)
    homeaddress=models.CharField(max_length=40)
    homephone=models.CharField(max_length=40)
    applyuniveristy=models.CharField(max_length=40)
    majorsub=models.CharField(max_length=40)
    profession=models.CharField(max_length=40)
    language=models.CharField(max_length=40)
    fathername=models.CharField(max_length=40)
    mothername=models.CharField(max_length=40)
    fatheremployement=models.CharField(max_length=40)
    motheremployement=models.CharField(max_length=40)
    fathernumber=models.CharField(max_length=40)
    mothernumber=models.CharField(max_length=40)
    academiccertificate=models.FileField(upload_to="AdmissionForm", default=None,blank=True,null=True)
    transcript=models.FileField(upload_to="AdmissionForm", default=None,blank=True,null=True)
    academiccertificate2=models.FileField(upload_to="AdmissionForm", default=None,blank=True,null=True)
    transcript2=models.FileField(upload_to="AdmissionForm", default=None,blank=True,null=True)
    academiccertificate3=models.FileField(upload_to="AdmissionForm", default=None,blank=True,null=True)
    transcript3=models.FileField(upload_to="AdmissionForm", default=None,blank=True,null=True)
    academiccertificate4=models.FileField(upload_to="AdmissionForm", default=None,blank=True,null=True)
    transcript4=models.FileField(upload_to="AdmissionForm", default=None,blank=True,null=True)
    academiccertificate5=models.FileField(upload_to="AdmissionForm", default=None,blank=True,null=True)
    transcript5=models.FileField(upload_to="AdmissionForm", default=None,blank=True,null=True)
    passportscan=models.FileField(upload_to="AdmissionForm", default=None,blank=True,null=True)
    nIDscan=models.FileField(upload_to="AdmissionForm", default=None,blank=True,null=True)
    bankstatement=models.FileField(upload_to="AdmissionForm", default=None,blank=True,null=True)
    recommendationletter=models.FileField(upload_to="AdmissionForm", default=None,blank=True,null=True)
    recommendationletter2=models.FileField(upload_to="AdmissionForm", default=None,blank=True,null=True)
    recommendationletter3=models.FileField(upload_to="AdmissionForm", default=None,blank=True,null=True)
    studyplan=models.FileField(upload_to="AdmissionForm", default=None,blank=True,null=True)
