def printExampleHeader(exampleNum):
    print(f"~Example {exampleNum}:\n\n")

#DEMO:


printExampleHeader(1)
# Create a simple function add_numbers(a, b) and write a docstring for it explaining what the function does, 
# what parameters it expects, and what it returns.

def add_numbers(a, b):
    """
    [DESCRIPTION]

    Parameters:
    

    Returns:
    
    """
    return a + b

print(add_numbers(3, 4))  # Should print 7


printExampleHeader(2)
#Show how to use a simple assert statement to test if a function is working as expected.
def test_add_numbers():
    assert add_numbers(3, 4) == 7, "Test failed"
    assert add_numbers(-1, 1) == 0, "Test failed"
    print("All tests passed!")

test_add_numbers()


printExampleHeader(3)
#Add exception handling to the add_numbers function to deal with cases where the inputs are not numbers.

def better_add_numbers(a, b):
    """
    Adds two numbers together.
    """
    try:
        return a + b
    except TypeError:
        return "Both inputs must be numbers"

print(better_add_numbers(3, "four"))  # Should print an error message
