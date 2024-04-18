import sqlite3

# Connect to the database
conn = sqlite3.connect('survey_database.db')
cursor = conn.cursor()

# Define the district, mandal, and village
district = 'Rangaredddy'
mandal = 'Rajendranagar'
village = 'Rajendranagar'

# Define the SQL query to get the survey numbers for the given district, mandal, and village
query = """
    SELECT survey_number
    FROM surveys
    WHERE district = ? AND mandal = ? AND village = ?
"""

# Execute the query using the cursor
cursor.execute(query, (district, mandal, village))

# Fetch all the rows returned by the query
rows = cursor.fetchall()

# Initialize an empty list to store the survey numbers
survey_numbers = []

# Iterate over the rows and extract the survey numbers
for row in rows:
    survey_numbers.append(row[0])

# Print the survey numbers
for survey_number in survey_numbers:
    print(survey_number)

# Close the database connection
conn.close()