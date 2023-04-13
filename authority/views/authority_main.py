
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
        context = super().get_context_data(**kwargs)
        context["title"] = "Authority" 
        context["complaints"] = Harassment.objects.filter(accept_status=False,decline_status=False).order_by('-id')
        return context
    
