
# ---------------------------- Optimal solution --------------------------

def romanToInt(s: str) -> int:
    """Takes a roman interger and return its int value.

    Parameters:
        s (str): Roman integer.
    
    Returns:
        int: Integer value.
    """

    hash_map = {
        "I" : 1,
        "IV" : 4,
        "V" : 5,
        "IX" : 9,
        "X" : 10,
        "XL" : 40,
        "L" : 50,
        "XC" : 90,
        "C" : 100,
        "CD" : 400,
        "D" : 500,
        "CM" : 900,
        "M" : 1000,
    }

    total_sum = 0
    i = 0

    while i < len(s):
        if i < len(s)- 1 and s[i:i+2] in hash_map :
            total_sum += hash_map[s[i:i+2]]
            i += 2
        else:
            total_sum += hash_map[s[i]]
            i += 1

    return total_sum