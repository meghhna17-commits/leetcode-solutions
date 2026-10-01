class Solution:
    def aggregateTimeSeries(self, series1, series2):
        i = j = 0
        n, m = len(series1), len(series2)
        ans = []

        while i < n or j < m:
            if j == m or (i < n and series1[i][0] < series2[j][0]):
                ans.append([
                    series1[i][0],
                    series1[i][1] + (series2[j][1] if j < m else 0)
                ])
                i += 1

            elif i == n or series2[j][0] < series1[i][0]:
                ans.append([
                    series2[j][0],
                    (series1[i][1] if i < n else 0) + series2[j][1]
                ])
                j += 1

            else:
                ans.append([
                    series1[i][0],
                    series1[i][1] + series2[j][1]
                ])
                i += 1
                j += 1

        return ans