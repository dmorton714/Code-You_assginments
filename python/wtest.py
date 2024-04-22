import unittest

class TestUserVariables(unittest.TestCase):
    @classmethod
    def variables(cls, A, B):
        # Check if variable 'A' is correctly assigned
        if A != 40:
            raise Exception("Error: Variable 'A' should be assigned the value 40.")
        
        # Check if variable 'B' is correctly assigned
        if B != 60:
            raise Exception("Error: Variable 'B' should be assigned the value 60.")
        
        print("Variable assignment test passed!")

    @classmethod
    def dataType(cls):
        # Add test cases for data types here
        pass
    
    @classmethod
    def conditionals(cls):
        # Add test cases for conditionals here
        pass

if __name__ == '__main__':
    unittest.main(argv=[''], defaultTest='TestUserVariables', exit=False)
    print("Congratulations! Your code passed the tests!")
