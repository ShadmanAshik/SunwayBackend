from rest_framework import serializers

from editor.models import *


class RichEditorSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = RichEditor
        fields ='__all__'
