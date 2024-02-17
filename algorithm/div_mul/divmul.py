def div_mul(x,n:int )->int:
    if n==0:
        return 1
    return div_mul(x*x,n//2) if n%2==0 else div_mul(x*x,n//2)*x
def matrix_mul(l1,l2):
    n=len(l1)
    l3=[[l1[i][j]*l2[j][i] for j in range(n)] for i in range(n)]
    return l3        
# print(div_mul(22,41))
print(matrix_mul([[1,1],[1,0]],[[1,1],[1,0]]))