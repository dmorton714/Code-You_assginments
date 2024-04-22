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
