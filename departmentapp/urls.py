from django.urls import path, include
from . import views

app_name = 'departmentapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('<dept_id>/',views.dashboard, name='dashboard'),
    path('<dept_id>/academic',views.academic,name='academic'),
    path('<dept_id>/nonacademic', views.nonacademic, name='nonacademic'),
    path('<dept_id>/course', views.course, name='course'),

]
