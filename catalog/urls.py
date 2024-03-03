from django.urls import path, include, re_path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('book_detail/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('author_list/', views.AuthorListView.as_view(), name='author_list'),
    path('Author_detail/<int:pk>', views.AuthorDetailView.as_view(), name='author_detail'),


    path('my_books/', views.LoanedBooksByUserListView.as_view(), name='my_books'),
]
