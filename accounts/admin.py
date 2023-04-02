from django.contrib import admin

# models
from accounts.models import User
from accounts.models import Profile

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('email','is_staff','is_student','is_active')
    search_fields=('email',)
    list_filter=('email',)
    list_per_page=50

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','first_name','last_name','gender','date_of_join')
    search_fields=('user','first_name','date_of_join')
    list_filter=('gender',)
    aw_id_fields=('user',)
    list_per_page=50