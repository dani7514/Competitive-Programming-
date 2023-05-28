#User function Template for python3

class Solution: 
    def select(self, arr, k):
        for i in range(0,k-1):
            minIndex=i
            for j in range(i+1,k):
               if arr[j]<arr[minIndex]:
                   minIndex=j
            if minIndex != i:
                arr[i],arr[minIndex]=arr[minIndex],arr[i]
        return arr
    
    def selectionSort(self, arr,n):
        return self.select(arr,n)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends