from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Employee, Event, Department
from django.http import JsonResponse
from datetime import datetime, date

# Create your views here.

def index(request):

    time = date.today()
    upcoming = Event.objects.all().order_by('date')
    event_count = Event.objects.all().count()
    employee_count = Employee.objects.all().count()

    context = {
        'time': time,
        'upcoming': upcoming,
        'event_count': event_count,
        'employee_count': employee_count,
    }

    

    return render(request, 'employees/index.html', context)

def employees(request):

    employee = Employee.objects.all()
    department = Department.objects.all()
    # pagination 
    paginator = Paginator(employee, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    # sidebar name search autofill.. to search every letter use ... full_name__istartswith=request.GET.get('term')
    if 'term' in request.GET:
        qs = Employee.objects.filter(full_name__istartswith=request.GET.get('term'))
        names = list()
        for employee in qs:
            names.append(employee.full_name)
        return JsonResponse(names, safe=False)
   
    context = {
        'employee': paged_listings,
        'departments': department,
    }

    return render(request, 'employees/employees.html', context)

def employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    departments = Department.objects.all()
    context = { 
        'employee': employee,
        'departments': departments,
    }
    return render(request, 'employees/employee.html', context)

def reference(request):
    data = Department.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'employees/reference.html', context)

def departments(request):

    departments = Department.objects.all().order_by('id')
    # Quality
    none_1 = Employee.objects.filter(quality__contains=0).count()
    beg_1 = Employee.objects.filter(quality__contains=1).count()
    int_1 = Employee.objects.filter(quality__contains=2).count()
    nov_1 = Employee.objects.filter(quality__contains=3).count()
    exp_1 = Employee.objects.filter(quality__contains=4).count()
    #Engineering
    none_2 = Employee.objects.filter(engineering__contains=0).count()
    beg_2 = Employee.objects.filter(engineering__contains=1).count()
    int_2 = Employee.objects.filter(engineering__contains=2).count()
    nov_2 = Employee.objects.filter(engineering__contains=3).count()
    exp_2 = Employee.objects.filter(engineering__contains=4).count()
    #Press Brake
    none_3 = Employee.objects.filter(press_brake__contains=0).count()
    beg_3 = Employee.objects.filter(press_brake__contains=1).count()
    int_3 = Employee.objects.filter(press_brake__contains=2).count()
    nov_3 = Employee.objects.filter(press_brake__contains=3).count()
    exp_3 = Employee.objects.filter(press_brake__contains=4).count()
    #laser
    none_4 = Employee.objects.filter(laser__contains=0).count()
    beg_4 = Employee.objects.filter(laser__contains=1).count()
    int_4 = Employee.objects.filter(laser__contains=2).count()
    nov_4 = Employee.objects.filter(laser__contains=3).count()
    exp_4 = Employee.objects.filter(laser__contains=4).count()
    #water_jet
    none_5 = Employee.objects.filter(water_jet__contains=0).count()
    beg_5 = Employee.objects.filter(water_jet__contains=1).count()
    int_5 = Employee.objects.filter(water_jet__contains=2).count()
    nov_5 = Employee.objects.filter(water_jet__contains=3).count()
    exp_5 = Employee.objects.filter(water_jet__contains=4).count()
    #cnc_mill
    none_6 = Employee.objects.filter(cnc_mill__contains=0).count()
    beg_6 = Employee.objects.filter(cnc_mill__contains=1).count()
    int_6 = Employee.objects.filter(cnc_mill__contains=2).count()
    nov_6 = Employee.objects.filter(cnc_mill__contains=3).count()
    exp_6 = Employee.objects.filter(cnc_mill__contains=4).count()
    #cnc_lathe
    none_7 = Employee.objects.filter(cnc_lathe__contains=0).count()
    beg_7 = Employee.objects.filter(cnc_lathe__contains=1).count()
    int_7 = Employee.objects.filter(cnc_lathe__contains=2).count()
    nov_7 = Employee.objects.filter(cnc_lathe__contains=3).count()
    exp_7 = Employee.objects.filter(cnc_lathe__contains=4).count()
    #stamp
    none_8 = Employee.objects.filter(stamp__contains=0).count()
    beg_8 = Employee.objects.filter(stamp__contains=1).count()
    int_8 = Employee.objects.filter(stamp__contains=2).count()
    nov_8 = Employee.objects.filter(stamp__contains=3).count()
    exp_8 = Employee.objects.filter(stamp__contains=4).count()
    #drill
    none_9 = Employee.objects.filter(drill__contains=0).count()
    beg_9 = Employee.objects.filter(drill__contains=1).count()
    int_9 = Employee.objects.filter(drill__contains=2).count()
    nov_9 = Employee.objects.filter(drill__contains=3).count()
    exp_9 = Employee.objects.filter(drill__contains=4).count()
    #shipping
    none_10 = Employee.objects.filter(shipping__contains=0).count()
    beg_10 = Employee.objects.filter(shipping__contains=1).count()
    int_10 = Employee.objects.filter(shipping__contains=2).count()
    nov_10 = Employee.objects.filter(shipping__contains=3).count()
    exp_10 = Employee.objects.filter(shipping__contains=4).count()
    #powder_coat
    none_11 = Employee.objects.filter(powder_coat__contains=0).count()
    beg_11 = Employee.objects.filter(powder_coat__contains=1).count()
    int_11 = Employee.objects.filter(powder_coat__contains=2).count()
    nov_11 = Employee.objects.filter(powder_coat__contains=3).count()
    exp_11 = Employee.objects.filter(powder_coat__contains=4).count()
    #epoxy
    none_12 = Employee.objects.filter(epoxy__contains=0).count()
    beg_12 = Employee.objects.filter(epoxy__contains=1).count()
    int_12 = Employee.objects.filter(epoxy__contains=2).count()
    nov_12 = Employee.objects.filter(epoxy__contains=3).count()
    exp_12 = Employee.objects.filter(epoxy__contains=4).count()
    #weld
    none_13 = Employee.objects.filter(weld__contains=0).count()
    beg_13 = Employee.objects.filter(weld__contains=1).count()
    int_13 = Employee.objects.filter(weld__contains=2).count()
    nov_13 = Employee.objects.filter(weld__contains=3).count()
    exp_13 = Employee.objects.filter(weld__contains=4).count()
    #robot_weld
    none_14 = Employee.objects.filter(robot_weld__contains=0).count()
    beg_14 = Employee.objects.filter(robot_weld__contains=1).count()
    int_14 = Employee.objects.filter(robot_weld__contains=2).count()
    nov_14 = Employee.objects.filter(robot_weld__contains=3).count()
    exp_14 = Employee.objects.filter(robot_weld__contains=4).count()
    #assembly
    none_15 = Employee.objects.filter(assembly__contains=0).count()
    beg_15 = Employee.objects.filter(assembly__contains=1).count()
    int_15 = Employee.objects.filter(assembly__contains=2).count()
    nov_15 = Employee.objects.filter(assembly__contains=3).count()
    exp_15 = Employee.objects.filter(assembly__contains=4).count()
     #fuse
    none_16 = Employee.objects.filter(fuse__contains=0).count()
    beg_16 = Employee.objects.filter(fuse__contains=1).count()
    int_16 = Employee.objects.filter(fuse__contains=2).count()
    nov_16 = Employee.objects.filter(fuse__contains=3).count()
    exp_16 = Employee.objects.filter(fuse__contains=4).count()
    #saw
    none_17 = Employee.objects.filter(saw__contains=0).count()
    beg_17 = Employee.objects.filter(saw__contains=1).count()
    int_17 = Employee.objects.filter(saw__contains=2).count()
    nov_17 = Employee.objects.filter(saw__contains=3).count()
    exp_17 = Employee.objects.filter(saw__contains=4).count()
    #maintenance
    none_18 = Employee.objects.filter(maintenance__contains=0).count()
    beg_18 = Employee.objects.filter(maintenance__contains=1).count()
    int_18 = Employee.objects.filter(maintenance__contains=2).count()
    nov_18 = Employee.objects.filter(maintenance__contains=3).count()
    exp_18 = Employee.objects.filter(maintenance__contains=4).count()
     #ju_channel
    none_19 = Employee.objects.filter(ju_channel__contains=0).count()
    beg_19 = Employee.objects.filter(ju_channel__contains=1).count()
    int_19 = Employee.objects.filter(ju_channel__contains=2).count()
    nov_19 = Employee.objects.filter(ju_channel__contains=3).count()
    exp_19 = Employee.objects.filter(ju_channel__contains=4).count()
    
    context = {
        # Quality
        'departments': departments,
        'none_1': none_1,
        'beg_1': beg_1,
        'int_1': int_1,
        'nov_1': nov_1,
        'exp_1': exp_1,
        #Engineering
        'none_2': none_2,
        'beg_2': beg_2,
        'int_2': int_2,
        'nov_2': nov_2,
        'exp_2': exp_2,
        #press_brake
        'none_3': none_3,
        'beg_3': beg_3,
        'int_3': int_3,
        'nov_3': nov_3,
        'exp_3': exp_3,
        #laser
        'none_4': none_4,
        'beg_4': beg_4,
        'int_4': int_4,
        'nov_4': nov_4,
        'exp_4': exp_4,
        #water_jet
        'none_5': none_5,
        'beg_5': beg_5,
        'int_5': int_5,
        'nov_5': nov_5,
        'exp_5': exp_5,
        #cnc_mill
        'none_6': none_6,
        'beg_6': beg_6,
        'int_6': int_6,
        'nov_6': nov_6,
        'exp_6': exp_6,
        #cnc_lathe
        'none_7': none_7,
        'beg_7': beg_7,
        'int_7': int_7,
        'nov_7': nov_7,
        'exp_7': exp_7,
        #stamp
        'none_8': none_8,
        'beg_8': beg_8,
        'int_8': int_8,
        'nov_8': nov_8,
        'exp_8': exp_8,
        #drill
        'none_9': none_9,
        'beg_9': beg_9,
        'int_9': int_9,
        'nov_9': nov_9,
        'exp_9': exp_9,
        #shipping
        'none_10': none_10,
        'beg_10': beg_10,
        'int_10': int_10,
        'nov_10': nov_10,
        'exp_10': exp_10,
        #powder_coat
        'none_11': none_11,
        'beg_11': beg_11,
        'int_11': int_11,
        'nov_11': nov_11,
        'exp_11': exp_11,
        #epoxy
        'none_12': none_12,
        'beg_12': beg_12,
        'int_12': int_12,
        'nov_12': nov_12,
        'exp_12': exp_12,
        #weld
        'none_13': none_13,
        'beg_13': beg_13,
        'int_13': int_13,
        'nov_13': nov_13,
        'exp_13': exp_13,
        #robot_weld
        'none_14': none_14,
        'beg_14': beg_14,
        'int_14': int_14,
        'nov_14': nov_14,
        'exp_14': exp_14,
        #assembly
        'none_15': none_15,
        'beg_15': beg_15,
        'int_15': int_15,
        'nov_15': nov_15,
        'exp_15': exp_15,
        #fuse
        'none_16': none_16,
        'beg_16': beg_16,
        'int_16': int_16,
        'nov_16': nov_16,
        'exp_16': exp_16,
        #saw
        'none_17': none_17,
        'beg_17': beg_17,
        'int_17': int_17,
        'nov_17': nov_17,
        'exp_17': exp_17,
        #maint
        'none_18': none_18,
        'beg_18': beg_18,
        'int_18': int_18,
        'nov_18': nov_18,
        'exp_18': exp_18,
        #j/u Channel
        'none_19': none_19,
        'beg_19': beg_19,
        'int_19': int_19,
        'nov_19': nov_19,
        'exp_19': exp_19,
    }

    return render(request, 'employees/departments.html', context)

