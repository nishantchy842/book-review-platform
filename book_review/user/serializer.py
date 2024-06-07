
from rest_framework import serializers
from book_review.models import UserModel

class userSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = UserModel
        fields = '__all__'
        extra_kwargs={
            'password':{
                'write_only': True
            }
        }
        
        
class UserLoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField( max_length=255)

    class Meta:
        model = UserModel
        fields = ['email', 'password']        