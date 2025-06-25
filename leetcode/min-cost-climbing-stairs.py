class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cac = [0] * len(cost)
        cac[0] = cost[0]
        cac[1] = cost[1]

        for i in range(2, len(cost)):
            cac[i] = min(cac[i-1], cac[i-2]) + cost[i]

        return(min(cac[-1], cac[-2]))