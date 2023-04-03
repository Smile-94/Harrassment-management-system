from django.urls import reverse_lazy
from django.contrib import messages

# Generic Class
from django.views.generic import CreateView
from django.views.generic import UpdateView

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from student.permissions import StudentPassesTestMixin

# Models
from student.models import StudentInfo
from student.forms import StudentInfoForm


class AddStudentInfoView(LoginRequiredMixin, StudentPassesTestMixin, UpdateView):
    model = StudentInfo
    form_class = StudentInfoForm
    template_name = 'student/add_profile.html'
    success_url = reverse_lazy('student:student_home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Profile"
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Profile Updated Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Profile not updated try again!")
        return super().form_invalid(form)
    
