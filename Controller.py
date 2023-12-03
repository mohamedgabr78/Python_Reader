# Authors: Mohamed Gabr
# student_number: 041057619
# Date: 2023-10-06

import csv
import pandas as pd
from matplotlib import pyplot as plt
from Records import Records

""" This class is the parent class of the Records class and is used to create objects"""

class Controller(object):
    # creates an empty list
    recordsList = []

    """ Load list """
    def load_list(self):
        # Try to open the file, if it is missing or unavailable an alert is shown
        try:
            # Read the new data from a CSV file
            with open('travel.csv', 'r') as csv_file:
                # Use a CSV reader to read the data
                reader = csv.reader(csv_file)

                # Assuming the first row contains column names
                columns = next(reader)

                for row in reader:
                    # Map the row data to the records class attributes
                    ref_number = row[0]
                    disclosure_group = row[1]
                    title_en = row[2]
                    title_fr = row[3]
                    name = row[4]
                    purpose_en = row[5]
                    purpose_fr = row[6]
                    start_date = row[7]
                    end_date = row[8]
                    destination_en = row[9]
                    destination_fr = row[10]
                    airfare = row[11]
                    other_transport = row[12]
                    lodging = row[13]
                    meals = row[14]
                    other_expenses = row[15]
                    total = row[16]
                    additional_comments_en = row[17]
                    additional_comments_fr = row[18]
                    owner_org = row[19]
                    owner_org_title = row[20]
                    
                    

                    # Create a new records object and add it to the list
                    records_temp = Records(
                        ref_number, disclosure_group, title_en, title_fr, name, purpose_en, purpose_fr,
                 start_date, end_date, destination_en, destination_fr, airfare, other_transport, lodging, meals,
                 other_expenses, total, additional_comments_en, additional_comments_fr, owner_org, owner_org_title
                    )

                    self.recordsList.append(records_temp)

                # Number of rows to be printed 
                del self.recordsList[1000:]

        # File is unavailable or not found the exception is printed
        except FileNotFoundError:
            print("File not found / unavailable")

    """ Create a file """
    def create_file(self):
        # Open a new csv file
        with open('Newrecords.csv', 'w', newline='') as csv_file:
            # Writer method to insert data on the file
            writer = csv.writer(csv_file)

            # Writes the headers at the top of the database file
            writer.writerow(["ref_number", "disclosure_group", "title_en", "title_fr", "name", "purpose_en", "purpose_fr",
                             "start_date", "end_date", "destination_en", "destination_fr", "airfare", "other_transport", "lodging", "meals",
                             "other_expenses", "total", "additional_comments_en", "additional_comments_fr", "owner_org", "owner_org_title"])

            # Write all data from the list into the file
            for records in self.recordsList:
                # Write to the rows
                writer.writerow([records.ref_number, records.disclosure_group, records.title_en, records.title_fr, records.name, records.purpose_en,
                                 records.purpose_fr, records.start_date, records.end_date, records.destination_en,
                                 records.destination_fr, records.airfare, records.other_transport, records.lodging, records.meals,
                                 records.other_expenses, records.total, records.additional_comments_en, records.additional_comments_fr,
                                 records.owner_org, records.owner_org_title])


    """ Display a specific row or all rows """
    def display_list(self, number):
        lineCounter = 0
        # Check user input
        if number < 0 or number > len(self.recordsList):
            print("Select a number between 0 and", len(self.recordsList) - 1)
            return

        # Columns (headers)
        print("ref_number  disclosure_group  title_en  title_fr  name  purpose_en  purpose_fr start_date  end_date  destination_en  destination_fr  airfare  other_transport  lodging  meals other_expenses  total  additional_comments_en  additional_comments_fr  owner_org  owner_org_title ")

        # Print the whole list
        if number == 0:
            for row in self.recordsList:
                lineCounter += 1
                print(lineCounter, end=": ")
                print(row.ref_number, row.disclosure_group, row.title_en, row.title_fr, row.name, row.purpose_en, row.purpose_fr,
                      row.start_date, row.end_date, row.destination_en, row.destination_fr, row.airfare, row.other_transport, row.lodging, row.meals,
                      row.other_expenses, row.total, row.additional_comments_en, row.additional_comments_fr, row.owner_org, row.owner_org_title)

        # Prints the data that the user has chosen
        else:
            print("Row #", number, ":\n           ", end=' ')
            # Print the specific data based on the user's choice
            selected_row = self.recordsList[number - 1]
            print(selected_row.ref_number, selected_row.disclosure_group, selected_row.title_en, selected_row.title_fr, selected_row.name, selected_row.purpose_en, selected_row.purpose_fr,
                  selected_row.start_date, selected_row.end_date, selected_row.destination_en, selected_row.destination_fr, selected_row.airfare, selected_row.other_transport, selected_row.lodging, selected_row.meals,
                  selected_row.other_expenses, selected_row.total, selected_row.additional_comments_en, selected_row.additional_comments_fr, selected_row.owner_org, selected_row.owner_org_title)

    """ Add a new data to the list """
    def add_records(self, ref_number, disclosure_group, title_en, title_fr, name, purpose_en, purpose_fr,
                 start_date, end_date, destination_en, destination_fr, airfare, other_transport, lodging, meals,
                 other_expenses, total, additional_comments_en, additional_comments_fr, owner_org, owner_org_title):

        # add the new data to the list
        self.recordsList.append(Records(ref_number, disclosure_group, title_en, title_fr, name, purpose_en, purpose_fr,
                 start_date, end_date, destination_en, destination_fr, airfare, other_transport, lodging, meals,
                 other_expenses, total, additional_comments_en, additional_comments_fr, owner_org, owner_org_title))

    """ Edit pre-existing data in the list """
    def edit_records(self, selected_records, ref_number, disclosure_group, title_en, title_fr, name, purpose_en, purpose_fr,
                 start_date, end_date, destination_en, destination_fr, airfare, other_transport, lodging, meals,
                 other_expenses, total, additional_comments_en, additional_comments_fr, owner_org, owner_org_title):

        # edit the data from the list
        self.recordsList[selected_records - 1] = Records(ref_number, disclosure_group, title_en, title_fr, name, purpose_en, purpose_fr,
                 start_date, end_date, destination_en, destination_fr, airfare, other_transport, lodging, meals,
                 other_expenses, total, additional_comments_en, additional_comments_fr, owner_org, owner_org_title)

    """ Edit an existing data to the list """
    def delete_records(self, delete_records):

        # Delete the new data from the list
        del self.recordsList[delete_records - 1]

    """ Display data """
    def display_recordsData(self, x):

        # Load list
        self.load_list()

        # To show first 1000 records
        del self.recordsList[x:]

        # Back list to a dataframe
        data = pd.DataFrame([t.__dict__ for t in self.recordsList])

        # Add columns to the dataframe
        data.columns = ['ref_number', 'disclosure_group', 'title_en', 'title_fr', 'name', 'purpose_en', 'purpose_fr',
                 'start_date', 'end_date', 'destination_en', 'destination_fr', 'airfare', 'other_transport', 'lodging', 'meals',
                 'other_expenses', 'total', 'additional_comments_en', 'additional_comments_fr', 'owner_org', 'owner_org_title']
        
        
    
    def display_graph(self):

        data = {'Vice Chair':'1076.91$', 'Board Member':'2153.74$',
                'Chief Executive Officer':'2597.14$', 'Chair':'4128.74$', 'Board Of Directors':'6522.74$'}
        
        

        geo = list(data.keys())
        values = list(data.values())

        fig = plt.figure(figsize=(15, 5))

        # creating the bar plot
        plt.bar(geo, values, color='#ECD574', edgecolor='#744529', width=0.4)

        plt.xlabel("Title")
        plt.ylabel("Total")
        plt.title("Total Expenses of each Title")
        plt.show()    