from django.urls import path
from . import views
from django.conf import settings

app_name = 'portal'
urlpatterns = [
    path('', views.index, name="index"),
]