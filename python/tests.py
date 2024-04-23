import unittest
import sys
from io import StringIO

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
    
    @classmethod
    def conditionals(cls, A, B):
        # Capture stdout
        sys.stdout = StringIO()
        
        # User code
        exec("""if A > B:
    print("A is greater than B")
elif A == B:
    print("A is equal to B")
else:
    print("B is greater than A")""")
        
        # Get output
        result = sys.stdout.getvalue().strip()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check if the result matches the expected output
        expected_result = "B is greater than A"  # Expected output for the given values of A and B
        if result == expected_result:
            print("Conditional test passed!")
        else:
            print("Conditional test failed! Expected:", expected_result, "but got:", result)


if __name__ == '__main__':
    A = 40
    B = 60.0
    
    # Run variable assignment test
    TestUserVariables.variables(A, B)
    
    # Run data type test
    TestUserVariables.dataType(A, B)
    
    # Run other test methods
    TestUserVariables.conditionals(A, B)
    
    print("Congratulations! Your code passed the tests!")

# _______________________________________________________________________________________________________________________________


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
