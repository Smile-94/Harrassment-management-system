from django.urls import path


app_name = 'student'

from student.views import student_panel
from student.views import manage_profile
from student.views import manage_harassment


# Student Home
urlpatterns = [
    path('student-home', student_panel.StudentHomeView.as_view(), name='student_home')
]

# Manage Profile
urlpatterns += [
    path('add-profile/<int:pk>/', manage_profile.AddStudentInfoView.as_view(), name='add_profile' ),
]

# Manage Harassment
urlpatterns += [
    path('complaint-harassment/', manage_harassment.HarassmentcomplaintView.as_view(), name='complaint_harassment'),
    path('pending-complaint-harassment-list/', manage_harassment.PendingComplaintListView.as_view(), name='pending_complaint_harassment'),
    path('accpted-complaint-harassment-list/', manage_harassment.AccptedComplaintListView.as_view(), name='accpted_complaint_harassment'),
    path('complaint-harassment-details/<int:pk>/', manage_harassment.ComplaintHarassmentDetailsView.as_view(), name='complaint_harassment_detail'),
]

