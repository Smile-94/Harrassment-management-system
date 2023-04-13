from django.db import models
import datetime

# Import Models
from student.models import StudentInfo

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

ACCUSED_OPT = (
    ('Teacher' , 'Teacher'),
    ('Student' , 'Student'),
    ('Staff' , 'Staff'),
    ('Gaurd' , 'Gaurd'),
    ('Other','Other')
)

class Harassment(models.Model):
    submit_by = models.ForeignKey(StudentInfo, on_delete=models.CASCADE, related_name='report_of')
    case_id = models.CharField( max_length=15, null=True, blank=True)
    submitted_date = models.DateField(auto_now_add=True)
    subject = models.CharField(max_length=150)
    harassment_type = models.CharField(max_length=30, choices=HARASSMENT_OPT)
    occurence_date = models.DateField(auto_now=False, auto_now_add=False)
    accused_name = models.CharField(max_length=50)
    accused_is = models.CharField(max_length=10, choices=ACCUSED_OPT)
    accoused_detail = models.TextField()
    description = models.TextField()
    accept_status = models.BooleanField(default=False)
    decline_status = models.BooleanField(default=False)
    message = models.TextField()
    hearing_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    hearing_time = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    hearing_room = models.CharField(max_length=50)
    proof_file = models.FileField(upload_to='Proof_file', max_length=100)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.case_id:
            year = str(datetime.date.today().year)[2:4]
            month = str(datetime.date.today().month)
            day = str(datetime.date.today().day)
            self.case_id = 'CASE'+year+month+day+str(self.pk).zfill(3)
            self.save()




