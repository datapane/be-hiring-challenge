import requests 
import json 
import os
import ast

ENDPOINT = f"http://localhost:8000/dataset"

def convertBytesToDictionary(content):
    dictStr = content.decode("utf-8")
    records = ast.literal_eval(repr(dictStr))
    converted = json.loads(records)
    return converted

def checkIfFileExists(function):
    def innerFunction(filePath): 
        if os.path.isfile(filePath):
            return function(filePath)
        else: 
            print("File Not found")
            exit()
    return innerFunction

def checkIfFileExistsById(function):
    global ENDPOINT
    def innerFunction(fileID):
        baseUrl = (ENDPOINT + "/check_file/{fileID}").format(fileID=fileID)
        response = requests.get(baseUrl)
        response = convertBytesToDictionary(response.content)
        if response:
            return function(fileID)
        else:
            print("File withe the given ID does not exist")
            exit()
    return innerFunction

def getAllDatasets():
    global ENDPOINT
    baseUrl = ENDPOINT + "/datasets"
    response = requests.get(baseUrl)
    response = convertBytesToDictionary(response.content)
    print(response)

def getDatasetByDatasetId(datasetId):
    global ENDPOINT 
    baseUrl = (ENDPOINT + "/datasets/{datasetId}/").format(datasetId=datasetId)
    response = requests.get(f"{baseUrl}")
    response = convertBytesToDictionary(response.content)
    print("File Name -> ", response["fileName"])
    print("File Size -> ", response["fileSize"])

@checkIfFileExists
def uploadCSVFileToServer(filePath): 
    global ENDPOINT
    baseUrl = ENDPOINT + "/datasets"
    file = open(filePath, "rb")
    response = requests.post(baseUrl, files={"file": file})
    response = convertBytesToDictionary(response.content)
    print("Message -> ", response["message"])
    print("File Path -> ", response["filePath"])
    print("File Name ->", response["fileName"])

@checkIfFileExistsById
def exportFileToExcel(datasetid):
    global ENDPOINT
    baseUrl = (ENDPOINT + "/datasets/{datasetid}/excel").format(datasetid=datasetid)
    response = requests.get(baseUrl)
    response = convertBytesToDictionary(response.content)
    if len(response) == 1: 
        print("Message: ", response["message"])
    else:
        print("Message: ", response["message"])
        print("File Path: ", response["filePath"])
        print("File Name: ", response["fileName"])

@checkIfFileExistsById
def viewFileStats(datasetid):
    global ENDPOINT
    baseUrl = (ENDPOINT + "/datasets/{datasetid}/stats").format(datasetid=datasetid)
    response = requests.get(baseUrl)
    response = convertBytesToDictionary(response.content)
    print(response)

@checkIfFileExistsById
def getNumericalPlots(datasetid):
    global ENDPOINT
    baseUrl = (ENDPOINT + "/datasets/{datasetid}/plot").format(datasetid=datasetid)
    response = requests.get(baseUrl)
    print(response.content)

@checkIfFileExistsById
def deleteDatasetById(datasetid):
    global ENDPOINT
    baseUrl = (ENDPOINT + "/datasets/{datasetid}").format(datasetid=datasetid)
    response = requests.delete(baseUrl)
    print(response.content.decode("utf-8"))