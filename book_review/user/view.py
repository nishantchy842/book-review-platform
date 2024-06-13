from rest_framework.views import APIView
from book_review.builders.response_builder import ResponseBuilder
from book_review.token import get_tokens_for_user
from .user_service import userServices
from .serializer import UserSerializer , UserLoginSerializer
from django.contrib.auth import authenticate
from rest_framework.decorators import authentication_classes
from book_review.shared.authentication import BorrowerAuthentication

class allUser(APIView):
    def get(self, request, *args, **kwargs):
        response_builder = ResponseBuilder()
        user_service = userServices()

        try:
            users = user_service.get_all_user()
            serializer = UserSerializer(users, many=True)
            return response_builder.result_object(serializer.data).success().message('all users list').ok_200().get_response()
        except Exception as e:
            return response_builder.result_object({'message': "Unable to get companies"}).fail().internal_error_500().message("Internal Error").get_response()

@authentication_classes([BorrowerAuthentication])
class singleUser(APIView):
     def get(self, request,id=None, *args, **kwargs):
        response_builder = ResponseBuilder()
        user_service = userServices()

        try:
            users = user_service.get_user_by_id(id=id)
            serializer = UserSerializer(users)
            return response_builder.result_object(serializer.data).success().ok_200().get_response()
        except Exception as e:
            return response_builder.result_object({'message': "Unable to get companies"}).fail().internal_error_500().message("Internal Error").get_response()
        
        
class createUser(APIView):
    def post(self, request):
        response_builder = ResponseBuilder()
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(request.data)
            user = serializer.save()
            user_data = UserSerializer(user).data
            return response_builder.result_object(user_data).success().ok_200().message('registered successfully').get_response()
        # print(serializer.errors)
        return response_builder.result_object({'message': "Unable to get companies"}).fail().bad_request_400().get_response()

