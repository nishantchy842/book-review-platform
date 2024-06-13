from book_review.builders.response_builder import ResponseBuilder
from rest_framework.views import APIView
from .serializer import BookSerializer, ReviewSerializer, CreateBookSerializer
from .book_service import BookServices
from rest_framework.decorators import authentication_classes
from book_review.shared.authentication import BorrowerAuthentication
from rest_framework.permissions import IsAuthenticated

class AllBooks(APIView):
    def get(self, request, *args, **kwargs):
        response_builder = ResponseBuilder()
        book_service = BookServices()
        

        try:
            books = book_service.get_all_books()
            serializer = BookSerializer(books, many=True).data
            return response_builder.result_object(serializer).success().message('All books list').ok_200().get_response()
        except Exception as e:
            return response_builder.result_object({'message': "Unable to get books"}).fail().internal_error_500().message("Internal Error").get_response()
    
 


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
        
@authentication_classes([BorrowerAuthentication])
class CreateBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response_builder = ResponseBuilder()
        serializer = CreateBookSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            try:
                book = serializer.save()
                response_serializer = CreateBookSerializer(book)

                return response_builder.result_object(response_serializer.data).success().accepted_202().message('Created successfully').get_response()
            except Exception as e:
                return response_builder.result_object({'message': str(e)}).fail().internal_error_500().get_response()
        else:
            errors = serializer.errors
            return response_builder.result_object({'message': errors}).fail().bad_request_400().get_response()
        

@authentication_classes([BorrowerAuthentication])
class GetLoginUserBook(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        book_service = BookServices()
        response_builder = ResponseBuilder()
        try:
            user_book = book_service.get_login_user_book(request.user.id)
            books = BookSerializer(user_book, many=True)
            return response_builder.result_object(books.data).success().ok_200().get_response()
        except Exception as e:
            return response_builder.result_object({'message': "Unable to get books"}).fail().internal_error_500().message("Internal Error").get_response()
        
@authentication_classes([BorrowerAuthentication])
class DeleteBook(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request,book_id):
        book_service = BookServices()
        response_builder = ResponseBuilder()
        try:
            book_service.delete_book_by_id(book_id, request.user.id)
            return response_builder.result_object(None).success().ok_200().message('Book deleted successfully').get_response()
        except PermissionError as e:
            return response_builder.result_object({'message': str(e)}).fail().user_forbidden_403().get_response()
        except ValueError as e:
            return response_builder.result_object({'message': str(e)}).fail().get_404_not_found_response().get_response()
        except Exception as e:
            return response_builder.result_object({'message': str(e)}).fail().internal_error_500().get_response()   
        