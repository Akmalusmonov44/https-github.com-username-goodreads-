from django.test import TestCase

from django.contrib.auth import login
from django.urls import reverse

from books.models import Book, BookReview
from users.models import CustomUser


class HomePageTests(TestCase):
    def test_paginated_list(self):
        book = Book.objects.create(title='Book1', description='Some description', isbn='1234598414')
        user = CustomUser.objects.create_user(
            username='testuser',
            first_name='Test',
            last_name='User',
            email='testuser@example.com',
            password='somepassword'
        )
        review1 = BookReview.objects.create(book=book, user=user, stars_given=5, comment='verybest')
        review2 = BookReview.objects.create(book=book, user=user, stars_given=5, comment='useful')
        review3 = BookReview.objects.create(book=book, user=user, stars_given=5, comment='nice')
        response = self.client.get(reverse('landing_page') + '?page_size=2')

        self.assertContains(response, review3.comment,)
        self.assertContains(response, review2.comment,)
        self.assertNotContains(response, review1.comment,)

