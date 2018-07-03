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

def get():
    pass


class department:
    pass


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
    pass


class nonacademic:
    pass


class academic_post:
    pass


class nonacademic_post:
    pass


class course:
    pass


class instructs:
    pass


class canteach:
    pass
