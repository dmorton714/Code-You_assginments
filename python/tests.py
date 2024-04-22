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
    def dataType(cls, A, B):
        # Check if variable 'A' is of type int
        if not isinstance(A, int):
            raise Exception("Error: Variable 'A' should be assigned an integer value.")
        
        # Check if variable 'B' is of type float
        if not isinstance(B, float):
            raise Exception("Error: Variable 'B' should be assigned a float value.")
        
        print("Data type test passed!")
    
    # @classmethod
    # def conditionals(cls):
    #     # Add test cases for conditionals here
    #     pass

if __name__ == '__main__':
    A = 40
    B = 60.0
    
    # Run variable assignment test
    TestUserVariables.variables(A, B)
    
    # Run data type test
    TestUserVariables.dataType(A, B)
    
    # Run other test methods
    TestUserVariables.conditionals()
    
    print("Congratulations! Your code passed the tests!")
