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