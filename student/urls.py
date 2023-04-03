from django.urls import path


app_name = 'student'

from student.views import student_panel
from student.views import manage_profile


# Student Home
urlpatterns = [
    path('student-home', student_panel.StudentHomeView.as_view(), name='student_home')
]

# Manage Profile
urlpatterns += [
    path('add-profile/<int:pk>/', manage_profile.AddStudentInfoView.as_view(), name='add_profile' ),
]
