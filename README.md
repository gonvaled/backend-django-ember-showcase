# Integrating Django and Ember #

Django allows you to write powerful and simple REST APIs with the help of [Django REST framework](http://www.django-rest-framework.org). [Ember.js](http://emberjs.com) is a JavaScript framework to help you write Single Page Applications. Integrating both platforms presents several hurdles, mainly caused by the fast pace of development of Ember, and the lack of documentation of both Ember and some of the required Django packages. Examples in the net are usually outdated.

Ember has recently moved to support [JSON API](http://jsonapi.org/) (which itself has reached 1.0 recently), and there are not many packages able to implement a JSON API compliant interface on top of Django REST framework (we have chosen [Django REST Framework - JSON API](http://drf-json-api.readthedocs.org/en/latest/)). Besides, since the JSON API itself has some freedom for certain aspects of the interface, the defaults in both Ember and Django side do not necessarily match.

This sample application, together with the frontend application, offer a starting point and a showcase on how to integrate both technologies.

Apart from showing how to interface Django and Ember, the backend application includes a method to serve the Ember SPA directly from the Django application. This way, a deploy of a single instance is enough to serve both Ember frontend and Django API. This reduces complexity and is very useful for small sized projects.

This project does not claim to follow best practices (although we try, so please send us a pull request if you feel that something can be improved!), but what we really aim is to provide a simple, easy to understand starting point for applications integrating Django backend and Ember frontend.

You can find a running demo [here](http://django-ember-showcase.herokuapp.com)

The browsable backend API can be found [here](http://django-ember-showcase.herokuapp.com/api)

The sister (Ember frontend) project of this one can be found [here](https://github.com/gonvaled/frontend-django-ember-showcase)

This project started while writing this [blog post](http://blog.gonvaled.com/ember/Configuring-Django-and-EmberData-interoperability.html)

## Used packages ##

* `Django==1.9.1` : latest version of Django published in PyPi as of this writing
* `dj-database-url==0.3.0` : database URL is defined on the environment
* `dj-static==0.0.6` : to serve static files (required in production)
* `djangorestframework==3.3.2` : REST API framework
* `django-rest-framework-json-api` : Add JSON API support to the DRF. At the time of this writing, JSON API 1.0 support is on the develop branch. We are using the latest available commit on hte develop branch.

For serving in Heroku, we need extra packages
* `gunicorn==19.4.5` : Python WSGI HTTP Server
* `psycopg2==2.6.1` : PostgreSQL adapter for the Python programming language

## Run the development backend in localhost ##

The project has been developed with Python 2.7.6, but should work with no (or little) modifications with Python 3.

* Create a virtualenv: `virtualenv venv`
* Activate the virtualenv: `source venv2.7/bin/activate`
* Install the development requirements: `pip install -r requirements-dev.txt`
* Start the server: `python mangage.py runserver`. Your app is reachable at `http://127.0.0.1:8000/`

## Deploy to Heroku ##

_TODO_

## Embed frontend release ##

_TODO_

## Legal ##

[Daniel Gonzalez](http://gonvaled.com) &copy; 2016

[Licensed under the MIT license](http://www.opensource.org/licenses/mit-license.php)
