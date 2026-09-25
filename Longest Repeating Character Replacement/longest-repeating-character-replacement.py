def characterReplacement(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """

    all_chars = [0] * 26
    left = max_len = max_occurance = 0

    for right in range(len(s)):
        all_chars[ord(s[right]) - ord("A")] += 1
        max_occurance = max(max_occurance , all_chars[ord(s[right]) - ord("A")])

        if (right - left + 1 ) - max_occurance > k:
            all_chars[ord(s[left]) - ord("A")] -= 1
            left += 1

        max_len = max(max_len , right - left + 1)

    return max_len
