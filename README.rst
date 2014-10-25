django-runuwsgi
===============

Application for Django, to run uwsgi.


Installation
------------

Requires
~~~~~~~~

::

    django >= 1.6

Install with ``pip``:

Run ``pip install git+https://github.com/silentsokolov/django-runuwsgi.git``

Or ``pip install django-runuwsgi``

Open ``settings.py`` and add ``runuwsgi`` to your ``INSTALLED_APPS``:

.. code:: python

    INSTALLED_APPS = (
        ...
        'runuwsgi',
        ...
    )


Example usage
-------------

.. code::

    python manage.py runuwsgi --port 9000 --socket /tmp/project.sock --home /project/env --chdir /project --module app.wsgi --autoreload 1


If you need to serve static, but you're not using Nginx, use ``--static-map /=/path/to/static``.
