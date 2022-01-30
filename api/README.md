# api

Datapane BE Hiring challenge

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


Prerequisites
-------------

* Docker; if you don't have it yet, follow the `installation instructions`_;
* Docker Compose; refer to the official documentation for the `installation guide`_.
* Pre-commit; refer to the official documentation for the [pre-commit](https://pre-commit.com/#install).

.. _`installation instructions`: https://docs.docker.com/install/#supported-platforms
.. _`installation guide`: https://docs.docker.com/compose/install/

Build the Stack
---------------

This can take a while, especially the first time you run this particular command on your development system::

    $ docker-compose -f local.yml build
    $ docker-compose -f local.yml up
    $ docker-compose -f local.yml run --rm django python manage.py migrate

Once the container is up & running, you will be able to access the API through the address localhost:8000.

To execute any python command into the container use:

    $ docker-compose -f local.yml run --rm django <your-commands>


Improvements
---------------

- Everything should be tested.
- In general, it's not a good idea to transform the input file before saving the model. The file could be huge and this process could take too much time. For this case, we should create the object, and trigger a background task in order to store the dataset.
- Pre-calculate excel and plot results instead of generating them on the fly.
- There should be a way to transform datasets without having to write them on disk and load them again.

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create an **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy api

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html).

### Celery

This app comes with Celery.

To run a celery worker:

``` bash
cd api
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

### Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at <https://sentry.io/signup/?code=cookiecutter> or download and host it yourself.
The system is set up with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
