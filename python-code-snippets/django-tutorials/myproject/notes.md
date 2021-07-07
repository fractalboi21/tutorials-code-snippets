# Django workflow
```bat
mkdir django-projects
cd django-projects/
django-admin startproject myproject
cd myproject/
python3 manage.py runserver
```
make sure that your in project folder
```bash
django-admin startapp myapp
```

Include your app to your project in settings.py as follow
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #include your apps
    'myapp'
]
```

[how to create models and register them to admin](http://www.john-player.com/django/how-to-register-a-model-with-django-admin/)

when ever you make changes to your model use these following commands
```
python3 manage.py makemigrations
python3 manage.py migrate
```
create superuser
```
python3 manage.py createsuperuser
```
And go check http://127.0.0.1:8000/admin/ and enter your password


create app
```
python3 manage.py startapp <app>
```

#Views code snippets
```python3
#/<app>/views.py
# function based viewa using HttpResponse
def geeks_view(request):
    count = Person.objects.count()
    html = f"Total number of entries: {count}"
    return HttpResponse(html)

#fuction
def name_list(request):
    return render(request,"index.html",context = {"info":"world"})
```

filter query in django
```python
Blog.objects.filter(tags__contains="python")
``