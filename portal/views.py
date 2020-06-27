from django.shortcuts import render
from .models import Assignment
from datetime import timedelta, datetime
# Create your views here.
def index(request):
    assignment = Assignment()
    assignment.course = "CS 101"
    assignment.assignment = "500 word essay"
    assignment.assign_date = datetime.now()
    assignment.due_date = datetime.now() + timedelta(days=1)
    assignment.save()
    return render(request, 'index.html', {'assignment': Assignment.objects.all()})