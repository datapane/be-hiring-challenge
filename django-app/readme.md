# Datasets API

## Requirements

- Docker

## Installation

- Clone the repository and `cd` into the project directory
- Build and start the services <br>
    `docker-compose up`
- When the build is up, app will be available at [http://0.0.0.0:8000](http://0.0.0.0:8000)
- (Optional) Take ownership of the files for editing <br>
    `sudo chown -R $USER:$USER .`
- Stop the containers using `stop` rather than `down` to preserve DB, migrations, and data <br>
    `docker-compose stop`