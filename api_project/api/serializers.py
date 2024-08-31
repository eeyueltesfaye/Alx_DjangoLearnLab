from .models import Book 
from rest_framework import serializers 
from datetime import datetime 


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'