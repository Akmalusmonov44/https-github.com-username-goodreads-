from http.client import responses

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from books.models import Book, BookReview
from users.models import CustomUser


class BookReviewApiTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', first_name='test',)
        self.user.set_password('somepassword')
        self.user.save()
        self.client.login(username='testuser', password='somepassword')

    def test_book_review_detail(self):
        book = Book.objects.create(title='Book1', description='Some description', isbn='1234598414')
        br = BookReview.objects.create(book=book, user=self.user, stars_given=5, comment='Very good')

        response = self.client.get(reverse('api:review-detail', kwargs={'id': br.id}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], br.id)
        self.assertEqual(response.data['stars_given'], 5)
        self.assertEqual(response.data['comment'], 'Very good')
        self.assertEqual(response.data['book']['id'], br.book.id)
        self.assertEqual(response.data['book']['title'], 'Book1')
        self.assertEqual(response.data['book']['description'], 'Some description')
        self.assertEqual(response.data['book']['isbn'], '1234598414')
        self.assertEqual(response.data['user']['id'], self.user.id)
        self.assertEqual(response.data['user']['username'], 'testuser')
        self.assertEqual(response.data['user']['first_name'], 'test')

    def test_book_review_delete(self):
        book = Book.objects.create(title='Book1', description='Some description', isbn='1234598414')
        br = BookReview.objects.create(book=book, user=self.user, stars_given=5, comment='Very good')

        response = self.client.delete(reverse('api:review-detail', kwargs={'id': br.id}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(BookReview.objects.filter(id=br.id).exists())

    def test_book_review_edit(self):
        book = Book.objects.create(title='Book1', description='Some description', isbn='1234598414')
        br = BookReview.objects.create(book=book, user=self.user, stars_given=5, comment='Very good')

        response = self.client.patch(reverse('api:review-detail', kwargs={'id': br.id}), data={
            'stars_given': 3,
        })
        br.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)


        self.assertEqual(br.stars_given, 3)

    def test_create_review(self):
        book = Book.objects.create(title='Book1', description='Some description', isbn='1234598414')
        data = {
            'stars_given': 3,
            'comment': 'Very Nice',
            'user_id': self.user.id,
            'book_id': book.id,
        }

        url = reverse('api:review-list')
        response = self.client.post(url, data=data)

        br = BookReview.objects.get(book=book)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(br.stars_given, 3)
        self.assertEqual(br.comment, 'Very Nice')

    def test_book_review_list(self):
        user2 = CustomUser.objects.create_user(username='somebody', first_name='someone',)

        book = Book.objects.create(title='Book1', description='Some description', isbn='1234598414')
        br = BookReview.objects.create(book=book, user=self.user, stars_given=5, comment='Very good')
        br2 = BookReview.objects.create(book=book, user=self.user, stars_given=4, comment='Very best')

        response = self.client.get(reverse('api:review-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)


        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['count'], 2)
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)


        self.assertEqual(response.data['results'][0]['id'], br2.id)
        self.assertEqual(response.data['results'][0]['comment'], br2.comment)
        self.assertEqual(response.data['results'][0]['stars_given'], br2.stars_given)
        self.assertEqual(response.data['results'][1]['id'], br.id)
        self.assertEqual(response.data['results'][1]['comment'], br.comment)
        self.assertEqual(response.data['results'][1]['stars_given'], br.stars_given)










