class Solution(object):
    def compress(self, s1):

        compress = ""
        consecutive = 1
        current_char =s1[0]

        for idx,char in enumerate(s1[1:]):
            if current_char == char:
                consecutive += 1
            else:
                compress+=current_char.repeat( consecutive )
                consecutive = 0
                current_char = char
                if length(compress) > length(s1):
                    return s1
        return compress





if __name__ == "__main__":
    x = Solution()
    haystack = "aaaaabccccccdfgqqqqq"

    print(x.compress(haystack))
