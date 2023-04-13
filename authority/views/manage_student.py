from django.urls import reverse_lazy


# Import Generic View Classes
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView

# Import Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from authority.permissions import AdminPassesTestMixin

# Models
from accounts.models import User

class StudentListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    model = User
    queryset = User.objects.filter(is_active=True, is_student=True).order_by('-id')
    context_object_name = 'students'
    template_name = 'authority/student_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Student List"
        return context

class StudentDetailsView(LoginRequiredMixin, AdminPassesTestMixin, DetailView):
    model = User
    context_object_name = 'student'
    template_name = 'authority/student_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Studetn Details"
        return context
    
    




