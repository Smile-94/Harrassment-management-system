from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class StudentIDBackend(ModelBackend):
    def authenticate(self, request, student_id=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(student_id=student_id)
        except UserModel.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None
