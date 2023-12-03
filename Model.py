# Authors: Mohamed Gabr
# student_number: 041057619
# Date: 2023-10-06

from Controller import Controller

"""Object for Model class"""
class Model(object):

    """ Creates an object and initializes list """
    def __init__(self):
        # Instance created
        self.controller = Controller()

    """ Reload the list """
    def reload_list(self):
        self.controller.load_list()
        print("List reloaded")

    """ Create a new file """
    def create_file(self):
        self.controller.create_file()
        print("File created")

    """ Displays the list """
    def display_list(self, user_input):
        self.controller.display_list(user_input)
        print("List displayed")

    """ Create new record """
    def create_records(self, ref_number, disclosure_group, title_en, title_fr, name, purpose_en, purpose_fr,
                 start_date, end_date, destination_en, destination_fr, airfare, other_transport, lodging, meals,
                 other_expenses, total, additional_comments_en, additional_comments_fr, owner_org, owner_org_title):
        self.controller.add_records(ref_number, disclosure_group, title_en, title_fr, name, purpose_en, purpose_fr,
                 start_date, end_date, destination_en, destination_fr, airfare, other_transport, lodging, meals,
                 other_expenses, total, additional_comments_en, additional_comments_fr, owner_org, owner_org_title)
        print("Data created")

    """ Update an existing record """
    def update_recordsList(self, selected_records, ref_number, disclosure_group, title_en, title_fr, name, purpose_en, purpose_fr,
                 start_date, end_date, destination_en, destination_fr, airfare, other_transport, lodging, meals,
                 other_expenses, total, additional_comments_en, additional_comments_fr, owner_org, owner_org_title):
        self.controller.edit_records(selected_records, ref_number, disclosure_group, title_en, title_fr, name, purpose_en, purpose_fr,
                 start_date, end_date, destination_en, destination_fr, airfare, other_transport, lodging, meals,
                 other_expenses, total, additional_comments_en, additional_comments_fr, owner_org, owner_org_title)
        print("Information updated")

    """ Delete a record """
    def delete_records(self, delete_records):
        self.controller.delete_records(delete_records)
        print("Successfully deleted")

    """ Display choice """
    def display_choice(self, choice):
        self.controller.display_recordsData(choice)
        
        
    """ Display graph """
    def display_graph(self):
        self.controller.display_graph()
        print("Graph displayed")