from book_review.builders.response_builder import ResponseBuilder
from rest_framework.views import APIView
from .serializer import BookSerializer, ReviewSerializer
from .book_service import BookServices


class allBooks(APIView):
    def get(self, request, *args, **kwargs):
        response_builder = ResponseBuilder()
        book_service = BookServices()

        try:
            books = book_service.get_all_books()
            serializer = BookSerializer(books, many=True)
            return response_builder.result_object(serializer.data).success().message('all users list').ok_200().get_response()
        except Exception as e:
            return response_builder.result_object({'message': "Unable to get companies"}).fail().internal_error_500().message("Internal Error").get_response()
        
    def post(self, request):
        response_builder = ResponseBuilder()
        try:
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                book = serializer.save()
                return response_builder.result_object(book).success().accepted_202().message('created successfully').get_response()
            else:
                errors = serializer.errors
                return response_builder.result_object({'message': errors}).fail().bad_request_400().get_response()
        except Exception as e:
            return response_builder.result_object({'message': str(e)}).fail().internal_error_500().get_response()   


class singleBook(APIView):
     def get(self, request,id=None, *args, **kwargs):
        response_builder = ResponseBuilder()
        book_service = BookServices()

        try:
            book = book_service.get_book_by_id(id=id)
            serializer = BookSerializer(book)
            return response_builder.result_object(serializer.data).success().ok_200().get_response()
        except Exception as e:
            return response_builder.result_object({'message': "Unable to get companies"}).fail().internal_error_500().message("Internal Error").get_response()
        
        
