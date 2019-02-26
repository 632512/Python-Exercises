# Define a function max_of_three()that takes three numbers as arguments
# and returns the largest of them


def max_of_any(numbers):
    int_typed = [int(x) for x in numbers]
    int_typed.sort(reverse=True)
    return int_typed[0]


if __name__ == '__main__':
    random_input = [1, 3, 4, 6, 2]
    msg = (
        "Returns the highest number\n"
        "Input: {}\n"
        "Output: {}".format(random_input, max_of_any(random_input))
    )
    print(msg)
