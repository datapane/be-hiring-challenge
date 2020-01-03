### Installation:
Requirements:
- Python 3.6 runtime
- Django 3.0.2
- Other dependencies in `Pipfile`

Procedure:
- Install [python](https://www.python.org/downloads/) in your environment.
- Navigate to the cloned repository.
    ```
    cd <project_directory_name>     # be-hiring-challenge
    ```
- Install `pipenv` for dependency management
    ```
    pip install pipenv
    ```
- Copy `.env.example` to `.env`
    ```
    cp .env.example .env
    ```
- Use pipenv to install other dependencies from `Pipfile`, add `--skip-lock` if locking is slow
    ```
    pipenv install --dev --skip-lock
    ```
- Change to `server/src` directory and optionally activate virtual environment, if you don't want to activate env, use `pipenv run` to run python scripts
    ```
    cd server/src
    source "$(pipenv --venv)"/bin/activate
    ```
- Make database migrations
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
- Run development server on localhost
    ```
    python manage.py runserver
    ```
    