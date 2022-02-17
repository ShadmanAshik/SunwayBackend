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




