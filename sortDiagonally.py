def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        z=min(m,n)
        for _ in range(z):
            for i in range(m):
                for j in range(n):
                    if i+1<m and j+1<n:
                        if mat[i+1][j+1]<mat[i][j]:
                            mat[i+1][j+1],mat[i][j]=mat[i][j],mat[i+1][j+1]
        return mat
