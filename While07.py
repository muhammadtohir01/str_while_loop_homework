def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    d=1
    while i<=len(s):
        if i%2==0:
            d+=1
        i+=1
    return d
print(main('3444434'))