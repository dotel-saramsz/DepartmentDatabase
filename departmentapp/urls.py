from django.urls import path, include
from . import views

app_name = 'departmentapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('<dept_code>/',views.dashboard, name='dashboard')
]
