from book_review.models import Book, Review


class BookAccessor:
    
    @staticmethod
    def get_all_books():
        return Book.objects.filter(is_deleted = False).all().order_by('-created_at')
    
    @staticmethod
    def get_book_by_id(id):
        return Book.objects.filter(id=id, is_deleted = False).first()
    
    @staticmethod
    def delete_book(id):
        book = BookAccessor.get_book_by_id(id=id)
        book.is_deleted = True
        book.save()