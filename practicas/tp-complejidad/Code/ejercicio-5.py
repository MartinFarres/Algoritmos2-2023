def ContieneSuma(A, n):
    for i in range(0, len(A)):
        if A[i] > n:
            A.pop(i)