def calendar(request):

    month = datetime.today().strftime("%B")
    year = datetime.today().strftime("%Y")
   

    context = {
       'current_month': month,
       'current_year': year,
    }

    return render(request, 'calendar/calendar.html', context)

def search(request):
     # this is the actual search function
    queryset_list = Employee.objects.all()

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(full_name__icontains=keywords)

    if 'quality' in request.GET:
        quality = request.GET['quality']
        if quality:
            queryset_list = queryset_list.filter(quality__gte=quality)
            
    if 'engineering' in request.GET:
        engineering = request.GET['engineering']
        if engineering:
            queryset_list = queryset_list.filter(engineering__gte=engineering)

    if 'press_brake' in request.GET:
        press_brake = request.GET['press_brake']
        if press_brake:
            queryset_list = queryset_list.filter(press_brake__gte=press_brake)

    if 'laser' in request.GET:
        laser = request.GET['laser']
        if laser:
            queryset_list = queryset_list.filter(laser__gte=laser)

    if 'water_jet' in request.GET:
        water_jet = request.GET['water_jet']
        if water_jet:
            queryset_list = queryset_list.filter(water_jet__gte=water_jet)

    if 'cnc_mill' in request.GET:
        cnc_mill = request.GET['cnc_mill']
        if cnc_mill:
            queryset_list = queryset_list.filter(cnc_mill__gte=cnc_mill)

    if 'cnc_lathe' in request.GET:
        cnc_lathe = request.GET['cnc_lathe']
        if cnc_lathe:
            queryset_list = queryset_list.filter(cnc_lathe__gte=cnc_lathe)

    if 'stamp' in request.GET:
        stamp = request.GET['stamp']
        if stamp:
            queryset_list = queryset_list.filter(stamp__gte=stamp)

    if 'drill' in request.GET:
        drill = request.GET['drill']
        if drill:
            queryset_list = queryset_list.filter(drill__gte=drill)

    if 'shipping' in request.GET:
        shipping = request.GET['shipping']
        if shipping:
            queryset_list = queryset_list.filter(shipping__gte=shipping)

    if 'powder_coat' in request.GET:
        powder_coat = request.GET['powder_coat']
        if powder_coat:
            queryset_list = queryset_list.filter(powder_coat__gte=powder_coat)

    if 'epoxy' in request.GET:
        epoxy = request.GET['epoxy']
        if epoxy:
            queryset_list = queryset_list.filter(epoxy__gte=epoxy)

    if 'weld' in request.GET:
        weld = request.GET['weld']
        if weld:
            queryset_list = queryset_list.filter(weld__gte=weld)

    if 'robot_weld' in request.GET:
        robot_weld = request.GET['robot_weld']
        if robot_weld:
            queryset_list = queryset_list.filter(robot_weld__gte=robot_weld)

    if 'assembly' in request.GET:
        assembly = request.GET['assembly']
        if assembly:
            queryset_list = queryset_list.filter(assembly__gte=assembly)

    if 'fuse' in request.GET:
        fuse = request.GET['fuse']
        if fuse:
            queryset_list = queryset_list.filter(fuse__gte=fuse)

    if 'saw' in request.GET:
        saw = request.GET['saw']
        if saw:
            queryset_list = queryset_list.filter(saw__gte=saw)
    
    if 'maintenance' in request.GET:
        maintenance = request.GET['maintenance']
        if maintenance:
            queryset_list = queryset_list.filter(maintenance__gte=maintenance)

    if 'ju_channel' in request.GET:
        ju_channel = request.GET['ju_channel']
        if ju_channel:
            queryset_list = queryset_list.filter(ju_channel__gte=ju_channel)





    context = {
        'employees': queryset_list,
    }

    return render(request, 'employees/search.html', context)


