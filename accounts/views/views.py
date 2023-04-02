from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse

#Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin

#Generic Views
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout

# Model
from accounts.models import User

# Forms
from accounts.forms import SignUpForm


# Create your views here.
class SignupView(CreateView):
    model = User
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:logout')
    template_name = 'accounts/signup.html'


class UserLogout(LoginRequiredMixin, LogoutView):
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponse("LOgin Student Successfull")