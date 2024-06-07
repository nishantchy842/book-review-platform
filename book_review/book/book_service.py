from .accessor import BookAccessor


class BookServices:
    def get_all_books(self):
        data = BookAccessor.get_all_books()
        return data
    
    def get_book_by_id(self,id):
        data = BookAccessor.get_book_by_id(id)
        return data
    
    def delete_book_by_id(self, id):
        data = BookAccessor.delete_book(id)
        return data