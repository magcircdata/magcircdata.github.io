import mysql

def connect_to_db(user, pw, host, database):
	return mysql.connector.connect(user=user,
							password=pw,
							host=host,
							database=database)

#instead of headers and rows
#do dictionary of col_names to values

#VALUES (%(col_name1)s, %(col_name2)s, %(col_name3)s)

def write_to_db(connection, headers, rows, table_name, col_names):
	cur = connection.cursor() #get the cursor

	col_names_query_str = "(" + (', '.join(col_names)) + ")"
	values_query_str = "(" + (", ".join(["%s" for _ in col_names])) + ")"

	cur.executemany(
		"INSERT INTO {} {} VALUES {}".format(col_names_query_str, values_query_str),
		rows
	) #makes sure that the data is cleaned


	connection.commit()
	cur.close()
	connection.close()