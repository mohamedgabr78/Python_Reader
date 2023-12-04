from Model import Model
from View import View

class Controller:
    
    # Controller class for managing user interactions and coordinating between Model and View.
    
    
    # Initialize the Controller with a Model and View.
    # :param model: An instance of the Model class.
    # :param view: An instance of the View class.
    def __init__(self, model, view):
        
        self.model = model
        self.view = view


    # Run the main loop of the application, handling user input and coordinating with the Model and View.
    def run(self):
        while True:
            self.view.display_menu()
            choice = self.view.get_user_choice()

            if choice == 1:
                start = int(input("Enter start record number: "))
                end = int(input("Enter end record number: "))
                records = self.model.get_records(start, end)
                self.view.display_records(records)

            elif choice == 2:
                records = self.model.get_records(1, 1000)
                self.view.display_records(records)
            
            elif choice == 3:
                record_data = self.view.get_record_data()
                self.model.insert_record(record_data)
                print("Record added successfully.")

            elif choice == 4:
                record_id = self.view.get_record_id()
                if self.model.get_records(record_id, record_id):
                    new_data = self.view.get_record_data()
                    self.model.update_record(record_id, new_data)
                    print("Record updated successfully.")
                else:
                    print("Record not found.")

            elif choice == 5:
                record_id = self.view.get_record_id()
                if self.model.get_records(record_id, record_id):
                    self.model.delete_record(record_id)
                    print("Record deleted successfully.")
                else:
                    print("Record not found.")
                    
            elif choice == 6:
                sort_choice = self.view.get_sort_choice()
                records = self.model.sort_records(sort_choice)
                self.view.display_records(records)
                    
            elif choice == 7:
                self.model.create_table('./travel.csv')
                self.model.load_data_from_file('./travel.csv')
                print("Database/Table created successfully.")
                break
                

            elif choice == 8:
                self.model.close_connection()
                print("Exiting the application.")
                break
            
            else:
                print("Invalid choice. Please select a valid option from the menu.")

if __name__ == "__main__":
    # Database configuration
    config = {
        'user': 'root',
        'password': '787878',
        'host': 'localhost',
        'database': 'python_data',
    }


    # Run the application using polymorphism
    # This allows you to easily switch to a different database model in the future 
    # without changing the Controller or other parts of your code.
    
    mysql_model = Model(config)
    controller = Controller(mysql_model, View())
    controller.run()
