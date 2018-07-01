from django.shortcuts import render
from django.db import connection,transaction

# Create your views here.

def home(request):
    with connection.cursor() as cursor:
        query1 = '''SELECT * FROM course;'''

        try:
            cursor.execute(query1)
            results = cursor.fetchall()
            rows = []
            columns = [each[0] for each in cursor.description]
            print(columns)
            for result in results:
                row = dict(zip(columns,result))
                rows.append(row)
            print(rows)
            return render(request,'departmentapp/home.html',{'results':rows})

        except Exception as e:
            print('Couldnt fetch data due to error ... '+ str(e))

    # query2 = '''SELECT * FROM academic WHERE staff_id='%s' '''%('9999')
        #
        # cursor.execute(query2)
        # results = cursor.fetchall()
        # print(results)
        # for result in results:
        #     print(result==None)