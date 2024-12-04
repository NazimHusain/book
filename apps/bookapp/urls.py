from django.urls import path
from apps.bookapp.views import BooksListView

urlpatterns = [
    path("list/", BooksListView.as_view(),  name='books-list'),
]

