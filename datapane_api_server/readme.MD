# Technical Challenge API Server

## Server setup
The setup uses docker and as such, requires that you have docker install
To build the image,  navigate to the location of the `Dockerfile` and run the command 
``` bash
docker build -t datapane .
```
To run the image, 
```bash
docker run -it -p 80:8000 datapane
```

Alternatively, you can download the required packages in `requirements.txt` and run the project locally.
## Server use
The server comes empty and you would need to upload some data to get going
To upload, visit the landing page
## sample url for dataset delete
`http://0.0.0.0:8000/datasets/1/delete`
## sample url for dataset stats
`http://0.0.0.0:8000/datasets/1/stats`
## sample url for dataset export to excel
`http://0.0.0.0:8000/datasets/1/excel`
## sample url for dataset export to pdf
`http://0.0.0.0:8000/datasets/1/plot`
## sample url for dataset file name
`http://0.0.0.0:8000/1

## Upload or view all datasets
`http://0.0.0.0:8000` or `http://0.0.0.0:8000/datasets`