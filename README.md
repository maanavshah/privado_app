# privado-app (django-mongodb)

Installation
------------

Execute the following commands to install spectre

To install django, djonogo (mongodb package) and create a virtual environment:

    $ pip install virtualenv
    $ python -m virtualenv venv
    $ source venv/bin/activate

Now, clone the repository and change the working directory to app. To install django:

    $ pip install django
    $ pip install djongo

You can check if django is correctly installed or not using:

    $ django-admin --version

Now, you need to run migrations to create the database schema for app:

    $ python manage.py migrate

You can now start the django server:

    $ python manage.py runserver

Or you can add it in your own application (optional: I have already added this.)

1. Add ``privado_app`` to your INSTALLED_APPS setting like this::

       INSTALLED_APPS = (
           ...
           'privado_app',
       )

2. Run ``python manage.py migrate``
3. Include the ``privado_app urls`` like this to have your "home page" as the blog index::

        urlpatterns = [
          ...
          url(r'^admin/', include(admin.site.urls)),
          path('te/customer/<str:customer_id>/templates', views.vw_templates),
        ]

Usage
-----

You can visit the django website at http://localhost:8000.

Testing
-------

You can create/retrieve a template in python:

    import requests
    import json

    # create template using customerId
    url = 'http://localhost:8000/te/customer/456/templates'
    x = requests.post(url)
    print(f'status_code: {x.status_code}')
    print(f'content: {json.loads(x.content)}')

    # get template using customerId
    url = 'http://localhost:8000/te/customer/456/templates'
    x = requests.get(url)
    print(f'status_code: {x.status_code}')
    print(f'content: {json.loads(x.content)}')
