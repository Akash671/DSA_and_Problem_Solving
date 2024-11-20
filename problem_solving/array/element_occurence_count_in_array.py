class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        #from collections import Counter
        #counts = Counter(arr)
        n=len(arr)
        
        tmp=[]
        for i in arr:
            if i not in tmp:
                tmp.append(i)
        #print(tmp)
        occur = {element: 0 for element in tmp}
        #print(occur)
        for i in arr:
            occur[i]+=1
        #print(occur)
        #n=len(arr)
        ans=[]
        for i in tmp:
            if occur[i]>n//3:
                ans.append(i)
        return sorted(ans)

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends
