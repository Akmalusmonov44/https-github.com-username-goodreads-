from django.test import TestCase
from django.urls import reverse
from books.models import Book, BookReview
from users.models import CustomUser


class BookTestCase(TestCase):
    def test_no_books(self):
        response = self.client.get(reverse('books:list'))

        self.assertContains(response, 'No books found')


    def test_books_list(self):
        book1 = Book.objects.create(title='Book1', description='Some description', isbn='12345')
        book2 = Book.objects.create(title='Book2', description='Some description', isbn='12346')
        book3 = Book.objects.create(title='Book3', description='Some description', isbn='12347')

        response = self.client.get(reverse('books:list'))


        for book in [book1, book2] :
            self.assertContains(response, book.title)

        response = self.client.get(reverse('books:list')+ '?page=2')

        self.assertContains(response, book3.title)

    def test_books_detail(self):
        book = Book.objects.create(title='Book1', description='Some description', isbn='1234598414')

        response = self.client.get(reverse('books:detail', kwargs={'book_id': book.id}))

        self.assertContains(response, book.title)
        self.assertContains(response, book.description)

    def test_search_books(self):
        book1 = Book.objects.create(title='Sport', description='Some description', isbn='12345')
        book2 = Book.objects.create(title='Guide', description='Some description', isbn='12346')
        book3 = Book.objects.create(title='Shoe Dog', description='Some description', isbn='12347')

        response = self.client.get(reverse('books:list') + '?q=sport')
        self.assertContains(response, book1.title)
        self.assertNotContains(response, book2.title)
        self.assertNotContains(response, book3.title)


class BookReviewTestCase(TestCase):
    def test_add_review(self):
        book = Book.objects.create(title='Book1', description='Some description', isbn='1234598414')

        user = CustomUser.objects.create_user(
            username='testuser',
            first_name='Test',
            last_name='User',
            email='testuser@example.com',
            password='somepassword'  # bu password login uchun ishlatiladi
        )

        self.client.login(username='testuser', password='somepassword')

        self.client.post(reverse('books:review', kwargs={'book_id': book.id}), data={
            'stars_given': 5,
            'comment': 'nice comment',
        })
        book_review = book.bookreview_set.all()

        self.assertEqual(book_review[0].stars_given, 5)
        self.assertEqual(book_review.count(),1 )
        self.assertEqual(book_review[0].comment, 'nice comment')
        self.assertEqual(book_review[0].book, book)
        self.assertEqual(book_review[0].user, user)

    def test_edit_review(self):
        book = Book.objects.create(
            title='Book1',
            description='Some description',
            isbn='1234598414'
        )

        user = CustomUser.objects.create_user(
            username='testuser',
            first_name='Test',
            last_name='User',
            email='testuser@example.com',
            password='somepassword'
        )

        self.client.login(username='testuser', password='somepassword')

        self.client.post(reverse('books:review', kwargs={'book_id': book.id}), data={
            'stars_given': 5,
            'comment': 'nice comment',
        })

        review = BookReview.objects.get(book=book, user=user)

        # Edit review
        self.client.post(reverse('books:edit', kwargs={
            'book_id': book.id,
            'review_id': review.id
        }), data={
            'stars_given': 3,
            'comment': 'updated comment',
        })

        review.refresh_from_db()
        self.assertEqual(review.stars_given, 3)
        self.assertEqual(review.comment, 'updated comment')








