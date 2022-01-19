from rest_framework import serializers

from form.models import *

<<<<<<< HEAD
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
        fields = ['id', 'fName', 'lName', 'email', 'phone','skill','country']



class BecomeTutorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = BecomeTutor
        fields = ['id', 'fName', 'lName', 'email', 'phone','skill','country' ]


class LookingTutorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = LookingTutor
        fields = ['id', 'fName', 'lName', 'email', 'phone','skill','country' ]


class AgentDataFormSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = AgentDataForm
        fields = ['id', 'fName', 'lName', 'email', 'phone','skill','country' ]


class BusinessAgentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = BusinessAgent
        fields = ['id', 'fName', 'lName', 'email', 'phone','skill','country' ]




=======

class SnippetSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Snippet
        fields = ['id', 'name', 'photo']
>>>>>>> 05a7b7f3179cb64f737e89aaaf86f47431f54670