#individual departments
def quality(request):
    data = Employee.objects.all().order_by('-quality')
    context = {
        'data': data,
    }
    return render(request, 'machines/quality.html', context)

def engineering(request):
    data = Employee.objects.all().order_by('-engineering')
    context = {
        'data': data,
    }
    return render(request, 'machines/engineering.html', context)

def press_brake(request):
    data = Employee.objects.all().order_by('-press_brake')
    context = {
        'data': data,
    }
    return render(request, 'machines/press_brake.html', context)

def laser(request):
    data = Employee.objects.all().order_by('-laser')
    context = {
        'data': data,
    }
    return render(request, 'machines/laser.html', context)

def water_jet(request):
    data = Employee.objects.all().order_by('-water_jet')
    context = {
        'data': data,
    }
    return render(request, 'machines/water_jet.html', context)

def cnc_mill(request):
    data = Employee.objects.all().order_by('-cnc_mill')
    context = {
        'data': data,
    }
    return render(request, 'machines/cnc_mill.html', context)

def cnc_lathe(request):
    data = Employee.objects.all().order_by('-cnc_lathe')
    context = {
        'data': data,
    }
    return render(request, 'machines/cnc_lathe.html', context)

def stamp(request):
    data = Employee.objects.all().order_by('-stamp')
    context = {
        'data': data,
    }
    return render(request, 'machines/stamp.html', context)

