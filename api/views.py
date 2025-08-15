from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from books.models import BookReview, Book
from api.serializers import BookReviewSerializer, BookSerializer, BookReviewListSerializer
from rest_framework import viewsets

class BookReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookReviewSerializer
    queryset = BookReview.objects.all().order_by('-created_at', '-id')
    lookup_field = 'id'

