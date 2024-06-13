from .accessor import UserAccessor


class userServices:
    def get_all_user(self):
        data = UserAccessor.get_all_user()
        return data
    
    def get_user_by_id(self,id):
        data = UserAccessor.get_user_by_id(id)
        print(data,'data')
        return data
    
    def get_user_by_email(self, email):
        data = UserAccessor.get_user_by_email(email)
        print(data,'data')
        return data
    