import bisect


class Solution:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """

    def maxEnvelopes(self, envelopes):
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        result = []

        for envelope in envelopes:
            height = envelope[1]
            if len(result) == 0 or height > result[-1]:
                result.append(height)
            else:
                index = bisect.bisect_left(result, height)
                result[index] = height

        return len(result)

if __name__ == '__main__':
    a = Solution()
    envelopes = [[5,4],[6,4],[6,7],[2,3]]
    a.maxEnvelopes(envelopes)