from django.db import connection,transaction

def insert(table_name,field_names,param_tuple):
    # Creation of INSERT query
    #   special case of only one value in param_tuple
    if len(param_tuple) == 1:
        param_tuple = '('+str(param_tuple[0])+')'

    with connection.cursor() as cursor:
        query = '''INSERT INTO {}{} VALUES {};'''.format(table_name,str(field_names),str(param_tuple))
        print(query)
        try:
            cursor.execute(query)
            transaction.commit()
            return {'error': False, 'message':'Successfully inserted {} into the table {}'.format(str(param_tuple),table_name)}
        except Exception as e:
            transaction.rollback()
            return {'error': True, 'message':"Error: Couldn't perform the insert operation in {}. {}".format(table_name,str(e))}

def update(table_name,update_statement,condition):
    # Creation of UPDATE query

    with connection.cursor() as cursor:
        query = '''UPDATE {} SET {} WHERE {};'''.format(table_name,update_statement,condition)
        print(query)
        try:
            cursor.execute(query)
            transaction.commit()
            return {'error': False,
                    'message': 'Successfully updated the table {} by statements: {}'.format( table_name,update_statement)}
        except Exception as e:
            transaction.rollback()
            return {'error': True,
                    'message': "Error: Couldn't perform the update operation in {}. Details:- {}".format(table_name, str(e))}


def delete(table_name,condition):
    # Creation of DELETE query
    with connection.cursor() as cursor:
        query = '''DELETE FROM {} WHERE {}'''.format(table_name,condition)
        print(query)
        try:
            cursor.execute(query)
            transaction.commit()
            return {'error': False, 'message': 'Successfully deleted matching record(s) from the table {}'.format(table_name)}
        except Exception as e:
            transaction.rollback()
            return {'error': True, 'message': "Couldn't perform the deletion operation in {}. Details:- {}".format(table_name,str(e))}

def get(table_name,column_names,condition):
    query = '''SELECT {} FROM {} WHERE {};'''.format(column_names,table_name,condition)
    print(query)
    with connection.cursor() as cursor:
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            rows = []
            columns = [each[0] for each in cursor.description]
            print(columns)
            for result in results:
                row = dict(zip(columns,result))
                rows.append(row)
            print(rows)
            return {'error': False, 'rows': rows}
        except Exception as e:
            return {'error': True, 'message': str(e)}

def count(table_name,column_name,condition):
    query = '''SELECT count({}) FROM {} WHERE {};'''.format(column_name,table_name,condition)
    print(query)
    with connection.cursor() as cursor:
        try:
            cursor.execute(query)
            result = cursor.fetchone()[0]   #By default, it returns a tuple like (count,) so indexing...
            print(result)
            return {'error': False, 'value': result}
        except Exception as e:
            return {'error': True, 'message': str(e)}

def join(table1,table2,type='natural',on=None):
    joinstr = '{} {} join {} '.format(table1,type,table2)
    if on is not None:
        joinstr += 'on {}'.format(on)
    return joinstr

def nullresolver(input_value,isinteger=False):
    if input_value == '':
        return None
    if isinteger:
        return int(input_value)
    else:
        return input_value

class department:

    def getall(column_names=None):
        if column_names is None:
            column_names = '*'
        return get('department',column_names,condition=1)

    def get(condition,column_names=None):
        if column_names is None:
            column_names = '*'
        return get('department',column_names,condition)



class employee:
    field_names = ['staff_id','staff_fname','staff_mname','staff_lname','photo_url','email','home_contact','mobile_contact','address','department_id']

    def insert(staff_id,staff_fname,staff_mname,staff_lname,photo_url,email,home_contact,mobile_contact,address,department_id):
        input_fields = []
        arguments = [staff_id,staff_fname,staff_mname,staff_lname,photo_url,email,home_contact,mobile_contact,address,department_id]
        argdict = dict(zip(employee.field_names,arguments))
        input_values = []
        for field in argdict:
            if argdict[field] is not None:
                input_fields.append(field)
                input_values.append(argdict[field])

        return insert('employee','('+','.join(input_fields)+')',tuple(input_values))

    def update(staff_id,staff_fname,staff_mname,staff_lname,photo_url,email,home_contact,mobile_contact,address,department_id,condition):
        update_expressions = []
        arguments = [staff_id,staff_fname,staff_mname,staff_lname,photo_url,email,home_contact,mobile_contact,address,department_id]
        argdict = dict(zip(employee.field_names,arguments))
        for field in argdict:
            if argdict[field] is not None:
                if isinstance(argdict[field],int):
                    update_expressions.append('{} = {}'.format(field,argdict[field]))
                elif isinstance(argdict[field],str):
                    update_expressions.append("{} = '{}'".format(field,argdict[field]))
            else:
                update_expressions.append('{} = NULL'.format(field))

        return update('employee',','.join(update_expressions),condition)



