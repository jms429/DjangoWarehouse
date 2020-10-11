from django.urls import path

from . import views

# app_name = 'employees'
urlpatterns = [
    # HOME PAGE 
    
    path('', views.index, name='index'),
    path('employees', views.employees, name='employees'),
    path('machines', views.machines, name='machines'),
    path('calendar', views.calendar, name='calendar'),
    path('search', views.search, name='search'),
    path('<int:employee_id>', views.employee, name='employee'),
    path('machine_1', views.machine_1, name='machine_1'),
    path('machine_2', views.machine_2, name='machine_2'),
    path('machine_3', views.machine_3, name='machine_3'),
    path('machine_4', views.machine_4, name='machine_4'),
    path('machine_5', views.machine_5, name='machine_5'),
]