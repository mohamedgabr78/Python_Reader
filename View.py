# Authors: Mohamed Gabr
# student_number: 041057619
# Date: 2023-10-06

""" This file contains the View class """

from Model import Model

"""Object for View class"""
class View(object):

    """ Creates an object and initializes list """
    def __init__(self):
        # Instance created
        self.model = Model()

    """ Main menu """
    def main_menu(self):
        print("\nABy Mohamed Gabr")
        print("Main Menu, choose an option: \n"
              "1. Load/Reload data from the dataset \n"
              "2. Write to a new file \n"
              "3. Select one record or all records \n"
              "4. Create and store a new record\n"
              "5. Edit a record \n"
              "6. Delete a record \n"
              "7. Display a graph \n"
              "0. To exit \n")

        option = int(input("Select an option: "))

        # Ensures that the user selects a valid option
        while option != 0:

            # Statement for the user inputs
            if option == 1:
                # Reload data
                Model().reload_list()
                # Print menu
                v.main_menu()

            elif option == 2:
                # Create a file
                Model().create_file()
                # Print menu
                v.main_menu()

            elif option == 3:
                # Option to choose to display all data or a specific one
                choice = int(input("Choose a row from 1 to 1000 or 0 to see all: "))
                Model().display_list(choice)
                # Print menu
                v.main_menu()

            elif option == 4:
                # Data that the user must enter
                ref_number_entry = str(input("Enter Ref Number: "))
                disclosure_group_entry = str(input("Enter Disclosure Group: "))
                title_en_entry = str(input("Enter Title (English): "))
                title_fr_entry = str(input("Enter Title (French): "))
                name_entry = str(input("Enter Name: "))
                purpose_en_entry = str(input("Enter Purpose (English): "))
                purpose_fr_entry = str(input("Enter Purpose (French): "))
                start_date_entry = str(input("Enter Start Date: "))
                end_date_entry = str(input("Enter End Date: "))
                destination_en_entry = str(input("Enter Destination (English): "))
                destination_fr_entry = str(input("Enter Destination (French): "))
                airfare_entry = str(input("Enter Airfare: "))
                other_transport_entry = str(input("Enter Other Transport: "))
                lodging_entry = str(input("Enter Lodging: "))
                meals_entry = str(input("Enter Meals: "))
                other_expenses_entry = str(input("Enter Other Expenses: "))
                total_entry = str(input("Enter Total: "))
                additional_comments_en_entry = str(input("Enter Additional Comments (English): "))
                additional_comments_fr_entry = str(input("Enter Additional Comments (French): "))
                owner_org_entry = str(input("Enter Owner Org: "))
                owner_org_title_entry = str(input("Enter Owner Org Title: "))
                

                # This data is sent to the Model class and later to the Controller class.
                Model().create_records(ref_number_entry, disclosure_group_entry, title_en_entry, title_fr_entry, name_entry, purpose_en_entry, purpose_fr_entry,
                                        start_date_entry, end_date_entry, destination_en_entry, destination_fr_entry, airfare_entry, other_transport_entry, lodging_entry, meals_entry,
                 other_expenses_entry, total_entry, additional_comments_en_entry, additional_comments_fr_entry, owner_org_entry, owner_org_title_entry)
                v.main_menu()

            elif option == 5:
                # Data that the user must enter to edit the record
                selected_records = int(input("Enter the row desired to edit: "))
                ref_number_edit = str(input("Enter the new Ref Number: "))
                disclosure_group_edit = str(input("Enter the new Disclosure Group: "))
                title_en_edit = str(input("Enter the new Title (English): "))
                title_fr_edit = str(input("Enter the new Title (French): "))
                name_edit = str(input("Enter the new Name: "))
                purpose_en_edit = str(input("Enter the new Purpose (English): "))
                purpose_fr_edit = str(input("Enter the new Purpose (French): "))
                start_date_edit = str(input("Enter the new Start Date: "))
                end_date_edit = str(input("Enter the new End Date: "))
                destination_en_edit = str(input("Enter the new Destination (English): "))
                destination_fr_edit = str(input("Enter the new Destination (French): "))
                airfare_edit = str(input("Enter the new Airfare: "))
                other_transport_edit = str(input("Enter the new Other Transport: "))
                lodging_edit = str(input("Enter the new Lodging: "))
                meals_edit = str(input("Enter the new Meals: "))
                other_expenses_edit = str(input("Enter the new Other Expenses: "))
                total_edit = str(input("Enter the new Total: "))
                additional_comments_en_edit = str(input("Enter the new Additional Comments (English): "))
                additional_comments_fr_edit = str(input("Enter the new Additional Comments (French): "))
                owner_org_edit = str(input("Enter the new Owner Org: "))
                owner_org_title_edit = str(input("Enter the new Owner Org Title: "))


                # This data is sent to the Model class and later to the Controller class.
                Model().update_recordsList(selected_records, ref_number_edit, disclosure_group_edit, title_en_edit, title_fr_edit, name_edit, purpose_en_edit, purpose_fr_edit,
                                            start_date_edit, end_date_edit, destination_en_edit, destination_fr_edit, airfare_edit, other_transport_edit, lodging_edit, meals_edit,
                 other_expenses_edit, total_edit, additional_comments_en_edit, additional_comments_fr_edit, owner_org_edit, owner_org_title_edit)
                v.main_menu()

            elif option == 6:
                # Delete a record after entering the row number
                delete_records = int(input("Enter the row desired to delete: "))

                # Pass this line number to the model and then to the controller
                Model().delete_records(delete_records)
                v.main_menu()
                
            elif option == 7:
                # Display a graph
                Model().display_graph()
                v.main_menu()

            # If user selects 0 then exits program
            exit(0)

if __name__ == "__main__":
    v = View()
    v.main_menu()