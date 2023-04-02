from django.urls import path


from accounts.views import signup_view

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup_view.SignupView.as_view(), name='signup'),
    path('login/', signup_view.UserLoginView.as_view(), name='login'),
]