from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from pyexpat import model
from rest_framework import serializers

from users.models import *


class UserRegisterSerializer(UserCreateSerializer):
    re_password = serializers.CharField(style={"input_type": "password"}, write_only=True, max_length=100)
    phone = serializers.CharField(style={"input_type": "text"}, write_only=True, max_length=15)

    def create(self, validate_data):
        print(f'Create Validate Data {validate_data}')
        is_agent = validate_data.pop('is_agent', False)
        is_student = validate_data.pop('is_student', False)
        user = super().create(validate_data)
        if is_agent:
            user.is_agent = True 
            Agent.objects.create(user=user)
            
        elif is_student:
            user.is_student = True 
            Student.objects.create(user=user,phone=self.phone)
        user.save()

        return user 
    
    def validate(self, attrs):
        print(f' validate  {attrs}')
        re_password = attrs.get('re_password')
        password = attrs.get('password')
        if re_password != password:
            raise serializers.ValidationError({'re_password': "Passwords Don't Match"})
        
        attrs.pop('re_password')
        self.phone=attrs.pop('phone','')
        return super().validate(attrs)
    
    class Meta(UserCreateSerializer.Meta):
        fields = ['name', 'email', 'is_agent', 'password', 're_password', 'is_student','phone']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'name', 'email',  'is_agent', 'is_student','is_admin']
