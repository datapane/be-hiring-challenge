======
client
======

Python API client


Installation guide
--------

Create a virtual environment

    $ python3 -m venv /path/to/new/virtual/environment

With your environment activated, execute the following line to install the command:

    $ pip install .


Features
--------

The following commands are available:

    $ datapane-client datasets list

    $ datapane-client datasets get --id <id>

    $ datapane-client datasets post <path-to-dataset>

    $ datapane-client datasets delete --id <id>

    $ datapane-client datasets get-stats --id <id>

    $ datapane-client datasets get-excel --id <id>  --destination <path-to-save-the-file>

    $ datapane-client datasets get-plot --id <id> --destination <path-to-save-the-file>


Improvements
--------

- No tests included.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
