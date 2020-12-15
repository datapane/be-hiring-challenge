### Installation
Requirements :- Docker , Docker-Compose

```sh
$ sudo docker-compose up -d

```
# Migrations
login into docker container   
python3.6 manage.py migrate    
performs migrations for auth and contenttypes contrib apps   

python3.6 manage.py migrate --run-syncdb   
creates the rest of the database   

The App will start listening on localhost at port 8000

# installing Cli

```sh
$ cd datapane_cli
$ pip install .

```

