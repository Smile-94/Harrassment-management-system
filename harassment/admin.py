from django.contrib import admin

# Import Models
from harassment.models import Harassment

# Register your models here.
@admin.register(Harassment)
class HarassmentAdmin(admin.ModelAdmin):
    list_display = ('submit_by','case_id','submitted_date','hearing_date','hearing_time','hearing_room')
    search_fields = ('case_id','submit_by')
    list_per_page = 50
