from django.urls import path


# Views 
from authority.views import authority_main
from authority.views import manage_complient
from authority.views import manage_student


app_name = 'authority'

urlpatterns = [
    path('authority/', authority_main.AuthorityHomeView.as_view(), name='authority'),
]

# Manage student
urlpatterns += [
    path('student-list/', manage_student.StudentListView.as_view(), name='student_list'),
    path('student-details/<int:pk>/', manage_student.StudentDetailsView.as_view(), name='student_detail'),
    
]


# Manage Complient
urlpatterns += [
    path('pending-complaint-list/', manage_complient.AdminPendingComplaintListView.as_view(), name='pending_complaint_list'),
    path('accpted-complaint-list/', manage_complient.AdminAccptedComplaintListView.as_view(), name='accpted_complaint_list'),
    path('declined-complaint-list/', manage_complient.AdminCelinedComplaintListView.as_view(), name='declined_complaint_list'),
    path('complaint-details/<int:pk>/', manage_complient.AdminComplaintHarassmentDetailsView.as_view(), name='complaint_detail'),
    path('complaint-accept/<int:pk>/', manage_complient.AcceptHarassmentComplaintView.as_view(), name='complaint_accept'),
    path('complaint-decline/<int:pk>/', manage_complient.DeclinedHarassmentComplaintView.as_view(), name='complaint_decline'),
]
