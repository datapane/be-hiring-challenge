Prerequisites:

1. Python 3.7
2. docker 19.03
3. docker-compose 1.25.0



- Add python 3.7 to the path


- install virtualenv using `pip3 install virtualenv`

- create a new virtualenv using `python3 -m virtualenv venv`

- Activate virtualenv using `source venv/bin/activate`

- clone source code  using: `git clone https://github.com/Nishant23/be-hiring-challenge.git`

- `cd be-hiring-challenge`

- `pip install -r requirements.txt`

- `docker-compose up -d`

- `pip install cli_tools/dist/cli_tools-1.0-py3-none-any.whl`

- COMMAND LINE CLIENT
    1. GET /datasets/ = `cli-tools list-all`
    
    2. POST /datasets/ = `cli-tools create --file=<filepath>`
    
    3. GET /datasets/<id>/ = `cli-tools get --id=<dataset_id>`
    
    4. DELETE /datasets/<id>/ = `cli-tools delete --id=<dataset_id>`
    
    5. GET /datasets/<id>/excel/ = `cli-tools excel --id=<dataset_id>`
    
    6. GET /datasets/<id>/plot/ = `cli-tools plot --id=<dataset_id>`
    
    7. GET /datasets/<id>/stats/ = `cli-tools stats --id=<dataset_id>`





