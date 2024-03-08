from rest_framework import serializers
from .models import Book, BookNumber, Character, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = "__all__"


class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False, read_only=True)
    characters = CharacterSerializer(many=True, read_only=True)
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = "__all__"


