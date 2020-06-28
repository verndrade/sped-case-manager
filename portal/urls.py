from django.urls import path
from . import views
from django.conf import settings

app_name = 'portal'
urlpatterns = [
    path('', views.index, name="index"),
    path('casemanager/', views.case_manager_landing_page, name="casemanager"),
    path('casemanager/student', views.student, name="student"),
    path('casemanager/student/assignments', views.assignments, name="assignments"),
    path('casemanager/student/iep', views.iep, name="iep"),
    path('casemanager/student/discipline', views.discipline, name="discipline"),
    path('landingpage/', views.landing_page, name="landingpage"),
]