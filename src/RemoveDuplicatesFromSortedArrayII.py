# General solution for at most k duplicates kept:
#
# int removeDuplicates(int A[], int n, int k) {
#    if (n <= k) return n;       // no need to deal with n<=k case.
#    int len = k, itor = k;
#    while (itor < n) {
#        if (A[itor] != A[len-k]) 
#            A[len++] = A[itor];
#        itor++;
#    }
#    return len;
#}
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        index = 0
        pre = None
        hasTwo = False
        for num in A:
            if num == pre and hasTwo:
                continue
            if num == pre:
                hasTwo = True
            else:
                hasTwo = False
                pre = num
            A[index] = num
            index += 1
        return index