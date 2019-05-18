Taken from LongestSubstring_With_K.py:
    1. c = min(set(s), key=s.count)   -- least frequent char in string s

    2. max(self.longestSubstring(t, k) for t in s.split(c))   -- List Comprehensions for each substring

