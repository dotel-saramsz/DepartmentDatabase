from django.urls import path, include
from . import views

app_name = 'departmentapp'

urlpatterns = [
    path('',views.home,name='home'),
]