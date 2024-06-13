
from django.urls import path
from book_review.user.view import allUser, singleUser, createUser
from book_review.book.view import AllBooks, singleBook, CreateBookView, GetLoginUserBook, DeleteBook,UpdateBookView
from book_review.user import auth

urlpatterns = [
    # login
    
    
    path('login/',  auth.login, name='login'),
    path('user/books',  GetLoginUserBook.as_view(), name='user_books'),
    path('user/books/delete/<int:book_id>',  DeleteBook.as_view(), name='delete_book'),
    
    # user
    path('user/',  allUser.as_view(), name='user'),
    #book
    path('books/<int:book_id>/update', UpdateBookView.as_view(), name='update-book'),

    path('user/<int:id>',  singleUser.as_view(), name='single_user'),
    path('user/register',  createUser.as_view(), name='create_user'),
    path('book/create',  CreateBookView.as_view(), name='create_book'),
    path('book/<int:id>',  singleBook.as_view(), name='get_single_book'),
    path('book/',  AllBooks.as_view(), name='all_book'),
    
   
]