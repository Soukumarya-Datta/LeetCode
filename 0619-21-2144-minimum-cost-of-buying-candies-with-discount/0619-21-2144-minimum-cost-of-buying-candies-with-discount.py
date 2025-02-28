class Solution:
    def minimumCost(self, cost):
        len_cost = len(cost)
        cost.sort(reverse=True)
        ret_val = 0
        n = 1
        while (n <= len_cost):
            c = cost[n-1]
            if (n % 3 == 0):
                ret_val += 0
            else:
                ret_val += c
            n += 1

        return ret_val