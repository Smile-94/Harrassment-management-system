from django import forms

# Widgets
from student.widgets import CustomPictureImageFieldWidget
from student.widgets import CustomSignetureImageFieldWidget

# Models
from student.models import StudentInfo

class StudentInfoForm(forms.ModelForm):
    photo = forms.ImageField(widget=CustomPictureImageFieldWidget)
    signature = forms.ImageField(widget=CustomSignetureImageFieldWidget)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = StudentInfo
        exclude = ('info_of','is_active')