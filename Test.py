import unittest
from Model import Model

programmer = "Mohamed Gabr"
course = "Computer Programming"
print(course, " - Program by: ", programmer)

class MyTests(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        # Create a temporary config for testing
        test_config = {
        'user': 'root',
        'password': '787878',
        'host': 'localhost',
        'database': 'python_data',
        }
        self.model = Model(test_config)

    def test_getDisplay_list(self):
        # Specify the range of records we want to retrieve (500 to 51)
        start = 500
        end = 510
        records = self.model.get_records(start, end)
        self.assertEqual(records[0][0], 500)
        
    def test_insertRecord(self):
        # Create a sample record to insert
        record_data = {
            'ref_number': 'ABC123',
            'disclosure_group': 'Group A',
            'title_en': 'English Title',
            'title_fr': 'French Title',
            'name': 'John Doe',
            'purpose_en': 'English Purpose',
            'purpose_fr': 'French Purpose',
            'start_date': '2020-01-01',
            'end_date': '2020-01-02',
            'destination_en': 'English Destination',
            'destination_fr': 'French Destination',
            'airfare': '100',
            'other_transport': '100',
            'lodging': '100',
            'meals': '100',
            'other_expenses': '100',
            'total': '500',
            'additional_comments_en': 'English Comments',
            'additional_comments_fr': 'French Comments',
            'owner_org': 'Organization',
            'owner_org_title': 'Organization Title'
    }

    # Insert the record into the model
        self.model.insert_record(record_data)
        # Retrieve the record from the database
        records = self.model.get_records(1000, 1000)
        # Check if the record was inserted correctly
        self.assertEqual(records[0][0], 1000)


if __name__ == '__main__':
    unittest.main()