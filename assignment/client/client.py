import requests

def send_http_get_request(url, args = None):
	"""Return a json object

	Response returned by sending a get request to the url
	"""
	response = requests.get(url = url, params = args)
	return response.json()

def send_http_post_request(url, data = None, file = None):
	"""Return a json object

	Response returned by sending a post request to the url
	"""
	response = requests.post(url = url, files = file, data = data)
	return response.json()

def send_http_delete_request(url, args = None):
	"""Return a json object

	Response returned by sending a delete request to the url
	"""
	response = requests.delete(url = url, params = args)
	return response.json()

def main():
	""" The main function """
	base_url = "http://127.0.0.1:8000/"
	
	while True:
		command = input("Enter command: ")
		command = command.strip().split()

		# "get_all_datasets" -> GET /datasets/ 
		# To list the uploaded datasets
		if(command[0] == "get_all_datasets"):
			url = base_url + "datasets/"
			try:
				response = send_http_get_request(url)
				print(response)
				print()

			except Exception as e:
				print("Request failed. Error: " + str(e))

		# "create_dataset" ->  POST /datasets/
		# Creates a dataset.
		elif(command[0] == "create_dataset"):
			if(len(command) != 3):
				print("Invalid number of arguments. Required arguments: file_path file_description")
				continue
			file_path = str(command[1])
			file_description = str(command[2])
			file = open(file_path, 'rb')
			url = base_url + "datasets/"
			files = {'file' : file}
			data = {'description' : file_description}
			try:
				response = send_http_post_request(url, data, files)
				print(response)
				print()
			except Exception as e:
				print("Request failed. Error: " + str(e))
			finally:
				file.close()

		# "get_dataset" -> GET /datasets/<id>/
		# Returns the file name, and size of the dataset object
		elif(command[0] == "get_dataset"):
			if(len(command) != 2):
				print("Invalid number of arguments. Required arguments: file_id")
				continue
			file_id = str(command[1])
			url = base_url + "datasets/" + file_id +"/"
			try:
				response = send_http_get_request(url)
				print(response)
				print()

			except Exception as e:
				print("Request failed. Error: " + str(e))

		# "delete_dataset" -> DELETE /datasets/<id>/ 
		# delete the dataset object
		elif(command[0] == "delete_dataset"):
			if(len(command) != 2):
				print("Invalid number of arguments. Required arguments: file_id")
				continue
			file_id = str(command[1])
			url = base_url + "datasets/" + file_id +"/"
			try:
				response = send_http_delete_request(url)
				print(response)
				print()

			except Exception as e:
				print("Request failed. Error: " + str(e))

		# "export_excelfile" -> GET /datasets/<id>/excel/
		# Exports the dataset as an excel file and return the path of the excel file
		elif(command[0] == "export_excelfile"):
			if(len(command) != 2):
				print("Invalid number of arguments. Required arguments: file_id")
				continue
			file_id = str(command[1])
			url = base_url + "datasets/" + file_id +"/excel/"
			try:
				response = send_http_get_request(url)
				print(response)
				print()
			except Exception as e:
				print("Request failed. Error: " + str(e))

		# "get_dataset_stats" -> GET /datasets/<id>/stats/
		# Returns the the stats of the dataset
		elif(command[0] == "get_dataset_stats"):
			if(len(command) != 2):
				print("Invalid number of arguments. Required arguments: file_id")
				continue
			file_id = str(command[1])
			url = base_url + "datasets/" + file_id +"/stats/"
			try:
				response = send_http_get_request(url)
				print("Stats of the requested file:")
				print(response)
				print()
			except Exception as e:
				print("Request failed. Error: " + str(e))

		# "get_dataset_plots" -> GET /datasets/<id>/plot/
		# Generates a PDF file containing a list of histograms of all the numerical columns in the dataset
		# Return the path of the generated PDF file
		elif(command[0] == "get_dataset_plots"):
			if(len(command) != 2):
				print("Invalid number of arguments. Required arguments: file_id")
				continue
			file_id = str(command[1])
			url = base_url + "datasets/" + file_id +"/plot/"
			try:
				response = send_http_get_request(url)
				print("Plots of the numerical columns in the dataset:")
				print(response)
				print()
			except Exception as e:
				print("Request failed. Error: " + str(e))

		# Exit the program
		elif(command[0] == "exit"):
			exit()

		# Command does not matches with any valid command.
		else:
			print("Invalid command. Try again...")

if __name__ == "__main__":
	main()