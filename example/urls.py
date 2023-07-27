from django.urls import path, include
from .views import BooksAPIMixins, BookAPIMixins

urlpatterns = [
    path("mixin/books/", BooksAPIMixins.as_view()),
    path("mixin/book/<int:bid>/", BookAPIMixins.as_view()),
]
