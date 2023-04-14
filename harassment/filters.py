import django_filters
from django import forms

# Models
from harassment.models import Harassment



# Create your models here.
HARASSMENT_OPT = (
    ('Raging', 'Raging'),
    ('Sexual Harassment', 'Sexual Harassment'),
    ('Racial Harassment', 'Racial Harassment'),
    ('Gender-based Harassment', 'Gender-based Harassment'),
    ('LGBTQ+ Harassment', 'LGBTQ+ Harassment'),
    ('Disability Harassment', 'Disability Harassment'),
    ('Age-related Harassment', 'Age-related Harassment'),
    ('Religious Harassment', 'Religious Harassment'),
)

class HarassmentFilter(django_filters.FilterSet):

    case_id = django_filters.CharFilter(widget=forms.TextInput(attrs={'placeholder': 'Case ID'}))
    harassment_type = django_filters.ChoiceFilter(choices=HARASSMENT_OPT)
    from_date = django_filters.DateFilter(field_name='submitted_date', lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date'}), label='From')
    to_date = django_filters.DateFilter(field_name='submitted_date', lookup_expr='lte', widget=forms.DateInput(attrs={'type': 'date'}), label='To')
    
    class Meta:
        model = Harassment
        fields = ('case_id','harassment_type','submitted_date')