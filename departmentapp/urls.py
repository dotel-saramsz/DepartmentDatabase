from django.urls import path, include
from . import views

app_name = 'departmentapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('<dept_code>/',views.dashboard, name='dashboard'),
    path('<dept_code>/academic',views.academic,name='academic'),
    path('<dept_code>/nonacademic', views.nonacademic, name='nonacademic'),
    path('<dept_code>/course', views.course, name='course'),

]
