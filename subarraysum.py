a = [2,-2,1,3,4,-7,-1,6,-2,3,6,80]
n=len(a)

def maxsum(a,n):
    mlen=0
    i=0
    while i < n:
        sum = 0
        j=i
        while j < n:
            sum = sum + a[j]
            if sum == 0:
                #mlen = max(mlen,j-i+1)
                mlen = j-i+1
            j = j+1
        i= i+1
        return mlen

max_len = maxsum(a,n)
print max_len
