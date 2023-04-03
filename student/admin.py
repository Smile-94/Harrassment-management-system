from django.contrib import admin

# Models
from student.models import StudentInfo

# Register your models here.
@admin.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ('info_of','full_name','department','student_phone','dob')
    list_per_page = 50
