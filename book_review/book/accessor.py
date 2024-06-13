from book_review.models import Books


class BookAccessor:
    
    @staticmethod
    def get_all_books():
        print('execute')
        return Books.objects.filter(is_deleted = False).all().order_by('-created_at')
    
    @staticmethod
    def get_book_by_id(id):
        return Books.objects.filter(id=id, is_deleted = False).first()
    
    
    @staticmethod
    def delete_book(id):
        book = BookAccessor.get_book_by_id(id=id)
        book.is_deleted = True
        return book.save()
        
    
    @staticmethod
    def get_login_user_book(id):
        book = Books.objects.filter(created_by_id = id)
        return book    