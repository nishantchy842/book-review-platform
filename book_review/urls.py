
from django.urls import path
from book_review.user.view import allUser, singleUser, createUser, UserLoginView
from book_review.book.view import allBooks, singleBook

urlpatterns = [
    path('user/',  allUser.as_view(), name='user'),
    path('user/<int:id>',  singleUser.as_view(), name='single_user'),
    path('user/register',  createUser.as_view(), name='create_user'),
    path('user/login',  UserLoginView.as_view(), name='user_login'),
    path('book/',  allBooks.as_view(), name='create_book'),
    path('book/<int:id>',  singleBook.as_view(), name='get_single_book'),
    path('book/',  allBooks.as_view(), name='all_book'),
    
   
]