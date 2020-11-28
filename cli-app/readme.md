# CLI Client App

## Requirements

- Python 3.x
- venv - `pip install venv`

## Installation

- Create virtual environment <br>
    `venv env`
- Activate environment <br>
    `source env/bin/activate`
- Install the app <br>
    `pip install --editable .`
    
## Usage
 
    dataset [OPTIONS] COMMAND [ARGS]...
    
- Options:
    - `help` -- opens man page
    
- Commands:
    - `ls` -- retrieves datasets
    - `get` `id` -- shows a dataset
        - Arguments:
            - `id` -- integer: dataset identifier
    - `create` `--file` `-f` -- creates a dataset
        - Options:
            - `--file` `-f` -- string: takes path to CSV file

    - `delete` `id` -- deletes a dataset
        - Arguments:
            - `id` -- integer: dataset identifier
    - `excel` `id` -- exports excel for a dataset
        - Arguments:
            - `id` -- integer: dataset identifier
    - `stats` `id` -- shows stats for a dataset
        - Arguments:
            - `id` -- integer: dataset identifier
    - `plot` `id` -- exports plot on a PDF for a dataset
        - Arguments:
            - `id` -- integer: dataset identifier