import click
from click.decorators import option
import requests
import re
import os , shutil
from pprint import pprint
API_URL = os.getenv("DATAPANE_URL") if os.getenv("DATAPANE_URL") else "http://localhost:8000/dataset/"

def CmdIDFactory(request_type:str ): 
  
    """Factory Method"""
    localizers = { 
        "list": FileInfo, 
        "delete": DeleteFile, 
        "excel": ExcelConvert, 
        "plot" :PlotData,
        "stats":StatData
    } 
  
    return localizers[request_type]() 

def CmdFactory(request_type:str ): 
  
    localizers = { 
        "list": ListFiles, 
        "create": CreateFile, 
    } 
  
    return localizers[request_type]() 


class FileInfo:
    def make_requests(self, id=None):
        error =  False
        error_msg = ""
        try :
            response =  requests.get(API_URL+id+"/")
            if response.status_code != 200 :
                error = True
                error_msg = "cannot connect to api server"
                return error , error_msg
        except Exception as ex :
            error = True
            error_msg = "error occured {}".format(ex)
            return error , error_msg
        return error , response.json()

class DeleteFile:
    def make_requests(self, id=None):
        error =  False
        error_msg = ""
        try :
            response =  requests.delete(API_URL+ id +"/")
            if response.status_code != 204 :
                error = True
                error_msg = "cannot connect to api server"
                return error , error_msg
        except Exception as ex :
            error = True
            error_msg = "error occured {}".format(ex)
            return error , error_msg
        return error , "deleted"

class ExcelConvert:
    def make_requests(self , id=None):
        error =  False
        error_msg = ""
        try :
            response =  requests.get(API_URL+ id +"/excel/")
            if response.status_code != 200 :
                error = True
                error_msg = "cannot connect to api server"
                return error , error_msg
        except Exception as ex :
            error = True
            error_msg = "error occured {}".format(ex)
            return error , error_msg

        d = response.headers['content-disposition']
        fname = re.findall("filename=(.+)", d)[0]
 
        with open(fname, 'wb') as target:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, target)
        return error , "download {}".format(fname)

class StatData :
    def make_requests(self ,id=None):
        error =  False
        error_msg = ""
        try :
            response =  requests.get(API_URL+id+"/stats/")
            if response.status_code != 200 :
                error = True
                error_msg = "cannot connect to api server"
                return error , error_msg
        except Exception as ex :
            error = True
            error_msg = "error occured {}".format(ex)
            return error , error_msg
        return error , response.json()

class PlotData :
     def make_requests(self , id=None):
        error =  False
        error_msg = ""
        try :
            response =  requests.get(API_URL+ id +"/excel/")
            if response.status_code != 200 :
                error = True
                error_msg = "cannot connect to api server"
                return error , error_msg
        except Exception as ex :
            error = True
            error_msg = "error occured {}".format(ex)
            return error , error_msg

        d = response.headers['content-disposition']
        fname = re.findall("filename=(.+)", d)[0]
 
        with open(fname, 'wb') as target:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, target)
        return error , "download {}".format(fname)   


class ListFiles:
    def make_requests(self, id=None):
        error =  False
        error_msg = ""
        try :
            response =  requests.get(API_URL)
            if response.status_code != 200 :
                error = True
                error_msg = "cannot connect to api server"
                return error , error_msg
        except Exception as ex :
            error = True
            error_msg = "error occured {}".format(ex)
            return error , error_msg
        return error , response.json()

class CreateFile:
    def make_requests(self, id=None):
        error =  False
        error_msg = ""
        try :
            files = {'file': open(id, 'rb')}
            response =  requests.post(API_URL, files=files)
            if response.status_code != 200 :
                error = True
                error_msg = "cannot connect to api server"
                return error , error_msg
        except Exception as ex :
            error = True
            error_msg = "error occured {}".format(ex)
            return error , error_msg
        return error , response.json()


@click.group()
def cli():
    """Example script."""
    click.echo('''Usage:   
  datapanecli <command> [options]

Commands:
  list                        List all Datasets.
  create  /path/to/file       Create the Dataset   
  item  [id] [operations]     specify the File id and one of the operation info ,delete, excel , stat ,plot

''')

@cli.command()
@click.option('--id', type=int, help="item id of a the data ")
@click.option('--process', type=str, help=" process one of the operation(info , delete ,excel , stat ,plot) ")

def item(id ,process):
    option_val =  process
    id  = str(id )
    error = ""
    json = ""
    if option_val not in ["delete", "list","excel","stats", "plot"] :
        click.echo(" should specify one of the operation(info , delete ,excel , stat ,plot)")
        return 
    
    if not id :
        click.echo("should provide id for the file")
    
    request_object = CmdIDFactory(option_val)
    error , json = request_object.make_requests(id)
    if error :

        click.echo("error occured {}".format(json) )
        return
    click.echo(json)    

@cli.command()
def list():
    error , json = CmdFactory("list").make_requests()
    if error :
        click.echo("error occured {}".format(json) )
        return
    click.echo(pprint(json) )

@cli.command()
@click.option('--filepath',type=click.Path(exists=True),help='create the datasets , specify the path of the dataset.')
def create(filepath):
    option_val =  '%s' % filepath
    if not option_val :
        click.error("file path should be specified ")
    error , json = CmdFactory("create").make_requests()
    if error :
        click.echo("error occured {}".format(json) )
        return
    if json :
        click.echo("file create")


