from .accessor import BookAccessor
from book_review.user.user_service import userServices


class BookServices:
    def get_all_books(self):
        data = BookAccessor.get_all_books()
        print(data,'data')
        return data
    
    def get_book_by_id(self,id):
        data = BookAccessor.get_book_by_id(id)
        return data
    
    def delete_book_by_id(self, book_id, user_id):
        user_services = userServices()
        user = user_services.get_user_by_id(user_id)
        book = self.get_book_by_id(book_id)
        # Check if the user is the admin or the owner of the book
        if user.role != 'Admin' and book.created_by_id != user_id:
            raise PermissionError("Only admins or the owner of the book can delete it.")

        # Perform the delete operation
        data = BookAccessor.delete_book(book_id)
        return data
    
    def get_login_user_book(self, id):
        data = BookAccessor.get_login_user_book(id=id)
        return data
    
