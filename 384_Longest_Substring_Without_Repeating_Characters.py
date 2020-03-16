class Solution:
    """
    @param s: a string
    @return: an integer

    版本一：
    拿一个固定的窗口一直滑动，不符合就缩小窗口，继续滑动。 这不是滑动窗口 这是brute force
    """

    def lengthOfLongestSubstring(self, s):

        start = 0
        length = len(s)
        while length:

            for start in range(len(s) - length + 1):
                end = start + length - 1
                if set(s[start:end+1]) == len(s[start:end+1]):
                    return length

            length -= 1



class Solution:
    """
    这才是真正的滑动窗口
    """


    def lengthOfLongestSubstring2(self,s):
        if not s:
            return 0

        left, right = 0,0
        unique_chars = set()
        result = 0

        while left < len(s) and right < len(s):
            if s[right] not in unique_chars:
                unique_chars.add(s[right])
                result = max(result, len(unique_chars))
                right += 1
            else:
                unique_chars.remove(s[left])
                left += 1

        return result


if __name__ == '__main__':
    a = Solution()
    string = "an++--viaj"
    result = a.lengthOfLongestSubstring2(string)

