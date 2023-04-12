from django import forms

# Import Models
from harassment.models import Harassment


class HarassmentRequistForm(forms.ModelForm):
    occurence_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Harassment
        fields = ('subject','harassment_type','occurence_date','accused_name','accused_is','accoused_detail','description','proof_file')