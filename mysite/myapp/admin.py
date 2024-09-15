from django.contrib import admin
from .models import employee 

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['name','state']
admin.site.register(employee,EmployeeAdmin)