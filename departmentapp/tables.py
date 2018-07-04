from django.db import connection,transaction

def insert(table_name,field_names,param_tuple):
    # Creation of INSERT query
    with connection.cursor() as cursor:
        query = '''INSERT INTO {}{} VALUES {};'''.format(table_name,str(field_names),str(param_tuple))
        print(query)
        try:
            cursor.execute(query)
            transaction.commit()
            return ('Successfully inserted {} into the table {}'.format(str(param_tuple),table_name))
        except Exception as e:
            transaction.rollback()
            return ("Error: Couldn't perform the insert operation in {}. {}".format(table_name,str(e)))

def update():
    pass

def delete():
    pass

def get(table_name,column_names,condition):
    query = '''SELECT {} FROM {} WHERE {};'''.format(column_names,table_name,condition)
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


class department:

    def getall():
        return get('department','*',condition=1)



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


class academic_post:
    pass


class nonacademic_post:
    pass


class course:
    field_names = ['course_code','course_name','department_id']

    def insert(course_code,course_name,department_id):
        input_fields = []
        arguments = [course_code,course_name,department_id]
        argdict = dict(zip(course.field_names, arguments))
        input_values = []
        for field in argdict:
            if argdict[field] is not None:
                input_fields.append(field)
                input_values.append(argdict[field])

        return insert('course', '(' + ','.join(input_fields) + ')', tuple(input_values))


class instructs:
    field_names = ['staff_id','course_code','semester']

    def insert(staff_id,course_code,semester):
        input_fields = []
        arguments = [staff_id,course_code,semester]
        argdict = dict(zip(instructs.field_names, arguments))
        input_values = []
        for field in argdict:
            if argdict[field] is not None:
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
            if argdict[field] is not None:
                input_fields.append(field)
                input_values.append(argdict[field])

        return insert('canteach', '(' + ','.join(input_fields) + ')', tuple(input_values))

