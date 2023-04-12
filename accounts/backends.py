from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth import get_user_model
from accounts.models import User

class StudentIDBackend(ModelBackend):
    def authenticate(self, request, student_id=None, password=None, **kwargs):
        UserModel = User
        users = UserModel.objects.filter(student_id=student_id)
        for user in users:
            if user.check_password(password):
                return user
        return None
