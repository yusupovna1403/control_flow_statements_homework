def main(a,b,c):
    """
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    sum = 0
    if a > 0:
        sum+=1
    if b > 0:
        sum+=1
    if c > 0:
        sum+=1
    return sum
print(main(-2,4,1))
print(main(2,-4,-6))