def drill(request):
    data = Employee.objects.all().order_by('-drill')
    context = {
        'data': data,
    }
    return render(request, 'machines/drill.html', context)

def shipping(request):
    data = Employee.objects.all().order_by('-shipping')
    context = {
        'data': data,
    }
    return render(request, 'machines/shipping.html', context)

def powder_coat(request):
    data = Employee.objects.all().order_by('-powder_coat')
    context = {
        'data': data,
    }
    return render(request, 'machines/powder_coat.html', context)

def epoxy(request):
    data = Employee.objects.all().order_by('-epoxy')
    context = {
        'data': data,
    }
    return render(request, 'machines/epoxy.html', context)

def weld(request):
    data = Employee.objects.all().order_by('-weld')
    context = {
        'data': data,
    }
    return render(request, 'machines/weld.html', context)

def robot_weld(request):
    data = Employee.objects.all().order_by('-robot_weld')
    context = {
        'data': data,
    }
    return render(request, 'machines/robot_weld.html', context)

def assembly(request):
    data = Employee.objects.all().order_by('-assembly')
    context = {
        'data': data,
    }
    return render(request, 'machines/assembly.html', context)

def fuse(request):
    data = Employee.objects.all().order_by('-fuse')
    context = {
        'data': data,
    }
    return render(request, 'machines/fuse.html', context)

def saw(request):
    data = Employee.objects.all().order_by('-saw')
    context = {
        'data': data,
    }
    return render(request, 'machines/saw.html', context)

def maintenance(request):
    data = Employee.objects.all().order_by('-maintenance')
    context = {
        'data': data,
    }
    return render(request, 'machines/maintenance.html', context)

def ju_channel(request):
    data = Employee.objects.all().order_by('-ju_channel')
    context = {
        'data': data,
    }
    return render(request, 'machines/ju_channel.html', context)
