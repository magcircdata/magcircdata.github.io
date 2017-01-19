import MySQLdb

def connect_to_db(user, pw, host, database):
	return MySQLdb.connect(user=user,
							passwd=pw,
							host=host,
							db=database)

#instead of headers and rows
#do dictionary of col_names to values

#VALUES (%(col_name1)s, %(col_name2)s, %(col_name3)s)


def write_to_db(connection, headers, rows, table_name, col_names):
	cur = connection.cursor() #get the cursor

	col_names_query_str = "(" + (', '.join(col_names)) + ")"
	values_query_str = "(" + (", ".join(["%s" for _ in col_names])) + ")"

	#ignore, silently ignores the error of duplicate entries
	query_template = "INSERT IGNORE INTO {} {} VALUES {}".format(table_name, col_names_query_str, values_query_str)

	cur.executemany(
		query_template,
		rows
	) #makes sure that the data is cleaned which is important because values/row comes from a Google Sheet


	#as long as table_names are hardcoded, no need to sanitize the following mysql commands
	# cur.execute("CREATE TABLE temp_GAS_unique_entries_table SELECT DISTINCT * FROM {}".format(table_name))
    #
	# cur.execute("DROP TABLE {}".format(table_name))
    #
	# cur.execute("RENAME TABLE temp_GAS_unique_entries_table TO {}".format(table_name))
    #
	# cur.execute("DROP TABLE IF EXISTS temp_GAS_unique_entries_table")



	connection.commit()
	cur.close()
	connection.close()