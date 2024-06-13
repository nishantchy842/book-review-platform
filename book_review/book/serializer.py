from rest_framework import serializers
from book_review.models import Books, Review
from book_review.user.serializer import AuthorSerializer
from datetime import date


class BookSerializer(serializers.ModelSerializer):
    created_by = AuthorSerializer(read_only=True)
    

    class Meta:
        model = Books
        fields = '__all__'
        
class CreateBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = ['title', 'author', 'published_date', 'isbn', 'pages', 'language']  # Corrected field name

    def validate_isbn(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("ISBN should be numeric.")
        if len(value) not in [10, 13]:
            raise serializers.ValidationError("ISBN should be either 10 or 13 digits long.")
        return value

    def validate_published_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Published date cannot be in the future.")
        return value

    def create(self, validated_data):
        request = self.context.get('request')
        if not request or not hasattr(request, 'user'):
            raise serializers.ValidationError("Request context is missing or invalid.")
        author = request.user
        author = request.user  # Assuming the author is the logged-in user
        book = Books.objects.create(created_by=author, **validated_data)
        return book
   
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'