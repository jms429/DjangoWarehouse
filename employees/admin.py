from django.contrib import admin

# Register your models here.
from .models import Employee, Event
from django.contrib.auth.models import User, Group

#unregister the group option from admin 
admin.site.unregister(Group)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'is_active')
    list_filter = ('machine_1', 'machine_2', 'machine_3', 'machine_4','machine_5')

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'event_type')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Event, EventAdmin)
