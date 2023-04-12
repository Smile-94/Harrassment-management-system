from django.urls import reverse_lazy


# Import Generic View Classes
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView

# Import Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from student.permissions import StudentPassesTestMixin

# Models
from harassment.models import Harassment

# Forms
from harassment.forms import HarassmentRequistForm


class HarassmentcomplaintView(LoginRequiredMixin, StudentPassesTestMixin, CreateView):
    model = Harassment
    form_class = HarassmentRequistForm
    template_name = 'student/add_complaint.html'
    success_url = reverse_lazy('student:student_home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Complaint Harassment"
        return context
    
    def form_valid(self, form):
        form_obj = form.save(commit=False)
        form_obj.submit_by = self.request.user.student_info
        form_obj.save()
        return super().form_valid(form)

class PendingComplaintListView(LoginRequiredMixin, StudentPassesTestMixin, ListView):
    queryset = Harassment.objects.filter(accept_status=False,decline_status=False).order_by('-id')
    context_object_name = 'complaints'
    template_name = 'student/pending_complaint.html'

    def get_queryset(self):
        return self.queryset.filter(submit_by= self.request.user.student_info)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Pending Complaint List"
        return context


class ComplaintHarassmentDetailsView(LoginRequiredMixin, StudentPassesTestMixin, DetailView):
    model = Harassment
    context_object_name = 'complaint'
    template_name = 'student/complaint_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Complaint Details"
        return context
    
    

