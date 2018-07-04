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
            if(hod_details['error']):
                raise Exception('HOD Details cannot be retrieved')
            result['hod'] = hod_details['rows'][0]  # Since, only one HOD in each dept, index 0 will only be filled in result

            #   To get the Deputy HOD details in a dictionary field 'dhod'
            dhod_details = tables.get(tables.join('employee', 'academic'),
                                     'salutation,staff_fname,staff_lname,email,mobile_contact,photo_url',
                                     condition='department_id = {} and post_id = {}'.format(
                                         result['department']['dept_id'], 2))
            if (dhod_details['error']):
                raise Exception('Deputy HOD Details cannot be retrieved')
            result['dhod'] = dhod_details['rows']  # Since, more than one HOD is possible in a dept, no indexing


        except IndexError as e:
            result = {'error': True, 'message': 'No such department is enlisted in the database'}

        except Exception as e:
            result = {'error': True, 'message': 'There was an error in querying the database: {}'.format(str(e))}

    return render(request,'departmentapp/dashboard.html',{'result':result})

def test(request):
    test = tables.employee.insert(9999,'David','','Seaman',None,None,7787,8878,None,1)
    print(test)
    return render(request,'departmentapp/test.html')

    # with connection.cursor() as cursor:
    #     query1 = '''SELECT * FROM course;'''
    #
    #     try:
    #         cursor.execute(query1)
    #         results = cursor.fetchall()
    #         rows = []
    #         columns = [each[0] for each in cursor.description]
    #         print(columns)
    #         for result in results:
    #             row = dict(zip(columns,result))
    #             rows.append(row)
    #         print(rows)
    #         return render(request,'departmentapp/test.html',{'results':rows})
    #
    #     except Exception as e:
    #         print('Couldnt fetch data due to error ... '+ str(e))

    # query2 = '''SELECT * FROM academic WHERE staff_id='%s' '''%('9999')
        #
        # cursor.execute(query2)
        # results = cursor.fetchall()
        # print(results)
        # for result in results:
        #     print(result==None)
