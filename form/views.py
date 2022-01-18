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
