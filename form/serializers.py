from rest_framework import serializers

from form.models import *


class SnippetSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Snippet
        fields = ['id', 'name', 'photo']
