from django.shortcuts import render
from django.db import connection,transaction
from . import tables

# Create your views here.


def home(request):
    result = tables.department.getall()
    print(result)
    return render(request,'departmentapp/home.html',{'result':result})

def dashboard(request,dept_code):
    result = tables.department.get("dept_code = '{}'".format(dept_code))
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
    result = tables.department.get("dept_code = '{}'".format(dept_code))
    if not result['error']:
        # try catch block check if empty record is returned through indexing operation
        try:
            #   To get the department details
            result = {'error': False, 'department': result['rows'][0]}

            #   To get the entire list of academic staffs in that department
            column_names = 'staff_id,salutation,staff_fname,staff_mname,staff_lname,email,mobile_contact,designation'
            staff_list = tables.get(tables.join('academic','employee'),column_names,'department_id = {}'.format(result['department']['dept_id']))
            if staff_list['error']:
                raise Exception('Academic Staff retrieval error')
            result['staff_list'] = staff_list['rows']

        except IndexError as e:
            result = {'error': True, 'message': 'No such department is enlisted in the database'}

        except Exception as e:
            result = {'error': True, 'department': result['department'],
                      'message': 'There was an error in querying the database: {}'.format(str(e))}

    return render(request, 'departmentapp/academic.html', {'result': result})


def nonacademic(request,dept_code):
    result = tables.department.get("dept_code = '{}'".format(dept_code))
    if not result['error']:
        # try catch block check if empty record is returned through indexing operation
        try:
            #   To get the department details
            result = {'error': False, 'department': result['rows'][0]}

            #   To get the entire list of academic staffs in that department
            column_names = 'staff_id,staff_fname,staff_mname,staff_lname,email,mobile_contact,post_name'
            staff_list = tables.get(tables.join(tables.join('nonacademic', 'employee'),'nonacademic_post','left',
                                                on='nonacademic.post_id=nonacademic_post.post_id'), column_names,
                                    'department_id = {}'.format(result['department']['dept_id']))
            if staff_list['error']:
                raise Exception('Non-Academic Staff retrieval error')
            result['staff_list'] = staff_list['rows']

        except IndexError as e:
            result = {'error': True, 'message': 'No such department is enlisted in the database'}

        except Exception as e:
            result = {'error': True, 'department': result['department'],
                      'message': 'There was an error in querying the database: {}'.format(str(e))}

    return render(request, 'departmentapp/nonacademic.html', {'result': result})


def course(request,dept_code):
    result = tables.department.get("dept_code = '{}'".format(dept_code))
    if not result['error']:
        # try catch block check if empty record is returned through indexing operation
        try:
            #   To get the department details
            result = {'error': False, 'department': result['rows'][0]}

            #   To get the entire list of academic staffs in that department
            column_names = 'course_code,course_name'
            course_list = tables.course.get('department_id = {}'.format(result['department']['dept_id']),column_names)
            if course_list['error']:
                raise Exception('Course List retrieval error')
            result['course_list'] = course_list['rows']

        except IndexError as e:
            result = {'error': True, 'message': 'No such department is enlisted in the database'}

        except Exception as e:
            result = {'error': True, 'department': result['department'],
                      'message': 'There was an error in querying the database: {}'.format(str(e))}

    return render(request, 'departmentapp/course.html', {'result': result})


def add_academic(request,dept_code):
    #   This function needs to handle get request to cater new form and post request to manage form submissions
    result = tables.department.get("dept_code = '{}'".format(dept_code))
    if not result['error']:
        try:
            #   To get the department details
            result = {'error': False, 'department': result['rows'][0]}

            #   To get the available posts' list for form dropdown
            postlist = tables.academic_post.getall()
            if postlist['error']:
                raise Exception('Post List retrieval error')
            result['postlist'] = postlist['rows']

            #   To get the course catered by the department for the form dropdown
            courselist = tables.course.get('department_id = {}'.format(result['department']['dept_id']))
            if courselist['error']:
                raise Exception('Available Course List retrieval error')
            result['courselist'] = courselist['rows']

        except IndexError as e:
            result = {'error': True, 'message': 'No such department is enlisted in the database'}

        except Exception as e:
            result = {'error': True, 'department': result['department'],
                      'message': 'There was an error in querying the database: {}'.format(str(e))}

    if request.method == 'GET':
        return render(request, 'departmentapp/addacademic.html', {'result': result})

    elif request.method == 'POST':
        print(request.POST)
        formdata = dict(request.POST.copy())
        # Here, we need to insert to 3 tables based on the submitted data: employee, academic and canteach
        try:
            # Insert into employee table
            employeeInsert = tables.employee.insert(int(formdata.get('staff_id')[0]),formdata.get('staff_fname')[0],
                                                    formdata.get('staff_mname')[0],formdata.get('staff_lname')[0],
                                                    None,formdata.get('email')[0],int(formdata.get('home_contact')[0]),
                                                    int(formdata.get('mobile_contact')[0]),formdata.get('address')[0],
                                                    result['department']['dept_id'])
            if employeeInsert['error']:
                print('Error in inserting employee details ' + employeeInsert['message'])
                raise Exception('Error in inserting employee details '+employeeInsert['message'])
            # Insert into academic table
            academicInsert = tables.academic.insert(int(formdata.get('staff_id')[0]),formdata.get('salutation')[0],
                                                    formdata.get('designation')[0],formdata.get('service_type')[0],
                                                    formdata.get('contract_type')[0],formdata.get('qualification')[0],
                                                    None if formdata.get('post_id')[0] == '' else int(
                                                        formdata.get('post_id')[0]))
            if academicInsert['error']:
                print('Error in inserting academic details ' + academicInsert['message'])
                raise Exception('Error in inserting academic details ' + academicInsert['message'])
            # Insert into canteach table
            for eachcourse in formdata.get('course_id'):
                canteachInsert = tables.canteach.insert(int(formdata.get('staff_id')[0]),eachcourse)
                if canteachInsert['error']:
                    print('Error in inserting course details ' + canteachInsert['message'])
                    raise Exception('Error in inserting course details '+ canteachInsert['message'])
            submissionresult = {'error': False, 'message': 'DONE: Successfully registered the academic staff with staff ID: {}'.format(formdata.get('staff_id')[0])}

        except Exception as e:
             submissionresult = {'error': True, 'message': 'REGISTRATION ERROR: '+ str(e)}

        return render(request, 'departmentapp/addacademic.html', {'result': result, 'submissionresult': submissionresult})
