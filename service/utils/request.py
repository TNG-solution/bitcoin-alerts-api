import os, sys
from service.types.file import File
from cerver import *
from cerver.http import *

def http_get_form_data_values(request, values=[]) -> (dict, dict):
	"""
	Function to get all params in a list
	# Parameters
	------------
	### request: Request
		Request of the current route
	### values: list
		List of strings representing name of variables are needed
	# Returns
	-----------
	body: Dict, files: Dict
	"""
	body = {}
	files = {}

	for value in values:
		try:
			retval = http_request_multi_parts_get_value(request, value.encode("utf-8"))
			retval = retval.contents.str
			retval = retval.decode("utf-8")
			body[value] = retval
		except:
			try:
				file = http_request_multi_parts_get_saved_filename(request, value.encode("utf-8"))
				filename = http_request_multi_parts_get_filename(request, value.encode("utf-8"))
	
				if file is not None:
					file = file.decode("utf-8")
					filename = filename.decode("utf-8")
					files[value] = File(file, filename)

			except:
				pass
	
	return body, files

def http_get_params_list(request) -> list:
	"""
	Function to get all params in a list
	# Parameters
	------------
	### request: Request
		Request of the current route
	# Returns
	-----------
	A list with n_params
	"""
	try:
		params = []
		n_params = http_request_get_n_params(request)
		for i in range(n_params):
			try:
				params.append(http_request_get_param_at_idx(request, i).contents.str.decode("utf-8"))
			except:
				pass

		return params
	except:
		return []
