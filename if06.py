def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """

    sum = 0
    if a > 0:
        sum+=1
    if b > 0:
        sum+=1
    if c > 0:
        sum+=1
    if sum > 1:
        return "there are a lot of positive numbers"
    else:
        return "there are a lot of negative numbers"
print(main(-2,4,1))
print(main(2,-4,-6))