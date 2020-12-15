# Installation
Requirements :- Docker , Docker-Compose

```sh
$ sudo docker-compose up -d

```
# Migrations
## login into docker container
 ```sh
 $ sudo docker exec -it container_id /bin/bash
 
 ```

## performs migrations for auth and contenttypes contrib apps   
```python 
$ python3.6 manage.py migrate 

```

## creates the rest of the database   
```python
$ python3.6 manage.py migrate --run-syncdb  

```

The App will start listening on localhost at port 8000

# Installing CLI

```sh
$ cd datapane_cli
$ pip install .

```

