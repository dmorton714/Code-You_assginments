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





# test 2 
# - - - - - - - - - - - - - - - -  - -- - - - - 

# Week 2 Assignments
class TestWeek2(unittest.TestCase):
    @classmethod
    def test_variable_assignment(cls, A, B, C):
        # Check if variables are correctly assigned
        if not isinstance(A, float) or A != 1:
            raise Exception("Error: Variable 'A' should be assigned the value 1 as a float.")
        
        if not isinstance(B, int) or B != 2:
            raise Exception("Error: Variable 'B' should be assigned the value 2 as an integer.")
        
        if not isinstance(C, int) or C != 3:
            raise Exception("Error: Variable 'C' should be assigned the value 3 as an integer.")
        
        print("Variable assignment test passed!")

    @classmethod
    def test_list_creation(cls, my_list):
        # Check if my_list contains A, B, and C
        if len(my_list) != 3:
            raise Exception("Error: Length of 'my_list' should be 3.")
        
        expected_values = [1.0, 2, 3]
        for i, value in enumerate(my_list):
            if value != expected_values[i]:
                raise Exception(f"Error: Value at index {i} in 'my_list' should be {expected_values[i]}.")

        print("List creation test passed!")


if __name__ == '__main__':
    A = float(1)
    B = int(2)
    C = int(3)
    
    # Create the list
    my_list = [A, B, C]
    
    # Run variable assignment test
    TestWeek2.test_variable_assignment(A, B, C)
    
    # Run list creation test
    TestWeek2.test_list_creation(my_list)
