from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from form.models import *
from form.serializers import *


class SnippetView(APIView):
    authentication_classes = [] 
    permission_classes = []

    def post(self, request):
        snippet = SnippetSerializer(data=request.data)
        if snippet.is_valid():
            snippet.save()
            return Response(snippet.data, status=status.HTTP_201_CREATED)
        
        return Response(snippet.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        snippets = SnippetSerializer(Snippet.objects.all(), many=True) 
        return Response(snippets.data, status = status.HTTP_201_CREATED)


class ContactUsView(APIView):
    authentication_classes = [] 
    permission_classes = []

    def post(self, request):
        ContactUs = ContactUsSerializer(data=request.data)
        if ContactUs.is_valid():
            ContactUs.save()
            return Response(ContactUs.data, status=status.HTTP_201_CREATED)
        
        return Response(ContactUs.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        ContactUss =ContactUsSerializer(ContactUs.objects.all(), many=True) 
        return Response(ContactUss.data, status = status.HTTP_201_CREATED)


class ScholarshipView(APIView):
    authentication_classes = [] 
    permission_classes = []

    def post(self, request):
        Scholarship = ScholarshipSerializer(data=request.data)
        if Scholarship.is_valid():
            Scholarship.save()
            return Response(Scholarship.data, status=status.HTTP_201_CREATED)
        
        return Response(Scholarship.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        Scholarshipss =ScholarshipSerializer(Scholarship.objects.all(), many=True) 
        return Response(Scholarshipss.data, status = status.HTTP_201_CREATED)

class DevelopingSkillsView(APIView):
    authentication_classes = [] 
    permission_classes = []

    def post(self, request):
        DevelopingSkills = DevelopingSkillsSerializer(data=request.data)
        if DevelopingSkills.is_valid():
            DevelopingSkills.save()
            return Response(DevelopingSkills.data, status=status.HTTP_201_CREATED)

        return Response(DevelopingSkills.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        DevelopingSkillss =DevelopingSkillsSerializer(DevelopingSkills.objects.all(), many=True) 
        return Response(DevelopingSkillss.data, status = status.HTTP_201_CREATED)

class LanguageProficiencyView(APIView):
    authentication_classes = [] 
    permission_classes = []

    def post(self, request):
        LanguageProficiency = LanguageProficiencySerializer(data=request.data)
        if LanguageProficiency.is_valid():
            LanguageProficiency.save()
            return Response(LanguageProficiency.data, status=status.HTTP_201_CREATED)

        return Response(LanguageProficiency.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        LanguageProficiencyy =LanguageProficiencySerializer(LanguageProficiency.objects.all(), many=True) 
        return Response(LanguageProficiencyy.data, status = status.HTTP_201_CREATED)
