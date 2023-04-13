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
from harassment.models import Harassment

# Forms
from harassment.forms import HarassmentAcceptForm
from harassment.forms import HarassmentDeclineForm


class AdminPendingComplaintListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    queryset = Harassment.objects.filter(accept_status=False,decline_status=False).order_by('-id')
    context_object_name = 'complaints'
    template_name = 'authority/pending_complaint.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Pending Complaint List"
        return context
    
class AdminAccptedComplaintListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    queryset = Harassment.objects.filter(accept_status=True,decline_status=False).order_by('-id')
    context_object_name = 'complaints'
    template_name = 'authority/pending_complaint.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Pending Complaint List"
        return context
    
class AdminCelinedComplaintListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    queryset = Harassment.objects.filter(accept_status=False,decline_status=True).order_by('-id')
    context_object_name = 'complaints'
    template_name = 'authority/declined_complaint_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Declined Complaint List"
        return context


class AdminComplaintHarassmentDetailsView(LoginRequiredMixin,AdminPassesTestMixin,  DetailView):
    model = Harassment
    context_object_name = 'complaint'
    template_name = 'authority/complaint_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Complaint Details"
        return context


class AcceptHarassmentComplaintView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = Harassment
    form_class = HarassmentAcceptForm
    template_name = 'authority/accept_complaint.html'
    success_url = reverse_lazy('authority:pending_complaint_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Accept Complaint"
        return context

    def form_valid(self, form):
        form_obj = form.save(commit=False)
        form_obj.accept_status= True
        form_obj.save()
        return super().form_valid(form)
    

class DeclinedHarassmentComplaintView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = Harassment
    form_class = HarassmentDeclineForm
    template_name = 'authority/decline_complaint.html'
    success_url = reverse_lazy('authority:pending_complaint_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Accept Complaint"
        return context

    def form_valid(self, form):
        form_obj = form.save(commit=False)
        form_obj.decline_status= True
        form_obj.save()
        return super().form_valid(form)
    
    
    

