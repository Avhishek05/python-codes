def max_len(a):
    maxl=0
    curr_sum=0
    hash_map = {}
    for i in range(len(a)):
        curr_sum+=a[i]
        if a[i] is 0 and maxl is 0:
            return 0
        if curr_sum is 0:
            maxl+=1
        if curr_sum in hash_map:
            maxl = max(maxl,i-hash_map[curr_sum])
        else :
            hash_map[curr_sum] = i
    return maxl
a=[15,2,-2,-8,1,7,10,13]
mlen = max_len(a)
print mlen
#we will store sum in hash table if sum repeat means sum b'n them is 0 so i-(where same sum is store).i is current index
