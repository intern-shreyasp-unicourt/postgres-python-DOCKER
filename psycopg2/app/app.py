import psycopg2
import csv

# Connect to an existing database
conn = psycopg2.connect(
    database = "sitedatabase", 
    user = "postgres", 
    host= '192.168.5.26',
    password = "postgres",
    port = 5439)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS site_data(
            SiteHeading VARCHAR (200) NOT NULL,
            SiteDescription VARCHAR (2000) NOT NULL
            );""")

# :TODO
# copy_csv_to_db = '''\copy site_data(SiteHeading,SiteDescription) 
# FROM './site_data.csv' 
# WITH (FORMAT CSV)
# DELIMITER ',' 
# CSV HEADER;'''
# cur.execute(copy_csv_to_db) 


# Open the CSV file
with open('site_data.csv', 'r') as f:
    # Create a CSV reader object
    reader = csv.DictReader(f)

    # Insert the data from each row into the PostgreSQL table
    for row in reader:
        cur.execute(
            "INSERT INTO site_data (SiteHeading, SiteDescription) VALUES (%s, %s)",
            (row['SiteHeading'], row['SiteDescription'])
        )
# Commit the changes

conn.commit()

cur.close()
conn.close()

