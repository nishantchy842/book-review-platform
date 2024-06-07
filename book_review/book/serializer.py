from rest_framework import serializers
from book_review.models import Book, Review
from book_review.user.serializer import userSerializers


class BookSerializer(serializers.ModelSerializer):
    created_by = userSerializers(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'