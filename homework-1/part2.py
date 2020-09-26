"""
Create a true equation for each comparison operator, and a false question for each comparison operator. Your numbers should be unique in each equation.

For the equals and not equals operators, create two examples: one using numbers, one using strings
"""
from ignore import comparison_tests

less_than, less_than_equal_to, greater_than, greater_than_equal_to, equals_numbers, equals_strings, not_equals_numbers, not_equals_strings = None, None, None, None, None, None, None, None

comparisons = [
    less_than, less_than_equal_to, greater_than, greater_than_equal_to,
    equals_numbers, equals_strings, not_equals_numbers, not_equals_strings
]


def true_comparisons():
    '''Replace None with your comparison equations'''
    less_than = None
    less_than_equal_to = None
    greater_than = None
    greater_than_equal_to = None
    equals_numbers = None
    not_equals_numbers = None
    equals_strings = None
    not_equals_strings = None


def false_comparisons():
    '''Replace None with your comparison equations'''
    less_than = None
    less_than_equal_to = None
    greater_than = None
    greater_than_equal_to = None
    equals_numbers = None
    not_equals_numbers = None
    equals_strings = None
    not_equals_strings = None


## DO NOT EDIT
def main():
    true_comparisons()
    print("True comparisons")
    for i in range(len(comparisons)):
        if comparisons[i]:
            print(comparison_tests[i] + " ................ok")
        else:
            print(comparison_tests[i] + " ................FAIL")

    false_comparisons()
    print("\nFalse Comparisons")
    for i in range(len(comparisons)):
        if comparisons[i] is False:
            print(comparison_tests[i] + " ................ok")
        else:
            print(comparison_tests[i] + " ................FAIL")
