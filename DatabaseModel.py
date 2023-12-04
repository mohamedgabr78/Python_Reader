# DatabaseModel is an abstract class,that defines the common interface for database models. 

from abc import ABC, abstractmethod

class DatabaseModel(ABC):
    def __init__(self, config):
        self.config = config
        self.connection = None
        self.cursor = None

    @abstractmethod
    # Insert a new record into the database.
    # :param record_data: A dictionary containing the data for the new record.   
    def insert_record(self, record_data):
        pass

    @abstractmethod
    # Update an existing record in the database.
    # :param record_id: The ID of the record to update.
    # :param new_data: A dictionary containing the updated data for the record.
       
    def update_record(self, record_id, new_data):
        pass

    @abstractmethod
    def delete_record(self, record_id):
        pass

    @abstractmethod
    def get_records(self, start, end):
        pass

    @abstractmethod
    def close_connection(self):
        pass