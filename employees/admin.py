from django.contrib import admin

# Register your models here.
from .models import Employee, Event, Department
from django.contrib.auth.models import User, Group

#unregister the group option from admin 
admin.site.unregister(Group)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'is_active')

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'event_type')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Department, DepartmentAdmin)
