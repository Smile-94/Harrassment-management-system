from django.contrib import admin

# models
from accounts.models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('email','is_staff','is_active')
    search_fields=('email',)
    list_filter=('email',)
    list_per_page=50