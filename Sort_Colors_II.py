class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        combine = [0 for _ in range(k + 1)]

        for num in colors:
            combine[num] += 1

        index = 0
        for color in range(1, k + 1):
            for _ in range(combine[color]):
                colors[index] = color
                index += 1


