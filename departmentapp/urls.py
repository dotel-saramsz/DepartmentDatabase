from django.urls import path, include
from . import views

app_name = 'departmentapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('<dept_code>/',views.dashboard, name='dashboard'),
    path('<dept_code>/academic',views.academic,name='academic'),
    path('<dept_code>/academic/add', views.add_academic, name='add_academic'),
    path('<dept_code>/academic/filter', views.filter_academic, name='filter_academic'),
    path('<dept_code>/academic/<staff_id>', views.academic_profile, name='academic_profile'),
    path('<dept_code>/academic/<staff_id>/edit', views.edit_academic, name='edit_academic'),
    path('<dept_code>/nonacademic', views.nonacademic, name='nonacademic'),
    path('<dept_code>/nonacademic/add', views.add_nonacademic, name='add_nonacademic'),
    path('<dept_code>/nonacademic/filter', views.filter_nonacademic, name='filter_nonacademic'),
    path('<dept_code>/nonacademic/<staff_id>', views.nonacademic_profile, name='nonacademic_profile'),
    path('<dept_code>/nonacademic/<staff_id>/edit', views.edit_nonacademic, name='edit_nonacademic'),
    path('<dept_code>/course', views.course, name='course'),
    path('<dept_code>/course/add', views.add_course, name='add_course'),
    path('<dept_code>/course/filter', views.filter_course, name='filter_course'),
    path('<dept_code>/course/<course_code>', views.course_profile, name='course_profile'),
    path('<dept_code>/course/<course_code>/edit', views.edit_course, name='edit_course'),
    path('<dept_code>/ajax/addinstruct/<course_code>', views.add_instruct, name='add_instruct'),
    path('<dept_code>/ajax/deletestaff/<staff_id>', views.delete_employee, name='delete_employee'),
    path('<dept_code>/ajax/deletecourse/<course_code>', views.delete_course, name='delete_course'),
    path('<dept_code>/ajax/<course_code>/removeinstructor', views.remove_instructor, name='remove_instructor'),
    path('test', views.test, name='test'),
]
