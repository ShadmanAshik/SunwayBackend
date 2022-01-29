from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from users.models import *
from users.permissions import *

from form.models import *
from form.serializers import *

# class SnippetView(APIView):
#     authentication_classes = [TokenAuthentication] 
#     permission_classes = [IsAuthenticated,IsAdmin]

#     def post(self, request):
#         snippet = SnippetSerializer(data=request.data)
#         if snippet.is_valid():
#             snippet.save()
#             return Response(snippet.data, status=status.HTTP_201_CREATED)
        
#         return Response(snippet.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def get(self, request):
#         snippets = SnippetSerializer(Snippet.objects.all(), many=True) 
#         return Response(snippets.data, status = status.HTTP_201_CREATED)


class ContactUsGetView(APIView):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated,IsAdmin]

    def get(self, request):
        ContactUss =ContactUsSerializer(ContactUs.objects.all(), many=True) 
        return Response(ContactUss.data, status = status.HTTP_200_OK)


class ContactUsPostView(APIView):
    authentication_classes = [] 
    permission_classes = []
    def post(self, request):
        ContactUs = ContactUsSerializer(data=request.data)
        if ContactUs.is_valid():
            ContactUs.save()
            return Response(ContactUs.data, status=status.HTTP_201_CREATED)
        
        return Response(ContactUs.errors, status=status.HTTP_400_BAD_REQUEST)


class ScholarshipPostView(APIView):
    authentication_classes = [] 
    permission_classes = []

    def post(self, request):
        Scholarship = ScholarshipSerializer(data=request.data)
        if Scholarship.is_valid():
            Scholarship.save()
            return Response(Scholarship.data, status=status.HTTP_201_CREATED)
        
        return Response(Scholarship.errors, status=status.HTTP_400_BAD_REQUEST)


class ScholarshipGetView(APIView):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated,IsAdmin]    
    def get(self, request):
        Scholarshipss =ScholarshipSerializer(Scholarship.objects.all(), many=True) 
        return Response(Scholarshipss.data, status = status.HTTP_201_CREATED)


class DevelopingSkillsPostView(APIView):
    authentication_classes = [] 
    permission_classes = []

    def post(self, request):
        DevelopingSkills = DevelopingSkillsSerializer(data=request.data)
        if DevelopingSkills.is_valid():
            DevelopingSkills.save()
            return Response(DevelopingSkills.data, status=status.HTTP_201_CREATED)
        
        return Response(DevelopingSkills.errors, status=status.HTTP_400_BAD_REQUEST)


class DevelopingSkillsGetView(APIView):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated,IsAdmin]    
    def get(self, request):
        DevelopingSkillss =DevelopingSkillsSerializer(DevelopingSkills.objects.all(), many=True) 
        return Response(DevelopingSkillss.data, status = status.HTTP_201_CREATED)


class LanguageProficiencyPostView(APIView):
    authentication_classes = [] 
    permission_classes = []

    def post(self, request):
        LanguageProficiency = LanguageProficiencySerializer(data=request.data)
        if LanguageProficiency.is_valid():
            LanguageProficiency.save()
            return Response(LanguageProficiency.data, status=status.HTTP_201_CREATED)
        
        return Response(LanguageProficiency.errors, status=status.HTTP_400_BAD_REQUEST)

class LanguageProficiencyGetView(APIView):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated,IsAdmin]
    
    def get(self, request):
        LanguageProficiencyy =LanguageProficiencySerializer(LanguageProficiency.objects.all(), many=True) 
        return Response(LanguageProficiencyy.data, status = status.HTTP_201_CREATED)



class BecomeTutorPostView(APIView):
    authentication_classes = [] 
    permission_classes = []

    def post(self, request):
        BecomeTutor= BecomeTutorSerializer(data=request.data)
        if BecomeTutor.is_valid():
            BecomeTutor.save()
            return Response(BecomeTutor.data, status=status.HTTP_201_CREATED)
        
        return Response(BecomeTutor.errors, status=status.HTTP_400_BAD_REQUEST)


class BecomeTutorGetView(APIView):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated,IsAdmin]
    def get(self, request):
        BecomeTutors =BecomeTutorSerializer(BecomeTutor.objects.all(), many=True) 
        return Response(BecomeTutors.data, status = status.HTTP_201_CREATED)


class LookingTutorPostView(APIView):
    authentication_classes = [] 
    permission_classes = []

    def post(self, request):
        LookingTutor = LookingTutorSerializer(data=request.data)
        if LookingTutor.is_valid():
            LookingTutor.save()
            return Response(LookingTutor.data, status=status.HTTP_201_CREATED)
        
        return Response(LookingTutor.errors, status=status.HTTP_400_BAD_REQUEST)


class LookingTutorGetView(APIView):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated,IsAdmin]
    def get(self, request):
        LookingTutors =LookingTutorSerializer(LookingTutor.objects.all(), many=True) 
        return Response(LookingTutors.data, status = status.HTTP_201_CREATED)


class AgentDataFormPostView(APIView):
    authentication_classes = [] 
    permission_classes = []

    def post(self, request):
        agent_serializer = IndivisualAgentSerializer(data=request.data)
        if agent_serializer.is_valid():
            agent_serializer.save()
            return Response(agent_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(agent_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AgentDataFormGetView(APIView):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated,IsAdmin]    
    def get(self, request):
        AgentDataForms =AgentDataFormSerializer(AgentDataForm.objects.all(), many=True) 
        return Response(AgentDataForms.data, status = status.HTTP_201_CREATED)


class BusinessAgentPostView(APIView):
    authentication_classes = [] 
    permission_classes = []

    def post(self, request):
        BusinessAgent = BusinessAgentSerializer(data=request.data)
        if BusinessAgent.is_valid():
            BusinessAgent.save()
            return Response(BusinessAgent.data, status=status.HTTP_201_CREATED)
        
        return Response(BusinessAgent.errors, status=status.HTTP_400_BAD_REQUEST)


class BusinessAgentGetView(APIView):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated,IsAdmin]
    def get(self, request):
        BusinessAgents =BusinessAgentSerializer(BusinessAgent.objects.all(), many=True) 
        return Response(BusinessAgents.data, status = status.HTTP_201_CREATED)


class CommonFormPostView(APIView):
    authentication_classes = [] 
    permission_classes = []

    def post(self, request):
        CommonForm = CommonFormSerializer(data=request.data)
        if CommonForm.is_valid():
            CommonForm.save()
            return Response(CommonForm.data, status=status.HTTP_201_CREATED)
        
        return Response(CommonForm.errors, status=status.HTTP_400_BAD_REQUEST)


class CommonFormGetView(APIView):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated,IsAdmin]
    def get(self, request):
        CommonForms =CommonFormSerializer(CommonForm.objects.all(), many=True) 
        return Response(CommonForms.data, status = status.HTTP_201_CREATED)


class AdmissionFormPostView(APIView):
    authentication_classes = [] 
    permission_classes = []

    def post(self, request):
        AdmissionForm = AdmissionFormSerializer(data=request.data)
        if AdmissionForm.is_valid():
            AdmissionForm.save()
            return Response(AdmissionForm.data, status=status.HTTP_201_CREATED)
        
        return Response(AdmissionForm.errors, status=status.HTTP_400_BAD_REQUEST)


class AdmissionFormGetView(APIView):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated,IsAdmin]
    def get(self, request):
        AdmissionForms =AdmissionFormSerializer(AdmissionForm.objects.all(), many=True) 
        return Response(AdmissionForms.data, status = status.HTTP_201_CREATED)
