# DepartmentDatabase
DBMS project to create an app to facilitate the faculty coordination in Pulchowk Campus

MySQL connection with Django:

1. Edit the database backend setting in settings.py file
2. import connection, transaction (for data modification operations) from django.db
3. connection.cursor returns a cursor object that is used to execute(), fetchone(), fetchall() results of the query execution
4. We avoid the django model layer completely and make our own classes for each table and custom methods for insert, update, list or filter operations
