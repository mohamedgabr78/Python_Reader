# this class is a concrete subclass that inherits from DatabaseModel and provides the implementation specific to MySQL

import threading
import mysql.connector
from DatabaseModel import DatabaseModel
import csv


class Model(DatabaseModel):
    def __init__(self, config):
        super().__init__(config)
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()
        self.records = []  # Store records in a list
        self.load_thread = None  # Thread for loading data

    def insert_record(self, record_data):
        # Fetch the maximum value in the 'row_num' column
        max_row_num_query = "SELECT MAX(row_num) FROM travel_info"
        self.cursor.execute(max_row_num_query)
        max_row_num = self.cursor.fetchone()[0]

        if max_row_num is not None:
            # Increment the maximum value by 1
            new_row_num = max_row_num + 1
        else:
            # If the 'row_num' column is empty, start with 1
            new_row_num = 1

        # Add the calculated 'row_num' value to the record_data dictionary
        record_data['row_num'] = new_row_num

        # Insert the new record into the database
        insert_query = """
        INSERT INTO travel_info (row_num, ref_number, disclosure_group, title_en, title_fr, name, 
                                purpose_en, purpose_fr, start_date, end_date, destination_en, 
                                destination_fr, airfare, other_transport, lodging, meals, 
                                other_expenses, total, additional_comments_en, 
                                additional_comments_fr, owner_org, owner_org_title)
        VALUES (%(row_num)s, %(ref_number)s, %(disclosure_group)s, %(title_en)s, %(title_fr)s, %(name)s, 
                %(purpose_en)s, %(purpose_fr)s, %(start_date)s, %(end_date)s, %(destination_en)s, 
                %(destination_fr)s, %(airfare)s, %(other_transport)s, %(lodging)s, %(meals)s, 
                %(other_expenses)s, %(total)s, %(additional_comments_en)s, %(additional_comments_fr)s, 
                %(owner_org)s, %(owner_org_title)s)
        """
        self.cursor.execute(insert_query, record_data)
        self.connection.commit()

    def update_record(self, record_id, new_data):
        # Update an existing record in the database
        update_query = """
        UPDATE travel_info
        SET ref_number = %(ref_number)s, disclosure_group = %(disclosure_group)s, 
            title_en = %(title_en)s, title_fr = %(title_fr)s, name = %(name)s, 
            purpose_en = %(purpose_en)s, purpose_fr = %(purpose_fr)s, start_date = %(start_date)s, 
            end_date = %(end_date)s, destination_en = %(destination_en)s, 
            destination_fr = %(destination_fr)s, airfare = %(airfare)s, 
            other_transport = %(other_transport)s, lodging = %(lodging)s, meals = %(meals)s, 
            other_expenses = %(other_expenses)s, total = %(total)s, 
            additional_comments_en = %(additional_comments_en)s, 
            additional_comments_fr = %(additional_comments_fr)s, 
            owner_org = %(owner_org)s, owner_org_title = %(owner_org_title)s
        WHERE row_num = %(row_num)s
        """
        new_data['row_num'] = record_id  # Add the ID to the data
        self.cursor.execute(update_query, new_data)
        self.connection.commit()

    def delete_record(self, record_id):
        # Delete a record from the database
        delete_query = "DELETE FROM travel_info WHERE row_num = %s"
        self.cursor.execute(delete_query, (record_id,))
        self.connection.commit()

    def get_records(self, start, end):
        # Retrieve records from the database within the specified range
        select_query = """
        SELECT row_num, ref_number, disclosure_group, title_en, title_fr, name, purpose_en,
               purpose_fr, start_date, end_date, destination_en, destination_fr, airfare,
               other_transport, lodging, meals, other_expenses, total, additional_comments_en,
               additional_comments_fr, owner_org, owner_org_title
        FROM travel_info
        WHERE row_num BETWEEN %s AND %s
        """
        self.cursor.execute(select_query, (start, end))
        records = self.cursor.fetchall()
        return records
    
    def create_table(self, csv_file_path):
        # Read the CSV file and extract column names
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            columns = reader.fieldnames

        # Establish a connection
        conn = mysql.connector.connect(**self.config)

        # Create a cursor
        cursor = conn.cursor()

        # Create the database if not exists
        cursor.execute('CREATE DATABASE IF NOT EXISTS travel_data')
        cursor.execute('USE travel_data')

        # Create the table dynamically
        create_table_query = f'''
            CREATE TABLE IF NOT EXISTS travel_info (
                {', '.join(f'{column} VARCHAR(200)' for column in columns)}
            )
        '''
        cursor.execute(create_table_query)

        # Commit changes
        conn.commit()

        # Insert data into the table
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                insert_query = f'''
                    INSERT INTO travel_info ({', '.join(columns)})
                    VALUES ({', '.join(["%s"] * len(columns))})
                '''
                cursor.execute(insert_query, tuple(row.values()))

        # Commit changes and close the connection
        conn.commit()
        conn.close()
        
        
    def sort_records(self, key):
    # Sort records based on the specified key
        if not self.records:
            print("No records to sort.")
            return

        try:
            self.records = sorted(self.records, key=lambda x: x[key])
            print(f"Records sorted based on column '{key}'.")
        except KeyError:
            print(f"Invalid column name: '{key}'. Sorting aborted.")
    
    
    def load_data_from_file(self, csv_file_path):
        def load_data():
            try:
                with open(csv_file_path, 'r') as file:
                    reader = csv.DictReader(file)
                    self.records = list(reader)
                    print("Data loaded successfully.")
            except Exception as e:
                print(f"Error loading data: {e}")

        # Check if a thread is already running
        if self.load_thread and self.load_thread.is_alive():
            print("A data loading thread is already running.")
        else:
            # Create a new thread and start it
            self.load_thread = threading.Thread(target=load_data)
            self.load_thread.start()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()