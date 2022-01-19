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
<<<<<<< HEAD


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



class BecomeTutorView(APIView):
    authentication_classes = [] 
    permission_classes = []

    def post(self, request):
        BecomeTutor= BecomeTutorSerializer(data=request.data)
        if BecomeTutor.is_valid():
            BecomeTutor.save()
            return Response(BecomeTutor.data, status=status.HTTP_201_CREATED)
        
        return Response(BecomeTutor.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        BecomeTutors =BecomeTutorSerializer(BecomeTutor.objects.all(), many=True) 
        return Response(BecomeTutors.data, status = status.HTTP_201_CREATED)


class LookingTutorView(APIView):
    authentication_classes = [] 
    permission_classes = []

    def post(self, request):
        LookingTutor = LookingTutorSerializer(data=request.data)
        if LookingTutor.is_valid():
            LookingTutor.save()
            return Response(LookingTutor.data, status=status.HTTP_201_CREATED)
        
        return Response(LookingTutor.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        LookingTutors =LookingTutorSerializer(LookingTutor.objects.all(), many=True) 
        return Response(LookingTutors.data, status = status.HTTP_201_CREATED)


class AgentDataFormView(APIView):
    authentication_classes = [] 
    permission_classes = []

    def post(self, request):
        AgentDataForm = AgentDataFormSerializer(data=request.data)
        if AgentDataForm.is_valid():
            AgentDataForm.save()
            return Response(AgentDataForm.data, status=status.HTTP_201_CREATED)
        
        return Response(AgentDataForm.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        AgentDataForms =AgentDataFormSerializer(AgentDataForm.objects.all(), many=True) 
        return Response(AgentDataForms.data, status = status.HTTP_201_CREATED)


class BusinessAgentiew(APIView):
    authentication_classes = [] 
    permission_classes = []

    def post(self, request):
        BusinessAgent = BusinessAgentSerializer(data=request.data)
        if BusinessAgent.is_valid():
            BusinessAgent.save()
            return Response(BusinessAgent.data, status=status.HTTP_201_CREATED)
        
        return Response(BusinessAgent.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        BusinessAgents =BusinessAgentSerializer(BusinessAgent.objects.all(), many=True) 
        return Response(BusinessAgents.data, status = status.HTTP_201_CREATED)
=======
>>>>>>> 05a7b7f3179cb64f737e89aaaf86f47431f54670
