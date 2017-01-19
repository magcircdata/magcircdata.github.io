import GAS_execution as GAS
from store_to_db import *

import sys

USER = ""
PASSWORD = ""
HOST = ""
DATABASE = ""


def streamline_geographical_data():
	circ_response = GAS.get_spreadsheet_data("getGeoData")
	headers = circ_response['headers']
	circ_data = circ_response['data']

	connection = connect_to_db(USER, PASSWORD, HOST, DATABASE)

	COL_NAMES = ["magazine_id", "location_id", "sample_issue_date", "sample_period_end_date", "num_mail_subscriptions", "num_single_copy_sales"]

	TABLE_NAME = "circulation_data_by_location"

	write_to_db(connection, headers, circ_data, TABLE_NAME, COL_NAMES)

def streamline_magazine_lookup_table_data():
	circ_response = GAS.get_spreadsheet_data("getMagazineIdLookupTable")
	headers = circ_response['headers']
	circ_data = circ_response['data']

	connection = connect_to_db(USER, PASSWORD, HOST, DATABASE)

	COL_NAMES = ["magazine_id", "title"]

	TABLE_NAME = "magazines"

	write_to_db(connection, headers, circ_data, TABLE_NAME, COL_NAMES)


def streamline_non_geographical_data():
	"""
	NOT FINISHED YET
	:return:
	"""
	circ_response = GAS.get_spreadsheet_data("getGeoData")
	headers = circ_response['headers']
	circ_data = circ_response['data']

	connection = connect_to_db(USER, PASSWORD, HOST, DATABASE)

	COL_NAMES = ["magazine_id", "other_col_names"]
	# magazine_id | type_id | circulation | price | year | month | day

	TABLE_NAME = "circulation_data"

	write_to_db(connection, headers, circ_data, TABLE_NAME, COL_NAMES)


data_calls = {
	"location": streamline_geographical_data,
	# "non-location": streamline_non_geographical_data,
	"magazine": streamline_magazine_lookup_table_data
}

data_types = list(data_calls)


if __name__ == "__main__":
	params = sys.argv[1:]
	if len(params) == 0: #default is to streamline all data
		for data_type in data_calls:
			data_calls[data_type]()
	else:
		for data_type in params:
			if data_type in data_calls:
				data_calls[data_type]()
			else:
				print "Param {} not a valid tag".format(data_type)
				print "Try one of these {}".format(", ".join(data_types))
	print "Finished streamlining data"