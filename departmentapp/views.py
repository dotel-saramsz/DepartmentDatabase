from django.shortcuts import render, redirect
from django.db import connection,transaction
from django.conf import settings
from django.utils.datastructures import MultiValueDictKeyError
import os
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
            hod_details = tables.get(tables.join('employee','academic'),'salutation,staff_id,staff_fname,staff_lname,email,mobile_contact,photo_url',
                                     condition='department_id = {} and post_id = {}'.format(result['department']['dept_id'],1))
            if(hod_details['error'] or hod_details['rows'] == [] ):
                raise Exception('HOD Details cannot be retrieved')
            result['hod'] = hod_details['rows'][0]  # Since, only one HOD in each dept, index 0 will only be filled in result

            #   To get the Deputy HOD details in a dictionary field 'dhod'
            dhod_details = tables.get(tables.join('employee', 'academic'),
                                     'salutation,staff_id,staff_fname,staff_lname,email,mobile_contact,photo_url',
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
            staff_list = tables.get('academicsummary',column_names,'department_id = {}'.format(result['department']['dept_id']))
            if staff_list['error']:
                raise Exception('Academic Staff retrieval error')
            result['staff_list'] = staff_list['rows']

            #   To get the post list for filtering
            post_list = tables.academic_post.getall()
            if not post_list['error']:
                result['postlist'] = post_list['rows']

        except IndexError as e:
            result = {'error': True, 'message': 'No such department is enlisted in the database'}

        except Exception as e:
            result = {'error': True, 'department': result['department'],
                      'message': 'There was an error in querying the database: {}'.format(str(e))}

    return render(request, 'departmentapp/academic.html', {'result': result})


def filter_academic(request,dept_code):
    print('AJAX filter request received')
    formdata = dict(request.POST.copy())
    result = tables.department.get("dept_code = '{}'".format(dept_code))

    if not result['error']:
        try:
            #   To get the department details
            result = {'error': False, 'department': result['rows'][0]}
            formdata['department_id'] = [result['department']['dept_id']]
            #   To get the filtered list of academic staffs in that department
            column_names = 'staff_id,salutation,staff_fname,staff_mname,staff_lname,email,mobile_contact,designation'
            print('Filter Form Data: {}'.format(formdata))
            filter_columns = [field for field in formdata if field!='csrfmiddlewaretoken']
            filter_values = [formdata[field][0] for field in formdata if field!='csrfmiddlewaretoken']

            staff_list = tables.filter('academicsummary',filter_columns,filter_values)
            if staff_list['error']:
                raise Exception('No academic staffs were found with the specified criterias')
            result['staff_list'] = staff_list['rows']

        except IndexError as e:
            result = {'error': True, 'message': 'No such department is enlisted in the database'}

        except Exception as e:
            result = {'filtererror': True, 'department': result['department'],
                      'message': 'There was an error in querying the database: {}'.format(str(e))}

    return render(request, 'departmentapp/academictable.html', {'result': result})


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

            #   To get the post list for filtering
            post_list = tables.nonacademic_post.getall()
            if not post_list['error']:
                result['postlist'] = post_list['rows']

        except IndexError as e:
            result = {'error': True, 'message': 'No such department is enlisted in the database'}

        except Exception as e:
            result = {'error': True, 'department': result['department'],
                      'message': 'There was an error in querying the database: {}'.format(str(e))}

    return render(request, 'departmentapp/nonacademic.html', {'result': result})


def filter_nonacademic(request,dept_code):
    print('AJAX filter request received')
    formdata = dict(request.POST.copy())
    result = tables.department.get("dept_code = '{}'".format(dept_code))

    if not result['error']:
        try:
            #   To get the department details
            result = {'error': False, 'department': result['rows'][0]}
            formdata['department_id'] = [result['department']['dept_id']]
            #   To get the filtered list of academic staffs in that department
            print('Filter Form Data: {}'.format(formdata))
            filter_columns = [field for field in formdata if field!='csrfmiddlewaretoken']
            filter_values = [formdata[field][0] for field in formdata if field!='csrfmiddlewaretoken']

            staff_list = tables.filter('nonacademicsummary',filter_columns,filter_values)
            if staff_list['error']:
                raise Exception('No non-academic staffs were found with the specified criterias')
            result['staff_list'] = staff_list['rows']

        except IndexError as e:
            result = {'error': True, 'message': 'No such department is enlisted in the database'}

        except Exception as e:
            result = {'filtererror': True, 'department': result['department'],
                      'message': 'There was an error in querying the database: {}'.format(str(e))}

    return render(request, 'departmentapp/nonacademictable.html', {'result': result})


def course(request,dept_code):
    result = tables.department.get("dept_code = '{}'".format(dept_code))
    if not result['error']:
        # try catch block check if empty record is returned through indexing operation
        try:
            #   To get the department details
            result = {'error': False, 'department': result['rows'][0]}

            #   To get the entire list of courses offered by that department
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


def filter_course(request,dept_code):
    print('AJAX filter request received')
    formdata = dict(request.POST.copy())
    result = tables.department.get("dept_code = '{}'".format(dept_code))

    if not result['error']:
        try:
            #   To get the department details
            result = {'error': False, 'department': result['rows'][0]}
            formdata['department_id'] = [result['department']['dept_id']]
            #   To get the filtered list of courses in that department
            print('Filter Form Data: {}'.format(formdata))
            filter_columns = [field for field in formdata if field!='csrfmiddlewaretoken']
            filter_values = [formdata[field][0] for field in formdata if field!='csrfmiddlewaretoken']

            course_list = tables.filter('course',filter_columns,filter_values)
            if course_list['error']:
                raise Exception('No course was found with the specified course ID')
            result['course_list'] = course_list['rows']

        except IndexError as e:
            result = {'error': True, 'message': 'No such department is enlisted in the database'}

        except Exception as e:
            result = {'filtererror': True, 'department': result['department'],
                      'message': 'There was an error in querying the database: {}'.format(str(e))}

    return render(request, 'departmentapp/coursetable.html', {'result': result})


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
            # Resolve the uploaded file first
            try:
                staff_photo = request.FILES['photo_url']
                photo_filename = 'employee_{}{}'.format(formdata.get('staff_id')[0],os.path.splitext(str(staff_photo))[1])
                photo_fullurl = os.path.join(settings.MEDIA_ROOT, photo_filename)
                photo_url = photo_filename
                with open(photo_fullurl, 'wb+') as destination:
                    for chunk in staff_photo.chunks():
                        destination.write(chunk)
                print('Finished creating the image')
            except MultiValueDictKeyError:
                photo_url = None

            # Insert into employee table
            employeeInsert = tables.employee.insert(tables.nullresolver(formdata.get('staff_id')[0],True),
                                                    tables.nullresolver(formdata.get('staff_fname')[0]),
                                                    formdata.get('staff_mname')[0],
                                                    tables.nullresolver(formdata.get('staff_lname')[0]),
                                                    photo_url,
                                                    tables.nullresolver(formdata.get('email')[0]),
                                                    tables.nullresolver(formdata.get('home_contact')[0]),
                                                    tables.nullresolver(formdata.get('mobile_contact')[0]),
                                                    formdata.get('address')[0],
                                                    result['department']['dept_id'])


            if employeeInsert['error']:
                print('Error in inserting employee details ' + employeeInsert['message'])
                raise Exception('Error in inserting employee details '+employeeInsert['message'])
            # Insert into academic table
            academicInsert = tables.academic.insert(tables.nullresolver(formdata.get('staff_id')[0],True),formdata.get('salutation')[0],
                                                    formdata.get('designation')[0],formdata.get('service_type')[0],
                                                    formdata.get('contract_type')[0],formdata.get('qualification')[0],
                                                    tables.nullresolver(formdata.get('post_id')[0],True))
            if academicInsert['error']:
                print('Error in inserting academic details ' + academicInsert['message'])
                raise Exception('Error in inserting academic details ' + academicInsert['message'])
            # Insert into canteach table
            for eachcourse in formdata.get('course_code'):
                canteachInsert = tables.canteach.insert(tables.nullresolver(formdata.get('staff_id')[0],True),eachcourse)
                if canteachInsert['error']:
                    print('Error in inserting course details ' + canteachInsert['message'])
                    raise Exception('Error in inserting course details '+ canteachInsert['message'])
            submissionresult = {'error': False, 'message': 'DONE: Successfully registered the academic staff with staff ID: {}'.format(formdata.get('staff_id')[0])}

        except Exception as e:
             submissionresult = {'error': True, 'message': 'REGISTRATION ERROR: '+ str(e)}

        return render(request, 'departmentapp/addacademic.html', {'result': result, 'submissionresult': submissionresult})


def add_nonacademic(request,dept_code):
    #   This function needs to handle get request to cater new form and post request to manage form submissions
    result = tables.department.get("dept_code = '{}'".format(dept_code))
    if not result['error']:
        try:
            #   To get the department details
            result = {'error': False, 'department': result['rows'][0]}

            #   To get the available posts' list for form dropdown
            postlist = tables.nonacademic_post.getall()
            if postlist['error']:
                raise Exception('Post List retrieval error')
            result['postlist'] = postlist['rows']

        except IndexError as e:
            result = {'error': True, 'message': 'No such department is enlisted in the database'}

        except Exception as e:
            result = {'error': True, 'department': result['department'],
                      'message': 'There was an error in querying the database: {}'.format(str(e))}

    if request.method == 'GET':
        return render(request, 'departmentapp/addnonacademic.html', {'result': result})

    elif request.method == 'POST':
        print(request.POST)
        formdata = dict(request.POST.copy())
        # Here, we need to insert to 2 tables based on the submitted data: employee and nonacademic
        try:
            # Resolve the uploaded file first
            try:
                staff_photo = request.FILES['photo_url']
                photo_filename = 'employee_{}{}'.format(formdata.get('staff_id')[0],os.path.splitext(str(staff_photo))[1])
                photo_fullurl = os.path.join(settings.MEDIA_ROOT, photo_filename)
                photo_url = photo_filename
                with open(photo_fullurl, 'wb+') as destination:
                    for chunk in staff_photo.chunks():
                        destination.write(chunk)
                print('Finished creating the image')
            except MultiValueDictKeyError:
                photo_url = None

            # Insert into employee table
            employeeInsert = tables.employee.insert(tables.nullresolver(formdata.get('staff_id')[0], True),
                                                    tables.nullresolver(formdata.get('staff_fname')[0]),
                                                    formdata.get('staff_mname')[0],
                                                    tables.nullresolver(formdata.get('staff_lname')[0]),
                                                    photo_url,
                                                    tables.nullresolver(formdata.get('email')[0]),
                                                    tables.nullresolver(formdata.get('home_contact')[0]),
                                                    tables.nullresolver(formdata.get('mobile_contact')[0]),
                                                    formdata.get('address')[0],
                                                    result['department']['dept_id'])

            if employeeInsert['error']:
                print('Error in inserting employee details ' + employeeInsert['message'])
                raise Exception('Error in inserting employee details '+employeeInsert['message'])
            # Insert into nonacademic table
            nonacademicInsert = tables.nonacademic.insert(tables.nullresolver(formdata.get('staff_id')[0],True),
                                                          tables.nullresolver(formdata.get('post_id')[0],True))
            if nonacademicInsert['error']:
                print('Error in inserting academic details ' + nonacademicInsert['message'])
                raise Exception('Error in inserting non-academic details ' + nonacademicInsert['message'])

            submissionresult = {'error': False, 'message': 'DONE: Successfully registered the non-academic staff with staff ID: {}'.format(formdata.get('staff_id')[0])}

        except Exception as e:
             submissionresult = {'error': True, 'message': 'REGISTRATION ERROR: '+ str(e)}

        return render(request, 'departmentapp/addnonacademic.html', {'result': result, 'submissionresult': submissionresult})


def add_course(request,dept_code):
    #   This function needs to handle get request to cater new form and post request to manage form submissions
    result = tables.department.get("dept_code = '{}'".format(dept_code))
    if not result['error']:
        try:
            #   To get the department details
            result = {'error': False, 'department': result['rows'][0]}

        except IndexError as e:
            result = {'error': True, 'message': 'No such department is enlisted in the database'}

        except Exception as e:
            result = {'error': True, 'department': result['department'],
                      'message': 'There was an error in querying the database: {}'.format(str(e))}

    if request.method == 'GET':
        return render(request, 'departmentapp/addcourse.html', {'result': result})

    elif request.method == 'POST':
        print(request.POST)
        formdata = dict(request.POST.copy())
        # Here, we need to insert to 1 table based on the submitted data: course
        try:
            # Insert into course table
            courseInsert = tables.course.insert(formdata.get('course_code')[0],
                                                formdata.get('course_name')[0],
                                                result['department']['dept_id'])
            if courseInsert['error']:
                print('Error in inserting course details ' + courseInsert['message'])
                raise Exception('Error in inserting employee details '+courseInsert['message'])

            submissionresult = {'error': False, 'message': 'DONE: Successfully registered the course with course code: {}'.format(formdata.get('course_code')[0])}

        except Exception as e:
             submissionresult = {'error': True, 'message': 'REGISTRATION ERROR: '+ str(e)}

        return render(request, 'departmentapp/addcourse.html', {'result': result, 'submissionresult': submissionresult})


def test(request):
    # employeeInsert = tables.employee.insert(tables.nullresolver(formdata.get('staff_id')[0], True),
    #                                         tables.nullresolver(formdata.get('staff_fname')[0]),
    #                                         formdata.get('staff_mname')[0],
    #                                         tables.nullresolver(formdata.get('staff_lname')[0]),
    #                                         photo_url,
    #                                         tables.nullresolver(formdata.get('email')[0]),
    #                                         tables.nullresolver(formdata.get('home_contact')[0]),
    #                                         tables.nullresolver(formdata.get('mobile_contact')[0]),
    #                                         formdata.get('address')[0],
    #                                         result['department']['dept_id'])
    getter = tables.get('employee','photo_url','staff_id = 1162');
    print(getter['rows'])

    return render(request,'departmentapp/test.html')


def academic_profile(request,dept_code,staff_id):
    result = tables.department.get("dept_code = '{}'".format(dept_code))
    if not result['error']:
        # try catch block check if empty record is returned through indexing operation
        try:
            #   To get the department details
            result = {'error': False, 'department': result['rows'][0]}

            #   To get the staff details, we use the view in the db, academicprofile
            staff_details = tables.get('academicprofile','*','staff_id = {}'.format(staff_id))
            if staff_details['error']:
                raise Exception('Couldnt fetch the staff profile for staff_id:{}'.format(staff_id))
            result['staff'] = staff_details['rows'][0]

            #   To get the canteach course details
            canteach = tables.get(tables.join('canteach','course'),'*','staff_id = {}'.format(staff_id))
            if not canteach['error']:
                result['canteach'] = canteach['rows']

            #   To get the instructs course details
            instructs = tables.get(tables.join('instructs', 'course'), '*', 'staff_id = {}'.format(staff_id))
            if not instructs['error']:
                result['instructs'] = instructs['rows']

        except IndexError as e:
            result = {'error': True, 'message': 'Invalid department or staff info'}

        except Exception as e:
            result = {'error': True, 'department': result['department'],
                      'message': 'There was an error in querying the database: {}'.format(str(e))}

    return render(request, 'departmentapp/academicprofile.html', {'result': result})


def nonacademic_profile(request, dept_code, staff_id):
    result = tables.department.get("dept_code = '{}'".format(dept_code))
    if not result['error']:
        # try catch block check if empty record is returned through indexing operation
        try:
            #   To get the department details
            result = {'error': False, 'department': result['rows'][0]}

            #   To get the staff details, we use the view in the db, nonacademicprofile
            staff_details = tables.get('nonacademicprofile', '*', 'staff_id = {}'.format(staff_id))
            if staff_details['error']:
                raise Exception('Couldnt fetch the staff profile for staff_id:{}'.format(staff_id))
            result['staff'] = staff_details['rows'][0]

        except IndexError as e:
            result = {'error': True, 'message': 'Invalid department or staff info'}

        except Exception as e:
            result = {'error': True, 'department': result['department'],
                      'message': 'There was an error in querying the database: {}'.format(str(e))}

    return render(request, 'departmentapp/nonacademicprofile.html', {'result': result})


def course_profile(request, dept_code, course_code):
    result = tables.department.get("dept_code = '{}'".format(dept_code))
    if not result['error']:
        # try catch block check if empty record is returned through indexing operation
        try:
            #   To get the department details
            result = {'error': False, 'department': result['rows'][0]}

            #   To get the course details
            course_info = tables.course.get("course_code = '{}'".format(course_code))
            if course_info['error']:
                raise Exception('Course Details Retrieval Error')
            result['course'] = course_info['rows'][0]

            #   To get the list of academic staffs teaching this course
            current_stafflist = tables.get(tables.join('instructs','employee'),'*',"course_code = '{}'".format(course_code))
            if not current_stafflist['error']:
                result['current_stafflist'] = current_stafflist['rows']

            #   To get the list of academic staffs capable of teaching this course
            capable_stafflist = tables.get(tables.join('canteach', 'employee'), '*',
                                           "course_code = '{}'".format(course_code))
            if not capable_stafflist['error']:
                result['capable_stafflist'] = capable_stafflist['rows']

        except IndexError as e:
            result = {'error': True, 'message': 'No such department is enlisted in the database'}

        except Exception as e:
            result = {'error': True, 'department': result['department'],
                      'message': 'There was an error in querying the database: {}'.format(str(e))}

    return render(request, 'departmentapp/courseprofile.html', {'result': result})


def add_instruct(request,dept_code,course_code):
    result = tables.department.get("dept_code = '{}'".format(dept_code))
    result = {'error': False, 'department': result['rows'][0]}
    course_info = tables.course.get("course_code = '{}'".format(course_code))
    result['course'] = course_info['rows'][0]
    capable_stafflist = tables.get(tables.join('canteach', 'employee'), '*',
                                   "course_code = '{}'".format(course_code))
    result['capable_stafflist'] = capable_stafflist['rows']

    formdata = dict(request.POST.copy())

    try:
        insertResult = tables.instructs.insert(tables.nullresolver(formdata.get('staff_id')[0],True),course_code,
                                formdata.get('semester')[0],formdata.get('program')[0])
        if insertResult['error']:
            raise Exception('Invalid from fillup, Please refill the form. Details: '+insertResult['message'])
        result['submission'] = {'error': False,
                                'message': 'Successfully assigned staff: ID-{}, as the instructor for course:{} in {} for semester {}'.format(
                                formdata.get('staff_id')[0],
                                course_code,
                                formdata.get('program')[0],
                                formdata.get('semester')[0] )}
    except Exception as e:
        result['submission'] = {'error': True, 'message': str(e)}
    return render(request, 'departmentapp/addinstructform.html', {'result': result})

def delete_employee(request,dept_code,staff_id):
    deleteResult = tables.delete('employee','staff_id = {}'.format(staff_id))
    return render(request, 'departmentapp/deletioninfo.html', {'result': deleteResult})


def delete_course(request,dept_code,course_code):
    deleteResult = tables.delete('course',"course_code = '{}'".format(course_code))
    return render(request, 'departmentapp/deletioninfo.html', {'result': deleteResult})


def remove_instructor(request,dept_code,course_code):
    staff_id = request.META['HTTP_STAFFID']
    staff_semester = request.META['HTTP_STAFFSEMESTER']
    staff_program = request.META['HTTP_STAFFPROGRAM']
    print('To be deleted from instructs: {},{}'.format(staff_id,course_code))
    deleteResult = tables.delete('instructs',"staff_id = {} AND course_code = '{}' AND semester = {} AND program = '{}' ".format(
        staff_id,course_code,staff_semester,staff_program))
    return render(request, 'departmentapp/deletioninfo.html', {'result': deleteResult})


def edit_academic(request,dept_code,staff_id):
    #   This function needs to handle get request to cater new form and post request to manage form submissions
    result = tables.department.get("dept_code = '{}'".format(dept_code))
    if not result['error']:
        try:
            #   To get the department details
            result = {'error': False, 'department': result['rows'][0]}

            #   To get the initial staff details before update
            initial_staffdetails = tables.get('academicsummary', '*', 'staff_id = {}'.format(staff_id))
            if initial_staffdetails['error']:
                raise Exception('Couldnt fetch the staff profile for staff_id:{}'.format(staff_id))
            result['initial_staffdetails'] = initial_staffdetails['rows'][0]

            #   To get the initial canteach course details before update
            initial_canteach = tables.get(tables.join('canteach', 'course'), '*', 'staff_id = {}'.format(staff_id))
            if not initial_canteach['error']:
                result['initial_canteach'] = [ each['course_code'] for each in initial_canteach['rows']]

            #   Data retrieval for the form options ------------------
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
        return render(request, 'departmentapp/editacademic.html', {'result': result})

    elif request.method == 'POST':
        formdata = dict(request.POST.copy())
        # Here, we need to insert to 3 tables based on the submitted data: employee, academic and canteach
        try:
            # Resolve the uploaded file first
            try:
                staff_photo = request.FILES['photo_url']
                photo_filename = 'employee_{}{}'.format(formdata.get('staff_id')[0],
                                                        os.path.splitext(str(staff_photo))[1])
                photo_fullurl = os.path.join(settings.MEDIA_ROOT, photo_filename)
                photo_url = photo_filename
                with open(photo_fullurl, 'wb+') as destination:
                    for chunk in staff_photo.chunks():
                        destination.write(chunk)
                print('Finished creating the image')
            except MultiValueDictKeyError:
                photo_url = None

            new_staff_id = tables.nullresolver(formdata.get('staff_id')[0],True)

            if photo_url is None and result['initial_staffdetails']['photo_url'] is not None:
                photo_url = result['initial_staffdetails']['photo_url']

            # Update the employee table
            employeeUpdate = tables.employee.update(new_staff_id,
                                                    tables.nullresolver(formdata.get('staff_fname')[0]),
                                                    formdata.get('staff_mname')[0],
                                                    tables.nullresolver(formdata.get('staff_lname')[0]),
                                                    photo_url,
                                                    tables.nullresolver(formdata.get('email')[0]),
                                                    tables.nullresolver(formdata.get('home_contact')[0]),
                                                    tables.nullresolver(formdata.get('mobile_contact')[0]),
                                                    formdata.get('address')[0],
                                                    result['department']['dept_id'],
                                                    'staff_id = {}'.format(staff_id))
            if employeeUpdate['error']:
                print('Error in updating employee details ' + employeeUpdate['message'])
                raise Exception('Error in updating employee details ' + employeeUpdate['message'])
            #   Re-assignment is done so as to change according to successful update on employee
            initial_staffdetails = tables.get('academicsummary', '*', 'staff_id = {}'.format(new_staff_id))
            result['initial_staffdetails'] = initial_staffdetails['rows'][0]

            # Update the academic table
            academicUpdate = tables.academic.update(new_staff_id,
                                                    formdata.get('salutation')[0],
                                                    formdata.get('designation')[0], formdata.get('service_type')[0],
                                                    formdata.get('contract_type')[0], formdata.get('qualification')[0],
                                                    tables.nullresolver(formdata.get('post_id')[0], True),
                                                    'staff_id = {}'.format(new_staff_id))
            if academicUpdate['error']:
                print('Error in updating academic details ' + academicUpdate['message'])
                raise Exception('Error in inserting academic details ' + academicUpdate['message'])

            initial_staffdetails = tables.get('academicsummary', '*', 'staff_id = {}'.format(new_staff_id))
            result['initial_staffdetails'] = initial_staffdetails['rows'][0]

            # Update the canteach table
            #----first delete the initial records in canteach table
            removeinitial = tables.delete('canteach','staff_id = {}'.format(new_staff_id))

            #----then, add the new entries from form
            for eachcourse in formdata.get('course_code'):
                canteachInsert = tables.canteach.insert(new_staff_id,eachcourse)
                if canteachInsert['error']:
                    print('Error in inserting course details ' + canteachInsert['message'])
                    raise Exception('Error in inserting course details ' + canteachInsert['message'])

            return redirect('departmentapp:academic_profile',dept_code=dept_code,staff_id=new_staff_id)

        except Exception as e:
            updateError = {'error': True, 'message': 'UPDATE ERROR: ' + str(e)}

            return render(request, 'departmentapp/editacademic.html',
                      {'result': result, 'updateError': updateError})


def edit_nonacademic(request,dept_code,staff_id):
    #   This function needs to handle get request to cater new form and post request to manage form submissions
    result = tables.department.get("dept_code = '{}'".format(dept_code))
    if not result['error']:
        try:
            #   To get the department details
            result = {'error': False, 'department': result['rows'][0]}

            #   To get the initial staff details before update
            initial_staffdetails = tables.get('nonacademicsummary', '*', 'staff_id = {}'.format(staff_id))
            if initial_staffdetails['error']:
                raise Exception('Couldnt fetch the staff profile for staff_id:{}'.format(staff_id))
            result['initial_staffdetails'] = initial_staffdetails['rows'][0]

            #   Data retrieval for the form options ------------------
            #   To get the available posts' list for form dropdown
            postlist = tables.nonacademic_post.getall()
            if postlist['error']:
                raise Exception('Post List retrieval error')
            result['postlist'] = postlist['rows']


        except IndexError as e:
            result = {'error': True, 'message': 'No such department is enlisted in the database'}

        except Exception as e:
            result = {'error': True, 'department': result['department'],
                      'message': 'There was an error in querying the database: {}'.format(str(e))}

    if request.method == 'GET':
        return render(request, 'departmentapp/editnonacademic.html', {'result': result})

    elif request.method == 'POST':
        formdata = dict(request.POST.copy())
        # Here, we need to update 2 tables based on the submitted data: employee, nonacademic
        try:
            # Resolve the uploaded file first
            try:
                staff_photo = request.FILES['photo_url']
                photo_filename = 'employee_{}{}'.format(formdata.get('staff_id')[0],
                                                        os.path.splitext(str(staff_photo))[1])
                photo_fullurl = os.path.join(settings.MEDIA_ROOT, photo_filename)
                photo_url = photo_filename
                with open(photo_fullurl, 'wb+') as destination:
                    for chunk in staff_photo.chunks():
                        destination.write(chunk)
                print('Finished creating the image')
            except MultiValueDictKeyError:
                photo_url = None

            new_staff_id = tables.nullresolver(formdata.get('staff_id')[0], True)

            if photo_url is None and result['initial_staffdetails']['photo_url'] is not None:
                photo_url = result['initial_staffdetails']['photo_url']

            # Update the employee table
            employeeUpdate = tables.employee.update(new_staff_id,
                                                    tables.nullresolver(formdata.get('staff_fname')[0]),
                                                    formdata.get('staff_mname')[0],
                                                    tables.nullresolver(formdata.get('staff_lname')[0]),
                                                    photo_url,
                                                    tables.nullresolver(formdata.get('email')[0]),
                                                    tables.nullresolver(formdata.get('home_contact')[0]),
                                                    tables.nullresolver(formdata.get('mobile_contact')[0]),
                                                    formdata.get('address')[0],
                                                    result['department']['dept_id'],
                                                    'staff_id = {}'.format(staff_id))
            if employeeUpdate['error']:
                print('Error in updating employee details ' + employeeUpdate['message'])
                raise Exception('Error in updating employee details ' + employeeUpdate['message'])
            #   Re-assignment is done so as to change according to successful update on employee
            initial_staffdetails = tables.get('nonacademicsummary', '*', 'staff_id = {}'.format(new_staff_id))
            result['initial_staffdetails'] = initial_staffdetails['rows'][0]

            # Update the nonacademic table
            nonacademicUpdate = tables.nonacademic.update(new_staff_id,
                                                    tables.nullresolver(formdata.get('post_id')[0], True),
                                                    'staff_id = {}'.format(new_staff_id))
            if nonacademicUpdate['error']:
                print('Error in updating non-academic staff details ' + nonacademicUpdate['message'])
                raise Exception('Error in inserting non-academic staff details ' + nonacademicUpdate['message'])

            initial_staffdetails = tables.get('nonacademicsummary', '*', 'staff_id = {}'.format(new_staff_id))
            result['initial_staffdetails'] = initial_staffdetails['rows'][0]

            return redirect('departmentapp:nonacademic_profile', dept_code=dept_code, staff_id=new_staff_id)

        except Exception as e:
            updateError = {'error': True, 'message': 'UPDATE ERROR: ' + str(e)}

            return render(request, 'departmentapp/editnonacademic.html',
                          {'result': result, 'updateError': updateError})