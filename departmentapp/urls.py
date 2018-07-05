from django.urls import path, include
from . import views

app_name = 'departmentapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('<dept_code>/',views.dashboard, name='dashboard'),
    path('<dept_code>/academic',views.academic,name='academic'),
    path('<dept_code>/academic/add', views.add_academic, name='add_academic'),
    path('<dept_code>/nonacademic', views.nonacademic, name='nonacademic'),
    path('<dept_code>/nonacademic/add', views.nonacademic, name='add_nonacademic'),
    path('<dept_code>/course', views.course, name='course'),
    path('<dept_code>/course/add', views.course, name='add_course'),
]
