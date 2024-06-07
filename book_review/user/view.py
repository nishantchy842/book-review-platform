from rest_framework.views import APIView
from book_review.builders.response_builder import ResponseBuilder
from book_review.token import get_tokens_for_user
from .user_service import userServices
from .serializer import userSerializers , UserLoginSerializer
from django.contrib.auth import authenticate



class allUser(APIView):
    def get(self, request, *args, **kwargs):
        response_builder = ResponseBuilder()
        user_service = userServices()

        try:
            users = user_service.get_all_user()
            serializer = userSerializers(users, many=True)
            return response_builder.result_object(serializer.data).success().message('all users list').ok_200().get_response()
        except Exception as e:
            return response_builder.result_object({'message': "Unable to get companies"}).fail().internal_error_500().message("Internal Error").get_response()


class singleUser(APIView):
     def get(self, request,id=None, *args, **kwargs):
        response_builder = ResponseBuilder()
        user_service = userServices()

        try:
            users = user_service.get_user_by_id(id=id)
            serializer = userSerializers(users)
            return response_builder.result_object(serializer.data).success().ok_200().get_response()
        except Exception as e:
            return response_builder.result_object({'message': "Unable to get companies"}).fail().internal_error_500().message("Internal Error").get_response()
        
        
class createUser(APIView):
    def post(self, request):
        response_builder = ResponseBuilder()
        serializer = userSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(request.data)
            user = serializer.save()
            return response_builder.result_object(user).success().ok_200().message('registered successfully').get_response()
        # print(serializer.errors)
        return response_builder.result_object({'message': "Unable to get companies"}).fail().bad_request_400().get_response()

class UserLoginView(APIView):

    def post(self, request, format=None):
        response_builder = ResponseBuilder()
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            print(user,'user')
            if user is not None:
                token = get_tokens_for_user(user)
                return response_builder.result_object({token}).message('login successful').ok_200().get_response()
            else:
                return response_builder.fail().get_404_not_found_response('not found')
        return response_builder.result_object({'message': "Bad request"}).fail().bad_request_400().get_json_response()
                