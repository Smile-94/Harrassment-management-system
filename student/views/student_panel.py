

# Generic Classes
from django.views.generic import TemplateView



class StudentHomeView(TemplateView):
    template_name ='student/student.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Title' 
        return context
    