"""
You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.

"""
#Solution : Single Scan 
"""
Further, the two points being considered for the distance calculation should not both belong to the same array. Thus, for arrays aaa and bbb currently chosen, we can just find the maximum out of a[n−1]−b[0] and b[m−1]−a[0] to find the larger distance. Here, nnn and mmm refer to the lengths of arrays aaa and bbb respectively.
For every new array, a considered, we find the distance a[n−1]−min_val and max_val−a[0] to compete with the maximum distance found so far. Here, nnn refers to the number of elements in the current array, aaa. Further, we need to note that the maximum distance found till now needs not always be contributed by the end points of the distance being max_val and min_val.
"""
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        #init res and values
        res = 0
        n = len(arrays[0])
        min_val = arrays[0][0]
        max_val = arrays[0][n-1]

        for i in range(1,len(arrays)):
            #get len array i_th
            n = len(arrays[i])
            res = max(res, max(abs(arrays[i][n-1] - min_val), 
                               abs(max_val - arrays[i][0])))
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][n-1])
        
        return res