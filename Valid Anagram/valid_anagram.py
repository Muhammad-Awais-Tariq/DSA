
def isAnagram(s, t):

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