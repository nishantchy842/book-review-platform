
from rest_framework import serializers
from book_review.models import UserModel
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id','name','password', 'email', 'role']

    def create(self, validated_data):
        # Hash the password before saving the user
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id','email','name']        
        
class UserLoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField( max_length=255)

    class Meta:
        model = UserModel
        fields = ['email', 'password']        