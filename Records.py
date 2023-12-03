# Authors: Mohamed Gabr
# student_number: 041057619
# Date: 2023-10-06
# Description: This file contains the Records class and the Record class



""" This class is the parent class of the Records class and is used to create objects
    The Records class inherits the Record class """

class Record:

    """ This constructor assigns values to attributes, the object uses the
        method and sets the value inputted by the user to the class """
    def __init__(self, ref_number):
        self.ref_number = ref_number


""" Inherits the Record class object """
class Records(Record):

    """ Uses the attributes in the method header to create objects
        and the data entered for the class attributes """
    def __init__(self, ref_number, disclosure_group, title_en, title_fr, name, purpose_en, purpose_fr,
                 start_date, end_date, destination_en, destination_fr, airfare, other_transport, lodging, meals,
                 other_expenses, total, additional_comments_en, additional_comments_fr, owner_org, owner_org_title):
        self.ref_number = ref_number
        self.disclosure_group = disclosure_group
        self.title_en = title_en
        self.title_fr = title_fr
        self.name = name
        self.purpose_en = purpose_en
        self.purpose_fr = purpose_fr
        self.start_date = start_date
        self.end_date = end_date
        self.destination_en = destination_en
        self.destination_fr = destination_fr
        self.airfare = airfare
        self.other_transport = other_transport
        self.lodging = lodging
        self.meals = meals
        self.other_expenses = other_expenses
        self.total = total
        self.additional_comments_en = additional_comments_en
        self.additional_comments_fr = additional_comments_fr
        self.owner_org = owner_org
        self.owner_org_title = owner_org_title
        super().__init__(ref_number)
        self.ref_number = ref_number
        self.disclosure_group = disclosure_group
        self.title_en = title_en
        self.title_fr = title_fr
        self.name = name
        self.purpose_en = purpose_en
        self.purpose_fr = purpose_fr
        self.start_date = start_date
        self.end_date = end_date
        self.destination_en = destination_en
        self.destination_fr = destination_fr
        self.airfare = airfare
        self.other_transport = other_transport
        self.lodging = lodging
        self.meals = meals
        self.other_expenses = other_expenses
        self.total = total
        self.additional_comments_en = additional_comments_en
        self.additional_comments_fr = additional_comments_fr
        self.owner_org = owner_org
        self.owner_org_title = owner_org_title

    """ Prints all attributes in string format """
    def __str__(self):
        return super().__str__() + " " + self.ref_number + " " + self.disclosure_group + " " + self.title_en + " " + self.title_fr + " " \
               + self.name + " " + self.purpose_en + " " + self.purpose_fr + " " + self.start_date + " " \
               + self.end_date + " " + self.destination_en + " " + self.destination_fr + " " + self.airfare + " " \
               + self.other_transport + " " + self.lodging + " " + self.meals + " " + self.other_expenses + " " \
               + self.total + " " + self.additional_comments_en + " " + self.additional_comments_fr + " " \
               + self.owner_org + " " + self.owner_org_title
