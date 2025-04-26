from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'phone_number', 'password', 'confirm_password', 'image']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError({"confirm_password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        confirm_password = validated_data.pop('confirm_password')
        user = User(**validated_data)
        user.confirm_password = confirm_password  
        user.save()
        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email', 'phone_number', 'image','confirm_password','password']