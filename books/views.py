from msilib.schema import ListView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from pyexpat.errors import messages

from books.forms import BookReviewForm
from books.models import Book, BookReview


#
# class BookView(ListView):
#     context_object_name = 'books'
#     template_name = 'books/list.html'
#     queryset = Book.objects.all()

class BookView(View):
    def get(self, request):
        books = Book.objects.all().order_by('id')
        search_query = request.GET.get('q')
        if search_query:
            books = books.filter(title__icontains=search_query)


        page_size = request.GET.get('page_size', 2  )
        paginator = Paginator(books, 2)


        page_num = request.GET.get('page',1)
        page_obj = paginator.get_page(page_num)

        return render(request, 'books/list.html', {'page_obj': page_obj})

# class BookDetailView(DetailView):
#     template_name = 'books/detail.html'
#     pk_url_kwarg = 'book_id'
#     model = Book

class BookDetailView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        review_form = BookReviewForm()

        return render(request, 'books/detail.html', {'book': book, 'review_form': review_form})

class AddReviewView(LoginRequiredMixin, View):
    def post(self, request, book_id):
        book = Book.objects.get(id=book_id)
        review_form = BookReviewForm(data=request.POST)

        if review_form.is_valid():
            BookReview.objects.create(
                book=book,
                user=request.user,
                stars_given=review_form.cleaned_data['stars_given'],
                comment=review_form.cleaned_data['comment'],
            )

            return redirect(reverse('books:detail', kwargs={'book_id': book.id}))

        return render(request, 'books/detail.html', {'book': book, 'review_form': review_form, })

class EditReviewView(LoginRequiredMixin, View):
    def get(self, request, book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)
        review_form = BookReviewForm(instance=review)

        return render(request, 'books/edit.html', {'book': book, 'review': review, 'review_form': review_form})

    def post(self, request, book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)
        review_form = BookReviewForm(instance=review, data=request.POST)

        if review_form.is_valid():
            review_form.save()
            return redirect(reverse('books:detail', kwargs={'book_id': book.id}))


        return render(request, 'books/edit.html', {'book': book, 'review': review, 'review_form': review_form})

class ConfirmDeleteReviewView(LoginRequiredMixin, View):
    def get(self, request, book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)

        return render(request, 'books/confirm_delete.html', {'book': book, 'review': review,})

class DeleteReviewView(LoginRequiredMixin, View):
    def get(self, request, book_id, review_id):
        book = get_object_or_404(Book, id=book_id)
        review = get_object_or_404(BookReview, id=review_id, book=book)

        review.delete()
        return redirect(reverse('books:detail', kwargs={'book_id': book.id}))