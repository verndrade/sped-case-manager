from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Assignment(models.Model):
    course = models.CharField(max_length=200)
    assignment = models.CharField(max_length=200)
    assign_date = models.DateTimeField('date assigned')
    due_date = models.DateTimeField('date published')
    

class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student')
    assignments = models.ManyToManyField(Assignment)


class TeacherProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='teacher')
    students = models.ManyToManyField(StudentProfile)
