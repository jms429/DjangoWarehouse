from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Employee, Event
from django.http import JsonResponse
from datetime import datetime, date

# Create your views here.

def index(request):

    time = date.today()
    upcoming = Event.objects.all().order_by('date')

    context = {
        'time': time,
        'upcoming': upcoming,
    }

    

    return render(request, 'employees/index.html', context)

def employees(request):

    employee = Employee.objects.all()
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
    }

    return render(request, 'employees/employees.html', context)

def employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    context = { 
        'employee': employee
    }
    return render(request, 'employees/employee.html', context)

def machines(request):

    #machine 1
    mach1_none = Employee.objects.filter(machine_1__contains=0).count()
    mach1_beginner = Employee.objects.filter(machine_1__contains=1).count()
    mach1_inter = Employee.objects.filter(machine_1__contains=2).count()
    mach1_novice = Employee.objects.filter(machine_1__contains=3).count()
    mach1_expert = Employee.objects.filter(machine_1__contains=4).count()
    #machine 2
    mach2_none = Employee.objects.filter(machine_2__contains=0).count()
    mach2_beginner = Employee.objects.filter(machine_2__contains=1).count()
    mach2_inter = Employee.objects.filter(machine_2__contains=2).count()
    mach2_novice = Employee.objects.filter(machine_2__contains=3).count()
    mach2_expert = Employee.objects.filter(machine_2__contains=4).count()
    #machine 3
    mach3_none = Employee.objects.filter(machine_3__contains=0).count()
    mach3_beginner = Employee.objects.filter(machine_3__contains=1).count()
    mach3_inter = Employee.objects.filter(machine_3__contains=2).count()
    mach3_novice = Employee.objects.filter(machine_3__contains=3).count()
    mach3_expert = Employee.objects.filter(machine_3__contains=4).count()
    #machine 4
    mach4_none = Employee.objects.filter(machine_4__contains=0).count()
    mach4_beginner = Employee.objects.filter(machine_4__contains=1).count()
    mach4_inter = Employee.objects.filter(machine_4__contains=2).count()
    mach4_novice = Employee.objects.filter(machine_4__contains=3).count()
    mach4_expert = Employee.objects.filter(machine_4__contains=4).count()
    #machine 5
    mach5_none = Employee.objects.filter(machine_5__contains=0).count()
    mach5_beginner = Employee.objects.filter(machine_5__contains=1).count()
    mach5_inter = Employee.objects.filter(machine_5__contains=2).count()
    mach5_novice = Employee.objects.filter(machine_5__contains=3).count()
    mach5_expert = Employee.objects.filter(machine_5__contains=4).count()


    context = {
        'mach1_none' : mach1_none,
        'mach1_beginner' : mach1_beginner,
        'mach1_inter' : mach1_inter,
        'mach1_novice' : mach1_novice,
        'mach1_expert' : mach1_expert,
        'mach2_none' : mach2_none,
        'mach2_beginner' : mach2_beginner,
        'mach2_inter' : mach2_inter,
        'mach2_novice' : mach2_novice,
        'mach2_expert' : mach2_expert,
        'mach3_none' : mach3_none,
        'mach3_beginner' : mach3_beginner,
        'mach3_inter' : mach3_inter,
        'mach3_novice' : mach3_novice,
        'mach3_expert' : mach3_expert,
        'mach4_none' : mach4_none,
        'mach4_beginner' : mach4_beginner,
        'mach4_inter' : mach4_inter,
        'mach4_novice' : mach4_novice,
        'mach4_expert' : mach4_expert,
        'mach5_none' : mach5_none,
        'mach5_beginner' : mach5_beginner,
        'mach5_inter' : mach5_inter,
        'mach5_novice' : mach5_novice,
        'mach5_expert' : mach5_expert,
    }

    return render(request, 'machines/machines.html', context)

def machine_1(request):

    ltg = Employee.objects.all().order_by('-machine_1')
    
    context = { 
        'ltg': ltg
    }


    return render(request, 'machines/machine/1.html', context)

def machine_2(request):

    ltg = Employee.objects.all().order_by('-machine_2')
    
    context = { 
        'ltg': ltg
    }


    return render(request, 'machines/machine/2.html', context)

def machine_3(request):

    ltg = Employee.objects.all().order_by('-machine_3')
    
    context = { 
        'ltg': ltg
    }

    return render(request, 'machines/machine/3.html', context)

def machine_4(request):

    ltg = Employee.objects.all().order_by('-machine_4')
    
    context = { 
        'ltg': ltg
    }

    return render(request, 'machines/machine/4.html', context)

def machine_5(request):

    ltg = Employee.objects.all().order_by('-machine_5')
    
    context = { 
        'ltg': ltg
    }

    return render(request, 'machines/machine/5.html', context)

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

    context = {
        'employees': queryset_list,
    }

    return render(request, 'employees/search.html', context)

    
