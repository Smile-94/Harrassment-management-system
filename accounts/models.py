from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy

# uploaded file path
from accounts.utils import user_directory_path

# Create your models here.
class MyUserManager(BaseUserManager):

    """A custom manager to deal with emails and custom identifiers"""

    def _create_user(self, student_id, password, **extra_fields):
        """A custom manager to deal with emails and custom identifiers"""
        if not student_id:
            raise ValueError('Users must have a student ID')
        
        user = self.model(student_id=student_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def _create_staff_user(self, email, password, **extra_fields):
        """A custom manager to deal with emails and custom identifiers"""
        if not email:
            raise ValueError('Users must have a email')
        
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_student(self, student_id, password, **extra_fields):
        extra_fields.setdefault('is_student', True)
        return self._create_user(student_id, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("superuser must have is_staff=True")
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser=True')
        
        return self._create_staff_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True, blank=True)
    student_id = models.CharField(max_length=50, unique=True, null=True, blank=True)
    is_student = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        gettext_lazy('staff_status'), default=False,
        help_text=gettext_lazy('designates whether the user can login to this site'),
    )

    is_active = models.BooleanField(
        gettext_lazy('active'), default=True,
        help_text=gettext_lazy('designates whether the user can loin to this site'),
    )

    USERNAME_FIELD = 'email'

    objects = MyUserManager()

    @property
    def identifier(self):
        return self.email or self.student_id

    def __str__(self):
        return self.identifier

    def get_full_name(self):
        return self.identifier

    def get_short_name(self):
        return self.identifier

# profile models gender choices
GENDER_OPT = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=264, blank=True)
    last_name = models.CharField(max_length=15, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_OPT)
    photo = models.ImageField(upload_to=user_directory_path, null=True, default='default/user.jpg')
    date_of_join = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name+"'s profile"
