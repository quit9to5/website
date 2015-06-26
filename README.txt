1. We need to install pip installer. Do like this 

root@kripanand-VirtualBox:~$ apt-get install python-pip 

2. Now install django using pip
root@kripanand-VirtualBox:~$ pip install  Django==1.8.2

3. After installing django check django version like this
--->
root@kripanand-VirtualBox:~$ python
Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> django.VERSION
(1, 8, 2, 'final', 0)
>>> 

4. Create the First hello world project like this 

root@kripanand-VirtualBox:~$ django-admin.py startproject hello

5.First migrate the your project so that it support latest django support

root@kripanand-VirtualBox:~$ python manage.py migrate
Operations to perform:
  Synchronize unmigrated apps: staticfiles, messages
  Apply all migrations: admin, contenttypes, auth, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying sessions.0001_initial... OK


6. Now start your hello world server

root@kripanand-VirtualBox:~$ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
June 06, 2015 - 14:54:21
Django version 1.8.2, using settings 'hello.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

[06/Jun/2015 14:54:36]"GET / HTTP/1.1" 200 1767
[06/Jun/2015 14:54:36]"GET /favicon.ico HTTP/1.1" 404 1935
[06/Jun/2015 14:54:36]"GET /favicon.ico HTTP/1.1" 404 1935

7. Now open Web-page  
http://127.0.0.1:8000/

