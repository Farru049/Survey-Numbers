# Survey-Numbers
This Python script is used to print the survey numbers for a given district, mandal, and village. It uses the SQLite database survey_database.db and the sqlite3 module to execute SQL queries.

The script first connects to the database and creates a cursor object to execute SQL queries. It then defines the district, mandal, and village names that we want to query.

Next, it defines the SQL query to get the survey numbers for the given district, mandal, and village. The query selects the survey_number column from the surveys table where the district, mandal, and village columns match the given values.

The query is then executed using the cursor, and all the rows returned by the query are fetched. The survey numbers are extracted from the rows and stored in a list.

Finally, the survey numbers are printed, and the database connection is closed.

To use the script, simply replace the district, mandal, and village variables with the desired values. The script will print the survey numbers for the given district, mandal, and village.

Note that this script assumes that the surveys table has columns named survey_number, district, mandal, and village. If your table has different column names, we need to adjust the script accordingly.
