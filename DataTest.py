import mysql.connector

# Connection parameters
config = {
    'user': 'root',
    'password': '787878',
    'host': 'localhost',
    'database': 'python_data',
}

# Establish a connection
conn = mysql.connector.connect(**config)

# Create a cursor
cursor = conn.cursor()

# Example: Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS travel_info (
        ref_number VARCHAR(200),
        disclosure_group VARCHAR(200),
        title_en VARCHAR(200),
        title_fr VARCHAR(200),
        name VARCHAR(200),
        purpose_en VARCHAR(200),
        purpose_fr VARCHAR(200),
        start_date VARCHAR(200),
        end_date VARCHAR(200),
        destination_en VARCHAR(200),
        destination_fr VARCHAR(200),
        airfare VARCHAR(200),
        other_transport VARCHAR(200),
        lodging VARCHAR(200),
        meals VARCHAR(200),
        other_expenses VARCHAR(200),
        total VARCHAR(200),
        additional_comments_en VARCHAR(200),
        additional_comments_fr VARCHAR(200),
        owner_org VARCHAR(200),
        owner_org_title VARCHAR(200)
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()
