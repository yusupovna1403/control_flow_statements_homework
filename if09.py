def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    d_1 = a % 10
    d_2 = a // 10
    num = d_1 * 10 + d_2
    if num <= a:
        return True
    else:
        return False
print(main(57))
print(main(21))