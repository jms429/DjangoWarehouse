from django.urls import path

from . import views

# app_name = 'employees'
urlpatterns = [
    # HOME PAGE 
    path('', views.index, name='index'),
    path('employees', views.employees, name='employees'),
    path('deparments', views.departments, name='departments'),
    path('calendar', views.calendar, name='calendar'),
    path('reference', views.reference, name='reference'),
    path('search', views.search, name='search'),
    path('<int:employee_id>', views.employee, name='employee'),
    path('quality', views.quality, name='quality'),
    path('engineering', views.engineering, name='engineering'),
    path('press_brake', views.press_brake, name='press_brake'),
    path('laser', views.laser, name='laser'),
    path('water_jet', views.water_jet, name='water_jet'),
    path('cnc_mill', views.cnc_mill, name='cnc_mill'),
    path('cnc_lathe', views.cnc_lathe, name='cnc_lathe'),
    path('stamp', views.stamp, name='stamp'),
    path('drill', views.drill, name='drill'),
    path('shipping', views.shipping, name='shipping'),
    path('powder_coat', views.powder_coat, name='powder_coat'),
    path('epoxy', views.epoxy, name='epoxy'),
    path('weld', views.weld, name='weld'),
    path('robot_weld', views.robot_weld, name='robot_weld'),
    path('assembly', views.assembly, name='assembly'),
    path('fuse', views.fuse, name='fuse'),
    path('saw', views.saw, name='saw'),
    path('maintenance', views.maintenance, name='maintenance'),
    path('ju_channel', views.ju_channel, name='ju_channel'),
]