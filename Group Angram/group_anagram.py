def check_anagram(s: str, t: str) -> bool:
    """Check if two strings are anagrams.

    Parameters:
        s (str): The first string.
        t (str): The second string.

    Returns:
        bool: True if both strings are anagrams, otherwise False.
    """

    if len(s) != len(t):
        return False

    alphabets = [0] * 26

    for i in range(len(s)):
        alphabets[ord(s[i])-ord("a")] +=1
        alphabets[ord(t[i])-ord("a")] -=1

    for i in range(len(alphabets)):
        if alphabets[i] != 0:
            return False

    return True

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    all_anagrams = []

    for elment in strs:
        angrams = [elment]
        for second_elment in strs:
            if check_anagram(elment , second_elment) and second_elment not in angrams:
                angrams.append(second_elment)

        angrams = sorted(angrams)
        if angrams not in all_anagrams:
            all_anagrams.append(angrams)

    return all_anagrams

print(groupAnagrams(["a"]))
