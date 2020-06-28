from django.shortcuts import render

from .models import Assignment
from datetime import timedelta, datetime
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    if request.method == 'POST':
        assign = Assignment()
        assign.teacher = request.user
        assign.course = request.user.teacher.course
        assign.assign_date = datetime.now()
        if request.POST['duedate']:
            assign.due_date = request.POST['duedate']
        else:
            assign.due_date = assign.assign_date + timedelta(1)
        assign.save()
        User.objects.get(username=request.POST['id']).student.assignments.add(assign)
    return render(request, 'index.html')
  
# GET /casemanager
def case_manager_landing_page(request):
    return render(request, 'casemanager.html')

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
