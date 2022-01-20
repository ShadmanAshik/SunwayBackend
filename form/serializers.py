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
        fields = ['id', 'name', 'email', 'phone','message']


class ScholarshipSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Scholarship
        fields = ['id', 'fName','lName','email','phone','studywhen','studycountry','counselMode','studyLevel']


class DevelopingSkillsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = DevelopingSkills
        fields = ['id', 'fName', 'lName', 'email', 'counselMode','phone','skill','country']


class LanguageProficiencySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = LanguageProficiency
        fields = ['id', 'fName', 'lName', 'email','phone', 'language','counselMode','country']
        
class BecomeTutorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = BecomeTutor
        fields = ['id', 'fName', 'lName', 'email','phone', 'address','city',
        'degreeobtained','EducationOrganization','EducationBackground',
        'gender','tuitionarea', ]


class LookingTutorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = LookingTutor
        fields = ['id', 'yourName', 'studentName', 'email', 'phone','address',
        'medium','requirements', 'Class', 'institution' ]


class AgentDataFormSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = AgentDataForm
        fields = ['id', 'fName', 'lName', 'email', 'phone']


class BusinessAgentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = BusinessAgent
        fields = ['id', 'fName', 'lName', 'email', 'phone' ]


class CommonSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = BusinessAgent
        fields = ['id', 'fName', 'lName', 'email', 'phone','studyLevel','counselMode','country' ]



