# Datasets API & CLI

## Requirements

- Docker

## Installation

- Clone the repository and `cd` into the project directory
- Run `docker-compose up --build` to build and start the services
- When the build is up, app will be available at [http://0.0.0.0:8000](http://0.0.0.0:8000)
- On Linux, to make change to files (if you're not running Docker rootless), take ownership of all files: <br>
    `sudo chown -R $USER:$USER .`