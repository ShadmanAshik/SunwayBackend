from multiprocessing import AuthenticationError
from multiprocessing.sharedctypes import Value

from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from users.permissions import *

from editor.serializers import *


class RichEditorView(APIView):
    authentication_classes = [] 
    permission_classes = []


# TokenAuthentication
# IsAuthenticated,IsAdmin
    def post(self, request):
        RichEditor = RichEditorSerializers(data=request.data)
        if RichEditor.is_valid():
            RichEditor.save()
            return Response(RichEditor.data, status=status.HTTP_201_CREATED)
        
        return Response(RichEditor.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):

        RichEditors=RichEditorSerializers(RichEditor.objects.last())        
        return Response(RichEditors.data, status = status.HTTP_201_CREATED)

class EnglishSpokenEditorGetView(APIView):
    authentication_classes = [] 
    permission_classes = []
    def get(self, request):
        list=[]
        contents=RichEditorSerializers(RichEditor.objects.all())
        
        for content in contents:
            if content.data.pgName == "English Spoken":
                list.append(content)                
        es=list.pop()            
        return Response(es.data, status = status.HTTP_201_CREATED)




        RichEditors=RichEditorSerializers(RichEditor.objects.last())
        return Response(RichEditors.data, status = status.HTTP_201_CREATED)

from rest_framework import generics


class RichEditorGen(generics.ListCreateAPIView):
    serializer_class = RichEditorSerializers
    queryset = RichEditor.objects.all()
    permission_classes = [] 
    authentication_classes = [] 

    def get_queryset(self):
        return RichEditor.objects.filter(title__icontains="Sagor")

    def post(self, request, *args, **kwargs):
        if not str(request.user.__class__) == 'AnonymousUser' and  request.user.is_admin:
            print("Passes")
        else:
            raise ValueError 
        return super().post(request, *args, **kwargs) 
