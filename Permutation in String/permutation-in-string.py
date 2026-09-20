

# -------------------------- Optimal Solution ---------------
def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    s1_map = [0] * 26
    s2_map = [0] * 26

    for i in range(len(s1)):
        s1_map[ord(s1[i]) - ord("a")] += 1
        s2_map[ord(s2[i]) - ord("a")] += 1

    for i in range(len(s2) - len(s1)):
        if s1_map == s2_map:
            return True

        s2_map[ord(s2[i + len(s1)]) - ord("a")] += 1
        s2_map[ord(s2[i]) - ord("a")] -= 1

    return s1_map == s2_map


# --------------------------- My solution --------------------------------------------------

# def checkInclusion(self, s1, s2):
#     """
#     :type s1: str
#     :type s2: str
#     :rtype: bool
#     """
    
#     s1 = sorted(s1)
#     len_1 = len(s1)
#     for i in range(len(s2) - len_1 + 1):
#         current_slide = s2[i:i + len_1]
#         if s1 == sorted(current_slide):
#             return True
    
#     return False