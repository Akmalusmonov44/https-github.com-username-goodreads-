from django.urls import path
from django.views.generic import DeleteView

from books.views import BookView, BookDetailView, AddReviewView, EditReviewView, ConfirmDeleteReviewView, \
    DeleteReviewView

app_name = 'books'
urlpatterns = [
    path('', BookView.as_view(), name='list'),
    path('<int:book_id>/', BookDetailView.as_view(), name='detail'),
    path('<int:book_id>/review/', AddReviewView.as_view(), name='review'),
    path('<int:book_id>/review/<int:review_id>/edit/', EditReviewView.as_view(), name='edit'),
    path('<int:book_id>/review/<int:review_id>/delete-review/', ConfirmDeleteReviewView.as_view(), name='delete-review'),
    path('<int:book_id>/review/<int:review_id>/delete/', DeleteReviewView.as_view(),
         name='deleted-review'),

]