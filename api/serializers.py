

from books.models import BookReview, Book
from rest_framework import serializers

from users.models import CustomUser


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'isbn')



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class BookReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    book = BookSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    book_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = BookReview
        fields = ('id', 'comment', 'stars_given', 'book', 'user', 'user_id', 'book_id')

class BookReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookReview
        fields = ('id', 'book', 'stars_given', 'comment', 'user')


