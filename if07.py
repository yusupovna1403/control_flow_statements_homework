def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a > 0:
        if a % 2 == 1:
            return "positive odd number"
        else:
            return "positive even number"
    else:
        if a % 2 == 1:
            return "negative odd number"
        else:
            return "negative even number"

print(main(57))
print(main(-24))