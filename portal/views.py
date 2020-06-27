from django.shortcuts import render
from .models import Assignment
from datetime import timedelta, datetime
# Create your views here.
def index(request):
    return render(request, 'index.html')