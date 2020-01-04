# Dataset Management API Server

## Requirements

Be sure you have the following installed on your development machine:

+ Python >= 3.6.4
+ pandas == 0.25.3
+ Django == 2.2.9
+ django-picklefield == 2.0
+ djangorestframework == 3.11.0
+ matplotlib == 3.1.2
+ XlsxWriter == 1.2.7

## Project Installation

To setup a local development environment:

Create a virtual environment in which to install Python pip packages. With [virtualenv](https://pypi.python.org/pypi/virtualenv),
```bash
virtualenv -p python3 venv            # create a virtualenv
source venv/bin/activate   # activate the Python virtualenv 
```

or with [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/),
```bash
mkvirtualenv -p python3 venv   # create and activate environment
workon venv   # reactivate existing environment
```

Clone GitHub Project,
```bash
git clone https://github.com/saadmk11/be-hiring-challenge.git

cd be-hiring-challenge

git checkout challenge

cd dataset_management
```

Install development dependencies,
```bash
pip install -r requirements.txt
```

Migrate Database,
```bash
python manage.py migrate
```

Run the web application locally,
```bash
python manage.py runserver # 127.0.0.1:8000
```


# API Documentation


## Get All Datasets:

* **URL**

  `/datasets/`

* **Method:**

  `GET`

* **Success Response:**

  * **Code:** 200 <br />
  * **Content:** 
    ```json
    [
        {
            "id": 23,
            "name": "sample_data_1",
            "url": "http://127.0.0.1:8000/datasets/23/"
        },
        {
            "id": 22,
            "name": "sample_data_2",
            "url": "http://127.0.0.1:8000/datasets/22/"
        }
    ]
    ```
    
## Create Single Dataset:

* **URL**

  `/datasets/`

* **Method:**

  `POST`
  
* **Data Params**
  ```json
  {
      "csv_file": "file.csv"
  }
  ```

* **Success Response:**

  * **Code:** 201 <br />
  * **Content:** 
    ```json
    {
        "id": 29,
        "name": "sample_data_2",
        "url": "http://127.0.0.1:8000/datasets/29/"
    }
    ```
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:**
    ```json
    {
        "csv_file": [
            "No file was submitted."
        ]
    }
    ```

## Get Single Dataset:

* **URL**

  `/datasets/<dataset_id>/`

* **Method:**

  `GET`

* **Success Response:**

  * **Code:** 200 <br />
  * **Content:** 
    ```json
    {
        "id": 23,
        "name": "sample_data_1",
        "created_at": "2020-01-04T08:24:07.984742Z",
        "size": 220,
        "excel_url": "http://127.0.0.1:8000/datasets/23/excel/",
        "plot_url": "http://127.0.0.1:8000/datasets/23/plot/",
        "stat_url": "http://127.0.0.1:8000/datasets/23/stats/"
    }
    ```

## Delete Single Dataset:

* **URL**

  `/datasets/<dataset_id>/`

* **Method:**

  `DELETE`

* **Success Response:**

  * **Code:** 204 <br />
  * **Content:** None
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:**
    ```json
    {
        "detail": "Not found."
    }
    ```
    
## Get Dataset Stats:

* **URL**

  `/datasets/<dataset_id>/stats/`

* **Method:**

  `GET`

* **Success Response:**

  * **Code:** 204 <br />
  * **Content:** 
  ```json
  {
    "stats": {
        "id": [
            10.0,
            5.5,
            3.0276503540974917,
            1.0,
            3.25,
            5.5,
            7.75,
            10.0
        ],
        "zip": [
            10.0,
            55897.0,
            20311.33047231411,
            24140.0,
            42859.5,
            54263.0,
            71328.5,
            83973.0
        ],
        "version": [
            10.0,
            0.5999999999999999,
            1.1702778228589004e-16,
            0.6,
            0.6,
            0.6,
            0.6,
            0.6
        ]
    }
  }
  ```
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:**
    ```json
    {
        "detail": "Not found."
    }
    ```

## Export Dataset to Excel:

* **URL**

  `/datasets/<dataset_id>/excel/`

* **Method:**

  `GET`

* **Success Response:**

  * **Code:** 200 <br />
  * **Content-type:** 'application/ms-excel'

 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:**
    ```json
    {
        "detail": "Not found."
    }
    ```
    
## Export Dataset histogram plot to PDF:

* **URL**

  `/datasets/<dataset_id>/plot/`

* **Method:**

  `GET`

* **Success Response:**

  * **Code:** 200 <br />
  * **Content-type:** 'application/pdf'

 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:**
    ```json
    {
        "detail": "Not found."
    }
    ```
