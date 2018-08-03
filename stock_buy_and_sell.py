def find(a,n):
    c=0
    p=False
    for i in range(n-1):
        start=c
        if i==n-1-1:
            ends=n-1
        if a[i+1]<a[i]:
            c=i+1
            ends=i
            if start!=ends:
                p=True
                print("(",str(start),sep="",end=" ")
                print(ends,sep="",end="")
                print(")",end=" ")
    # if start!=ends:
    #     p=True
    #     print("(",end="")
    #     print(start,ends,end="")
    #     print(")")
    #     return
    if not p:
        print("No Profit")
    else:
        print("")
z=int(input())
for _ in range(z):
    n=int(input())
    a=list(map(int,input().split()))
    find(a,n)


# def find(a,n):
#     c=0
#     p=False
#     for i in range(n-1):
#         start=c
#         if i==n-1-1:
#             ends=n-1
#         if a[i+1]<a[i]:
#             c=i+1
#             ends=i
#             if start!=ends:
#                 p=True
#                 print("(",str(start),sep="",end=" ")
#                 print(ends,sep="",end="")
#                 print(")",end=" ")
#     if start!=ends:
#         p=True
#         print("(",end="")
#         print(start,ends,end="")
#         print(")")
#         return
#     if not p:
#         print("No Profit")
    
            
    
# z=int(input())
# for _ in range(z):
#     n=int(input())
#     a=list(map(int,input().split()))
#     find(a,n)