from django.contrib import admin
from .models import Assignment, TeacherProfile, StudentProfile

# Register your models here.

admin.site.register(Assignment)
admin.site.register(TeacherProfile)
admin.site.register(StudentProfile)