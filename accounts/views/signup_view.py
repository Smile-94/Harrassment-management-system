from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse

#Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin

#Generic Views
from django.contrib.auth import authenticate
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from django.contrib.auth import login

# Model
from accounts.models import User

# Forms
from accounts.forms import SignUpForm
from accounts.forms import CustomAuthenticationForm
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
class SignupView(CreateView):
    model = User
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:logout')
    template_name = 'accounts/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Signpu Student"
        return context

class UserLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'accounts/login.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Login Page" 
        return context
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        student_id = form.cleaned_data.get('student_id')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, student_id=student_id, password=password)
        if user is not None:
            if user.is_student:
                login(self.request, user)
                return HttpResponse("Student login panel will implement soon")
            else:
                return HttpResponse("You are not a student")
        else:
            return self.form_invalid(form)


class UserLogout(LoginRequiredMixin, LogoutView):
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponse("LOgin Student Successfull")