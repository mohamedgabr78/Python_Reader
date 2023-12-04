class View:
    def display_menu(self):
        print("Travel Information Application")
        print("Program by Mohamed Gabr")
        print("1. Display specific records (1-1000)")
        print("2. Display All records")
        print("3. Add a new record")
        print("4. Update a record")
        print("5. Delete a record")
        print("6. Sort records")
        print("7. Create Database/Table from CSV")
        print("8. Exit")

    def get_user_choice(self):
        try:
            choice = int(input("Enter your choice: "))
            return choice
        except ValueError:
            print("Invalid input. Please enter a number.")
            return self.get_user_choice()

    def get_record_data(self):
        # Prompt the user to enter data for a new record and return it as a dictionary
        record_data = {
            'ref_number': input("Enter Ref Number: "),
            'disclosure_group': input("Enter Disclosure Group: "),
            'title_en': input("Enter Title (English): "),
            'title_fr': input("Enter Title (French): "),
            'name': input("Enter Name: "),
            'purpose_en': input("Enter Purpose (English): "),
            'purpose_fr': input("Enter Purpose (French): "),
            'start_date': input("Enter Start Date: "),
            'end_date': input("Enter End Date: "),
            'destination_en': input("Enter Destination (English): "),
            'destination_fr': input("Enter Destination (French): "),
            'airfare': input("Enter Airfare: "),
            'other_transport': input("Enter Other Transport: "),
            'lodging': input("Enter Lodging: "),
            'meals': input("Enter Meals: "),
            'other_expenses': input("Enter Other Expenses: "),
            'total': input("Enter Total: "),
            'additional_comments_en': input("Enter Additional Comments (English): "),
            'additional_comments_fr': input("Enter Additional Comments (French): "),
            'owner_org': input("Enter Owner Organization: "),
            'owner_org_title': input("Enter Owner Organization Title: ")
        }
        return record_data

    def get_record_id(self):
        return int(input("Enter the ID of the record: "))
    
    def get_sort_choice(self):
        return int(input("Enter the column number to sort by: "))

    def display_records(self, records):
        if not records:
            print("No records found.")
        else:
            for record in records:
                print(record)