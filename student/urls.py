from django.urls import path


app_name = 'student'

from student.views import student_panel


# Student Home
urlpatterns = [
    path('student-home', student_panel.StudentHomeView.as_view(), name='student_home')
]