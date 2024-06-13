from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from book_review_project import settings

# from app.app_admin.admin import Admin
from book_review.user.user_service import userServices


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")
        print(auth_header,'auth.')

        if not auth_header or not auth_header.startswith("Bearer "):
            raise NotAuthenticated("Authorization header missing")

        try:
            token = auth_header.split(" ")[1]
            payload = AccessToken(token).payload
            id = payload.get(settings.SIMPLE_JWT["USER_ID_CLAIM"])
            borrow_auth = BorrowerAuthentication()
            user = borrow_auth.get_user_by_id(id) if id else None
            if not user:
                raise AuthenticationFailed("Invalid auth token")
            return user, None
        
        
        except AuthenticationFailed as e:
            raise e
        except Exception as e:
            raise AuthenticationFailed(f"Invalid auth token {e}")
    def get_user_by_id(self, id):
        return userServices.get_user_by_id(id)

class BorrowerAuthentication(JWTAuthentication):
    def get_user_by_id(self, id):
        return userServices().get_user_by_id(id)


# class AdminAuthentication(JWTAuthentication):
#     def get_user_by_id(self, id):
#         return Admin.get_user_by_id(id)
