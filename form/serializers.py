# from dataclasses import fields

from rest_framework import serializers

from form.models import *

# class SnippetSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     class Meta:
#         model = Snippet
#         fields = ['id', 'name', 'photo']



class ContactUsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = ContactUs
        fields ='__all__'


class ScholarshipSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Scholarship
        fields ='__all__'


class DevelopingSkillsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = DevelopingSkills
        fields ='__all__'


class LanguageProficiencySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = LanguageProficiency
        fields ='__all__'
        
class BecomeTutorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = BecomeTutor
        fields ='__all__'


class LookingTutorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = LookingTutor
        fields ='__all__'


# class AgentDataFormSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     class Meta:
#         model = AgentDataForm
#         fields = ['id', 'fName', 'lName', 'email', 'phone']

class IndivisualAgentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = IndivisualAgent
        fields ='__all__'
 
    
class BusinessAgentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = BusinessAgent
        fields ='__all__'


class CommonFormSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = CommonForm
        fields ='__all__'


class AdmissionFormSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = AdmissionForm
        fields ='__all__'




