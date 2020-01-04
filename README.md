# register.pacificyearlymeeting.org
Registration portal for Pacific Yearly Meeting.

## Initial project scope
Data model/database model definitions:
- registrant: someone who registers 
- (user) account: someone who logs in to manage registrants

## Development
In order to run and develop this code locally, you will need a few system-wide dependencies installed:

- [Git](https://git-scm.com/)
- [Python 3.7 +](https://www.python.org/)
- [Poetry](https://python-poetry.org/)

Once those dependencies have been installed, use the following steps to clone and initialize this project:

1. clone this repository to a local folder on your computer
2. in your terminal, change directory into the cloned project (where this README is located)
3. install the project sourcecode dependencies with `poetry install`
4. activate the development environment with the command `poetry shell`
5. set up a local sqlite database with `python manage.py migrate`
6. create a superuser with `python manage.py createsuperuser`
7. run the server with `python manage.py runserver`
8. visit the site at https://localhost:8000
9. log in with your superuser account

From there, you browse around the Wagtail admin.

Changing existing code files should automatically refresh the server, but you may need to manually refresh browser pages to see the changes.

## Resources
The following links are related to libraries/apps we have used to develop the site.

[Wagtail CMS](https://Wagtail.io) is the main content management system/developer framework. Wagtail is built on [Django](https://djangoproject.com), which provides many common components for web applications.

The following Django apps were used to create the website user registration process:
- https://django-registration.readthedocs.io/en/3.0.1/
- https://github.com/fusionbox/django-authtools