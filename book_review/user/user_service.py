from .accessor import UserAccessor


class userServices:
    def get_all_user(self):
        data = UserAccessor.get_all_user()
        return data
    
    def get_user_by_id(self,id):
        data = UserAccessor.get_user_by_id(id)
        return data
    