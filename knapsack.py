"""
Version 1
"""
from urllib3.connectionpool import xrange

"""

def knapsack(W, wt, val, n):
    dp = [[0 for i in range(W + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W], dp





if __name__ == "__main__":
    val = [3, 2, 4, 4]
    wt = [4, 3, 2, 3]
    n = 4
    w = 6
    F = [[0] * (w + 1)] + [[0] + [-1 for i in range(w + 1)] for j in range(n + 1)]
    optimal_solution, _ = knapsack(w, wt, val, n)
    print(optimal_solution)

"""
import numpy as np

'''
------------------------------------------------
Use dynamic programming (DP) to solve 0/1 knapsack problem
Time complexity: O(nW), where n is number of items and W is capacity
------------------------------------------------
knapsack_dp(values,weights,n_items,capacity,return_all=False)
Input arguments:
  1. values: a list of numbers in either int or float, specifying the values of items
  2. weights: a list of int numbers specifying weights of items
  3. n_items: an int number indicating number of items
  4. capacity: an int number indicating the knapsack capacity
  5. return_all: whether return all info, defaulty is False (optional)
Return:
  1. picks: a list of numbers storing the positions of selected items
  2. max_val: maximum value (optional)
------------------------------------------------
'''
def knapsack_dp(values,weights,n_items,capacity,return_all=False):
    check_inputs(values,weights,n_items,capacity)

    table = np.zeros((n_items+1,capacity+1),dtype=np.float32)
    keep = np.zeros((n_items+1,capacity+1),dtype=np.float32)

    for i in xrange(1,n_items+1):
        for w in xrange(0,capacity+1):
            wi = weights[i-1] # weight of current item
            vi = values[i-1] # value of current item
            if (wi <= w) and (vi + table[i-1,w-wi] > table[i-1,w]):
                table[i,w] = vi + table[i-1,w-wi]
                keep[i,w] = 1
            else:
                table[i,w] = table[i-1,w]

    picks = []
    K = capacity

    for i in xrange(n_items,0,-1):
        if keep[i,K] == 1:
            picks.append(i)
            K -= weights[i-1]

    picks.sort()
    picks = [x-1 for x in picks] # change to 0-index


    max_val = table[n_items,capacity]

    return picks,max_val

def check_inputs(values,weights,n_items,capacity):
    # check variable type
    assert(isinstance(values,list))
    assert(isinstance(weights,list))
    assert(isinstance(n_items,int))
    assert(isinstance(capacity,int))
    # check value type
    assert(all(isinstance(val,int) or isinstance(val,float) for val in values))
    assert(all(isinstance(val,int) for val in weights))
    # check validity of value
    assert(all(val >= 0 for val in weights))
    assert(n_items > 0)
    assert(capacity > 0)

if __name__ == '__main__':
    values = [2,3,4]
    weights = [1,2,3]
    n_items = 3
    capacity = 3
    picks, max_value = knapsack_dp(values,weights,n_items,capacity)
    print(picks, max_value)

