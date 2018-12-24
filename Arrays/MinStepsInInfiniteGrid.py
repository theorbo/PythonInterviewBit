class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return an integer
	def coverPoints(self, A, B):
	    startX = A[0]
	    startY = B[0]
	    ans = 0
	    
	    i=1
	    length = len(A)
	    
	    for i in range(1,len(A)):
	        diffX = abs(A[i]-startX)
	        diffY = abs(B[i]-startY)
	        ans += max(diffX, diffY)
	        startX = A[i]
	        startY = B[i]
	        
        return ans
	    
	    
