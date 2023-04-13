from django import forms

# Import Models
from harassment.models import Harassment


class HarassmentRequistForm(forms.ModelForm):
    occurence_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Harassment
        fields = ('subject','harassment_type','occurence_date','accused_name','accused_is','accoused_detail','description','proof_file')

class HarassmentAcceptForm(forms.ModelForm):
    hearing_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    hearing_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Harassment
        fields = ('hearing_date','hearing_time','hearing_room','message')

class HarassmentDeclineForm(forms.ModelForm):

    class Meta:
        model = Harassment
        fields = ('message',)