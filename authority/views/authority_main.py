
# Generic View Classes
from django.views.generic import TemplateView

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from authority.permissions import AdminPassesTestMixin

# Models
from harassment.models import Harassment



class AuthorityHomeView(LoginRequiredMixin, AdminPassesTestMixin, TemplateView):
    template_name = 'authority/authority.html'

    def get_context_data(self, **kwargs):
        total_complaint = Harassment.objects.filter(is_active=True).count()
        pending_complaint = Harassment.objects.filter(is_active=True,accept_status=False,decline_status=False).count()
        accpted_complaint = Harassment.objects.filter(is_active=True,accept_status=True,decline_status=False).count()
        declined_complaint = Harassment.objects.filter(is_active=True,accept_status=False,decline_status=True).count()

        if total_complaint > 0:
            pending_percentage = (pending_complaint / total_complaint) * 100
            accpted_percentage = (accpted_complaint /total_complaint) * 100
            declined_percentage = (declined_complaint /total_complaint) * 100
        else:
            pending_percentage = 0
            accpted_percentage = 0
            declined_percentage = 0

        context = super().get_context_data(**kwargs)
        context["title"] = "Authority" 
        context["complaints"] = Harassment.objects.filter(is_active=True,accept_status=False,decline_status=False).order_by('-id')[:10]
        context["total_complaints"] = total_complaint
        context["pending_complaints"] = pending_complaint
        context["pending_percentage"] = pending_percentage
        context["accpted_complaint"] = accpted_complaint
        context["accpted_percentage"] = accpted_percentage
        context["declined_complaint"] =declined_complaint
        context["declined_percentage"] = declined_percentage
        return context
    
