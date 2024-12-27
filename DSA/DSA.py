# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 12:19:01 2024

@author: akash
"""




import math


class Solution:
    
    
    #Count pairs is sum is equal to target
    def countPairs(self,arr, target):
       ans=0
       d={}
       for i,A in enumerate(arr):
           B=target-A 
           """
           target=A+B
           now we need to check B is in arr or not if its then pair exits 
    
           if B in arr:
               ans+=1
           
           """
           if B in d:
               ans+=d[B]
           if A in d:
               d[A]+=1
           else:
               d[A]=1
           
       return ans
       
       


 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()


