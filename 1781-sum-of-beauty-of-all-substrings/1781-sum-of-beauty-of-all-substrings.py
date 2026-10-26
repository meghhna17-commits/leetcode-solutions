class Solution(object):
    def beautySum(self, s):
        n = len(s)
        ans = 0

        for i in range(n):
            freq = {}

            for j in range(i, n):
                if s[j] in freq:
                    freq[s[j]] += 1
                else:
                    freq[s[j]] = 1

                maxi = max(freq.values())
                mini = min(freq.values())

                ans += maxi - mini

        return ans
