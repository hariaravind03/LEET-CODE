#User function Template for python3

class Solution:
    def median(self, matrix, R, C):
    	#code here
    	a=[]
    	for i in range(R):
    	    for j in range(C):
    	        a.append(matrix[i][j])
    	
    	a.sort()
    	
    	if len(a)%2!=0:
    	    return a[len(a)//2]
    	else:
    	    return (a[len(a)//2]+a[(len(a)//2)-1])//2
    	        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t=[int(el) for el in input().split()]
            for j in range(c):
                matrix[i][j]=t[j]
        ans = ob.median(matrix, r, c);
        print(ans)
        print("~")
# } Driver Code Ends