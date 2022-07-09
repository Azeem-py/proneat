from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class CreateUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = User

        fields = ('id','username', 'email', 'password', 'password2')
        extra_kwargs = {
            'username': {
                'required': False, 
                'validators': [UniqueValidator(User.objects.all(), "user is not available"),]
            },
            'email':{
                'required': True, 
                'validators': [UniqueValidator(User.objects.all(), "user is not available"),]
            },
            'password':{
                'required': True, 'write_only': True,
                'validators': [validate_password,]
            },
        }
        
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields don't match"})
        return attrs

    def create(self, validated_data):
        password, _ = (validated_data.pop('password'), validated_data.pop('password2'))
        validated_data['username'] = validated_data['email']
        user = User.objects.create(**validated_data)
        user.set_password(raw_password=password)
        user.save()
        return user
