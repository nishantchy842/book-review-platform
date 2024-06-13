from book_review.models import UserModel


class UserAccessor:
    
    @staticmethod
    def get_all_user():
        return UserModel.objects.filter(is_deleted = False).all().order_by('-created_at')
    
    @staticmethod
    def get_user_by_id(id):
        return UserModel.objects.filter(id=id, is_deleted = False).first()
    
    
    @staticmethod
    def get_user_by_email(email):
        return UserModel.objects.filter(email = email, is_deleted=False).first() 