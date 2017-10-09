Currently using Python is in backend  for Rest Api:

Python:

django-admin.py startproject djangular //start the project

python manage.py runserver // to run the server

to resolve applicaton error run:

python manage.py startapp scrumboard // for startng your own app

python manage.py makemigration // after creation of models

Then migrate your code changes to django project so that it will have all the changes related to it.

python manage.py migrate

To see yout table open sqllite using below command:

In windows: db.sqlite3 if you dont have sqlite installed in your system then follow below: 

For opening sqlite follow below step->

python doesnt have install default sqllite in your system
1. Download from : https://sqlitestudio.pl/index.rvt
   Basic tutorial : http://www.sqlitetutorial.net/download-install-sqlite/
 
https://goo.gl/ef55le

To login into the UI :
Register all the models in admin.py then
we need to create super user:
python manage.py createsuperuser
username: alokv
pass: alok1234

For rest full services install DRF (django restfull services)
pip install djangorestframework

after that create serializable class
then create API class which handle the request from the client

https://docs.djangoproject.com/en/1.8/topics/forms/modelforms/#selecting-the-fields-to-use
