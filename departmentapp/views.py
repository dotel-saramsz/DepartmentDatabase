from django.shortcuts import render
from django.db import connection,transaction
from . import tables

# Create your views here.


def home(request):
    result = tables.department.getall()
    print(result)
    return render(request,'departmentapp/home.html',{'result':result})

def dashboard(request,dept_id):
    result = tables.department.get("dept_id = '{}'".format(dept_id))
    if not result['error']:
        # try catch block check if empty record is returned through indexing operation
        try:
            #   To get the department details
            result = {'error': False, 'department': result['rows'][0]}

            #   To get the course count of the department
            course_count = tables.course.count("department_id = {}".format(result['department']['dept_id']))
            if(course_count['error']):
                raise Exception('Course Count Error')
            result['course_count'] = course_count['value']

            #   To get the academic staff count of the department
            academic_count = tables.count(tables.join('academic','employee'),'*','department_id = {}'.format(result['department']['dept_id']))
            if(academic_count['error']):
                raise Exception('Academic Staff Count Error')
            result['academic_count'] = academic_count['value']

            #   To get the nonacademic staff count of the department
            nonacademic_count = tables.count(tables.join('nonacademic', 'employee'), '*',
                                          'department_id = {}'.format(result['department']['dept_id']))
            if (nonacademic_count['error']):
                raise Exception('Non-Academic Staff Count Error')
            result['nonacademic_count'] = nonacademic_count['value']

            #   To get the HOD details in a dictionary field 'hod'
            hod_details = tables.get(tables.join('employee','academic'),'salutation,staff_fname,staff_lname,email,mobile_contact,photo_url',
                                     condition='department_id = {} and post_id = {}'.format(result['department']['dept_id'],1))
            if(hod_details['error'] or hod_details['rows'] == [] ):
                raise Exception('HOD Details cannot be retrieved')
            result['hod'] = hod_details['rows'][0]  # Since, only one HOD in each dept, index 0 will only be filled in result

            #   To get the Deputy HOD details in a dictionary field 'dhod'
            dhod_details = tables.get(tables.join('employee', 'academic'),
                                     'salutation,staff_fname,staff_lname,email,mobile_contact,photo_url',
                                     condition='department_id = {} and post_id = {}'.format(
                                         result['department']['dept_id'], 2))
            if (dhod_details['error'] or dhod_details['rows'] == []):
                raise Exception('Deputy HOD Details cannot be retrieved')
            result['dhod'] = dhod_details['rows']  # Since, more than one HOD is possible in a dept, no indexing


        except IndexError as e:
            result = {'error': True, 'message': 'No such department is enlisted in the database'}

        except Exception as e:
            result = {'error': True, 'department': result['department'], 'message': 'There was an error in querying the database: {}'.format(str(e))}

    return render(request,'departmentapp/dashboard.html',{'result':result})

def academic(request,dept_code):
    department_info = tables.department.get('')
    column_names = 'staff_id,salutation,staff_fname,staff_mname,staff_lname,email,mobile_contact,designation'
    result = tables.get(tables.join('academic','employee'),column_names,)
    return render(request,'departmentapp/academic.html')

def nonacademic(request,dept_code):
    return render(request,'departmentapp/nonacademic.html')

def course(request,dept_code):
    return render(request,'departmentapp/course.html')

