
import unittest
from Model import Model

programmer = "Mohamed Gabr"
course = "Computer Programming"
print(course, " - Program by: ", programmer)

class MyTests(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.model = Model()

    def test_getDisplay_list(self):
        self.assertEqual(self.model.reload_list(), self.model.create_file())

if __name__ == '__main__':
    unittest.main()