import click 
import utils

@click.group()
def cli():
    pass

@cli.command()
def listalldatasets(): 
    utils.getAllDatasets()

@cli.command()
@click.argument("datasetid", type=int)
def getdataset(datasetid):
    utils.getDatasetByDatasetId(datasetid)

@cli.command()
@click.argument("filepath", type=str)
def createfile(filepath):
    utils.uploadCSVFileToServer(filepath)

@cli.command()
@click.argument("datasetid", type=int)
def exporttoexcel(datasetid):
    utils.exportFileToExcel(datasetid)

@cli.command()
@click.argument("datasetid", type=int)
def viewstats(datasetid):
    utils.viewFileStats(datasetid)

@cli.command()
@click.argument("datasetid", type=int)
def getplot(datasetid):
    utils.getNumericalPlots(datasetid)

@cli.command()
@click.argument("datasetid", type=int)
def deletedataset(datasetid):
    utils.deleteDatasetById(datasetid)

cli()