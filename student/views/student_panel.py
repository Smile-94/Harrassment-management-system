

# Generic Classes
from django.views.generic import TemplateView

# Permission Classes
from harassment.models import Harassment



class StudentHomeView(TemplateView):
    template_name ='student/student.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Title' 
        context["totla_complaient"] = Harassment.objects.filter(submit_by=self.request.user.student_info).count()
        context["pending_complaient"] = Harassment.objects.filter(submit_by=self.request.user.student_info, accept_status=False, decline_status=False).count()
        context["accpted_complaient"] = Harassment.objects.filter(submit_by=self.request.user.student_info, accept_status=True, decline_status=False).count()
        context["declined_complaient"] = Harassment.objects.filter(submit_by=self.request.user.student_info, accept_status=False, decline_status=True).count()
        context["complaints"] = Harassment.objects.filter(submit_by=self.request.user.student_info, accept_status=False, decline_status=False).order_by('-id')[:10]

        return context
    