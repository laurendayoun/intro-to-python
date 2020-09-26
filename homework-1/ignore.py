import part1

comparison_tests = [
    "less_than", "less_than_equal_to", "greater_than", "greater_than_equal_to",
    "equals_numbers", "equals_strings", "not_equals_numbers",
    "not_equals_strings"
]


def part1_test():
    incor = 0
    for s in part1.strings():
        if type(s) != str:
            print("Your string is wrong!")
            incor += 1

    for i in part1.ints():
        if type(i) != int:
            print("Your int is wrong!")
            incor += 1

    for f in part1.floats():
        if type(f) != float:
            print("Your float is wrong!")
            incor += 1

    b1, b2 = part1.bools()
    if (b1 and not b2) or (not b1 and b2):
        print("Got " + str(14 - incor) + "/14 correct")
    else:
        print("Your bools are wrong or not different")
        incor += 2
        print("Got " + str(14 - incor) + "/14 correct")
