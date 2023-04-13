from django.urls import path


from accounts.views import signup_view

app_name = 'accounts'

urlpatterns = [
    path('', signup_view.StudentLoginView.as_view(), name='login'),
    path('signup/', signup_view.SignupView.as_view(), name='signup'),
    path('login/', signup_view.StudentLoginView.as_view(), name='login'),
    path('user-login/', signup_view.UserLoginView.as_view(), name='user_login'),
    path('logout/', signup_view.UserLogoutView.as_view(), name='logout'),
]