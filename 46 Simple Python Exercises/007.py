# Define a function reverse()that computes the reversal of a string.
# For example, reverse("I am testing") should return the string "gnitset ma I"


def reverse(text):
    reversed_text = list(text)
    reversed_text.reverse()
    return "".join(reversed_text)


if __name__ == '__main__':
    instance = "I am testing"
    msg = (
        "Returns the reverse of a string\n"
        "Instance: {}\n"
        "Output: {}".format(instance, reverse(instance))
    )
    print(msg)
