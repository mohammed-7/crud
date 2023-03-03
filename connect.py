from psycopg2 import connect 

# conn_string = "host='host_name'\   
# dbname = 'database_name' user='user_name'\
# password='your_password'"
conn_string = "host='host_name' \
dbname='database_name' user='user_name'\
password='your_password'"

conn = connect(conn_string)
