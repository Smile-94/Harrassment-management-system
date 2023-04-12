
# Generic View Classes
from django.views.generic import TemplateView

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from authority.permissions import AdminPassesTestMixin



class AuthorityHomeView(LoginRequiredMixin, AdminPassesTestMixin, TemplateView):
    template_name = 'authority/authority.html'