class academic:
    field_names = ['staff_id','salutation','designation','service_type','contract_type','qualification','post_id']

    def insert(staff_id,salutation,designation,service_type,contract_type,qualification,post_id):
        input_fields = []
        arguments = [staff_id,salutation,designation,service_type,contract_type,qualification,post_id]
        argdict = dict(zip(academic.field_names, arguments))
        input_values = []
        for field in argdict:
            if argdict[field] is not None:
                input_fields.append(field)
                input_values.append(argdict[field])

        return insert('academic', '(' + ','.join(input_fields) + ')', tuple(input_values))

    def update(staff_id,salutation,designation,service_type,contract_type,qualification,post_id,condition):
        update_expressions = []
        arguments = [staff_id,salutation,designation,service_type,contract_type,qualification,post_id]
        argdict = dict(zip(academic.field_names, arguments))
        for field in argdict:
            if argdict[field] is not None:
                if isinstance(argdict[field],int):
                    update_expressions.append('{} = {}'.format(field,argdict[field]))
                elif isinstance(argdict[field],str):
                    update_expressions.append("{} = '{}'".format(field,argdict[field]))
            else:
                update_expressions.append('{} = NULL'.format(field))

        return update('academic',','.join(update_expressions),condition)



class nonacademic:
    field_names = ['staff_id','post_id']

    def insert(staff_id,post_id):
        input_fields = []
        arguments = [staff_id,post_id]
        argdict = dict(zip(nonacademic.field_names, arguments))
        input_values = []
        for field in argdict:
            if argdict[field] is not None:
                input_fields.append(field)
                input_values.append(argdict[field])

        return insert('nonacademic', '(' + ','.join(input_fields) + ')', tuple(input_values))

    def update(staff_id,post_id,condition):
        update_expressions = []
        arguments = [staff_id,post_id]
        argdict = dict(zip(nonacademic.field_names, arguments))
        for field in argdict:
            if argdict[field] is not None:
                if isinstance(argdict[field],int):
                    update_expressions.append('{} = {}'.format(field,argdict[field]))
                elif isinstance(argdict[field],str):
                    update_expressions.append("{} = '{}'".format(field,argdict[field]))
            else:
                update_expressions.append('{} = NULL'.format(field))

        return update('nonacademic',','.join(update_expressions),condition)



class academic_post:
    def getall(column_names=None):
        if column_names is None:
            column_names = '*'
        return get('academic_post',column_names,condition=1)

    def get(condition,column_names=None):
        if column_names is None:
            column_names = '*'
        return get('academic_post',column_names,condition)

    def count(condition=1):
        return count('academic_post','*',condition)



class nonacademic_post:
    def getall(column_names=None):
        if column_names is None:
            column_names = '*'
        return get('nonacademic_post',column_names,condition=1)

    def get(condition,column_names=None):
        if column_names is None:
            column_names = '*'
        return get('nonacademic_post',column_names,condition)

    def count(condition=1):
        return count('nonacademic_post','*',condition)



class course:
    field_names = ['course_code','course_name','department_id']

    def insert(course_code,course_name,department_id):
        input_fields = []
        arguments = [course_code,course_name,department_id]
        argdict = dict(zip(course.field_names, arguments))
        input_values = []
        for field in argdict:
            if argdict[field] is not None and argdict[field] != '':
                input_fields.append(field)
                input_values.append(argdict[field])

        return insert('course', '(' + ','.join(input_fields) + ')', tuple(input_values))

    def getall(column_names=None):
        if column_names is None:
            column_names = '*'
        return get('course',column_names,condition=1)

    def get(condition,column_names=None):
        if column_names is None:
            column_names = '*'
        return get('course',column_names,condition)

    def count(condition=1):
        return count('course','*',condition)


class instructs:
    field_names = ['staff_id','course_code','semester']

    def insert(staff_id,course_code,semester):
        input_fields = []
        arguments = [staff_id,course_code,semester]
        argdict = dict(zip(instructs.field_names, arguments))
        input_values = []
        for field in argdict:
            if argdict[field] is not None and argdict[field] != '':
                input_fields.append(field)
                input_values.append(argdict[field])

        return insert('instructs', '(' + ','.join(input_fields) + ')', tuple(input_values))


class canteach:
    field_names = ['staff_id','course_code']

    def insert(staff_id,course_code):
        input_fields = []
        arguments = [staff_id, course_code]
        argdict = dict(zip(canteach.field_names, arguments))
        input_values = []
        for field in argdict:
            if argdict[field] is not None and argdict[field] != '':
                input_fields.append(field)
                input_values.append(argdict[field])

        return insert('canteach', '(' + ','.join(input_fields) + ')', tuple(input_values))

