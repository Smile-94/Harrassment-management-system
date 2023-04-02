from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

# models
from accounts.models import User
from accounts.models import Profile


# Widgets
from accounts.widgets import CustomPictureImageFieldWidget


# forms
class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email','student_id', 'password1', 'password2',)


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username')
        self.fields['student_id'] = forms.CharField(label="Student ID", max_length=100)

    def clean(self):
        student_id = self.cleaned_data.get('student_id')
        password = self.cleaned_data.get('password')
        user = authenticate(student_id=student_id, password=password)

        if user is None:
            raise forms.ValidationError("Invalid login credentials")
        elif not user.is_active:
            raise forms.ValidationError("This account is inactive")
        elif not user.is_student:
            raise forms.ValidationError("This user is not a student")

        self.cleaned_data['username'] = user.student_id
        self.cleaned_data['password'] = password

        return self.cleaned_data


class ProfileForm(forms.ModelForm):
    photo = forms.ImageField(widget=CustomPictureImageFieldWidget)

    class Meta:
        model = Profile
        exclude = ('user',)


