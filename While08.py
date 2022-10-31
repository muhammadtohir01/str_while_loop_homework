def main(s):
    """
    A string of numbers is given. Find how many odd numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    d=0
    while i<len(s):
        if str(s[i]).isdigit():
         if int(s[i])%2==1:
            d+=1
        else:
            d+=0
        i+=1
    return d
print(main('1567534'))