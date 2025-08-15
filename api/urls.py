from django.urls import path

# from api.views import BookReviewDetailApiView, BookListApiView, BookReviewListApiView
from rest_framework.routers import DefaultRouter
from api.views import BookReviewViewSet
app_name = 'api'
router = DefaultRouter()
router.register('review', BookReviewViewSet, basename='review')
urlpatterns = router.urls



