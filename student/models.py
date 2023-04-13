from django.db import models

# Models
from accounts.models import User

DEPARTMENT_OPT = (
    ('BCSE','BCSE'),
    ('BSCE','BSCE'),
    ('BSME','BSME'),
    ('BSEEE','BSEEE'),
    ('BBA','BBA'),
    ('BSN','BSN'),
    ('BATHM','BATHM'),
    ('BSAg','BSAg'),
    ('BSAg','BSAg'),
    ('BAEcon','BAEcon'),
    ('BA English','BA English'),
    ('MBA','MBA'),
    ('MPH','MPH'),
)

GENDER_OPT = (
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other'),
)

# Create your models here.
class StudentInfo(models.Model):
    info_of = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_info')
    full_name = models.CharField(max_length=50)
    department = models.CharField(max_length=10, choices=DEPARTMENT_OPT)
    gender = models.CharField(max_length=10, choices=GENDER_OPT, null=True)
    student_phone = models.CharField(max_length=15)
    national_id = models.CharField(max_length=15)
    father_name = models.CharField(max_length=50)
    father_occupation = models.CharField(max_length=30, blank=True, null=True)
    mother_name = models.CharField(max_length=50)
    mother_occupation = models.CharField(max_length=30, null=True, blank=True)
    gardian_name = models.CharField(max_length=50, blank=True, null=True )
    relation_with = models.CharField(max_length=50, blank=True, null=True)
    gardian_occupation = models.CharField(max_length=50, blank=True, null=True)
    gardian_phone = models.CharField(max_length=15)
    dob = models.DateField(auto_now=False, auto_now_add=False, null=True)
    photo = models.ImageField(upload_to='media/student')
    signature = models.ImageField(upload_to='medai/signature', null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.info_of)
    


