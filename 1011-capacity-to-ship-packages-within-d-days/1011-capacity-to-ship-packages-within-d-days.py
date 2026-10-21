class Solution(object):
    def shipWithinDays(self, weights, days):
        low=max(weights)
        high=sum(weights)
        ans=high
        while(low<=high):
            mid=(low+high)//2
            day=1
            load=0
            for w in weights:
                if load+w<=mid:
                    load+=w
                else:
                    day+=1
                    load=w
            if day<=days:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans     

        