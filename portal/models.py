from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.timezone import make_aware

# Create your models here.
class Assignment(models.Model):
    course = models.CharField(max_length=200)
    assignment = models.CharField(max_length=200)
    assign_date = models.DateTimeField('date assigned')
    due_date = models.DateTimeField('date published')
    teacher = models.CharField(max_length=200, default="teacher")
    

class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student')
    assignments = models.ManyToManyField(Assignment, related_name="students")


class TeacherProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='teacher')
    students = models.ManyToManyField(StudentProfile, related_name="teachers")
    cases = models.ManyToManyField(StudentProfile, related_name="case_manager")
    course = models.CharField(max_length=200, default="Algebra")