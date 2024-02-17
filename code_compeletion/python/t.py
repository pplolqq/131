def c(n,m):
    a=mul(n)
    b=mul(m)
    c=mul(n-m)
    return a//(b*c)
def mul(m):
    r=1
    for i in range(1,m+1):
        r*=i
    return r
k=2
n=1
# n1=c(2**k-1,n-1)*mul(n)*mul(n+1)*c(2**k-n,2)
# print(n1)
# n2=c(2**k-1,n)*mul(n)*mul(n+1)
# print(n1+n2)
