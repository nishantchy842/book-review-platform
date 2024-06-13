from rest_framework.decorators import api_view
from book_review.builders.response_builder import ResponseBuilder
from .serializer import UserLoginSerializer, UserSerializer
from book_review.token import get_tokens_for_user
from .user_service import userServices






@api_view(['POST'])
def login(request):
    response_builder = ResponseBuilder()
    user_services = userServices()
    
    serializer = UserLoginSerializer(data=request.data)
    if not serializer.is_valid():
        return response_builder.get_400_bad_request_response('input incorrect', serializer.errors)
    email = serializer.data.get('email')
    password = serializer.data.get('password')
    
    user = user_services.get_user_by_email(email)
    
    if not user:
        return response_builder.get_404_not_found_response('email not found')
    
    
    token = get_tokens_for_user(user=user)
    
    user_serializer = UserSerializer(user)
    
    response_data = {
                'token': token,
                'user': user_serializer.data
            }
    
    return response_builder.result_object(response_data).success().message('api success').ok_200().get_json_response()
    
    
    
    
                