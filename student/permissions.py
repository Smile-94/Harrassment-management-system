from django.contrib.auth.mixins import UserPassesTestMixin

class StudentPassesTestMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_student