from django.urls import path


# Views 
from authority.views import authority_main


app_name = 'authority'

urlpatterns = [
    path('authority/', authority_main.AuthorityHomeView.as_view(), name='authority'),
]