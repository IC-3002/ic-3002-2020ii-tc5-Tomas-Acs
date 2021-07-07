def burbuja(A):
    n = len(A)
    for i in range(1, n):
        for j in range(0, n - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)

def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp




def burbuja_optimizado(A):
	for i in range(len(A)):
		cambios = True
		for j in range(len(A)-1):
			if A[j] > A[j+1]:
				temp = A[j]
				A[j] = A[j+1]
				A[j+1] = temp
				cambios = False
		if cambios:
			return A
	return A
			
