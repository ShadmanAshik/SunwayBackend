from rest_framework import serializers

from form.models import *


class SnippetSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Snippet
        fields = ['id', 'name', 'photo']



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


class ContactUsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = ContactUs
        fields = ['id', 'name', 'email', 'phone','message']

class DevelopingSkillsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = DevelopingSkills
        fields = ['id', 'fName','lName', 'email', 'phone','skill', 'counselMode', 'country']