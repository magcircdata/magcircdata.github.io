import GAS_execution as GAS
from store_to_db import *

import sys


circ_response = GAS.get_spreadsheet_data()
headers = circ_response['headers']
circ_data = circ_response['data']

USER = "dsfsd"
PASSWORD = "AFSF"
HOST = "1.12.121.3"
DATABASE = "MYDB"


def streamline_geographical_data():
	connection = connect_to_db(USER, PASSWORD, HOST, DATABASE)

	COL_NAMES = ["magazine_id", "location"]

	TABLE_NAME = "circulation_by_location"

	write_to_db(connection, headers, circ_data, TABLE_NAME, COL_NAMES)


def streamline_non_geographical_data():
	connection = connect_to_db(USER, PASSWORD, HOST, DATABASE)

	COL_NAMES = ["magazine_id", "other_col_names"]

	TABLE_NAME = "circulation_data"

	write_to_db(connection, headers, circ_data, TABLE_NAME, COL_NAMES)


data_calls = {
	"location": streamline_geographical_data,
	"non-location": streamline_non_geographical_data
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
				print "Try one of these {}".format(",".join(data_types))
	print "Finished streamlining data"

