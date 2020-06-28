from django.shortcuts import render, redirect

from .models import Assignment
from datetime import timedelta, datetime
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('/admin')
        
    if request.method == 'POST':
        assign = Assignment()
        assign.teacher = request.user
        assign.assignment = request.POST['assignment']
        assign.course = request.user.teacher.course
        assign.assign_date = datetime.now()
        if request.POST['duedate']:
            assign.due_date = request.POST['duedate']
        else:
            assign.due_date = assign.assign_date + timedelta(1)
        assign.save()
        for i in request.user.teacher.students.all():
            i.assignments.add(assign)
    return render(request, 'index.html')
  
# GET /casemanager
def case_manager_landing_page(request):
    return render(request, 'casemanager.html')

# GET /casemanager
def search(request):
    found = False
    if request.method == 'POST':
        if ' ' in request.POST['search']:
            search = request.POST['search'].split(" ")
            found = User.objects.filter(first_name__icontains=search[0]).filter(last_name__icontains=search[1])
        else:
            found = User.objects.filter(first_name__icontains=request.POST['search']) | User.objects.filter(last_name__icontains=request.POST['search'])
    return render(request, 'search.html', {'found': found})

# GET /casemanager/student
def student(request):
    return render(request, 'student.html')

# GET /casemanager/student/assignments
def assignments(request):
    return render(request, 'assignments.html')

# GET /casemanager/student/iep
def iep(request):
    return render(request, 'iep.html')

# GET /casemanager/student/discipline
def discipline(request):
    return render(request, 'discipline.html')

# GET /landingpage 
def landing_page(request): 
    return render(request, 'landingpage.html')
