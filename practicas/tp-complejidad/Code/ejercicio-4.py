# Implementar un algoritmo que ordene una lista de elementos donde siempre el elemento del
# medio de la lista contiene antes que él en la lista la mitad de los elementos menores que él.
# Explique la estrategia de ordenación utilizada.

def halfsort(A):
    midIndex = len(A)//2
    n = 0
    # Is the Middle element capable of having //2 elements to the left or at least one element
    while A[midIndex] // 2 > len(A) // 2:
        if n == len(A):
            return False
        # Moves All elements to the right by one
        A = [A[-1]] + A[:-1]
        n += 1
    valuesSTM = 0  # Values Smaller Than Mid
    listBTM = []  # Index Values Bigger than Mid
    for i in range(0, midIndex):
        if A[i] < A[midIndex]:
            valuesSTM += 1
        else:
            listBTM.append(i)
    i = midIndex + 1
    while valuesSTM < A[midIndex] // 2:
        if A[i] < A[midIndex]:
            smallValue = A[i]
            indexToMove = listBTM[len(listBTM)-1]
            A[i] = A[indexToMove]
            A[indexToMove] = smallValue
            listBTM.pop()
            valuesSTM += 1
        i += 1
    if valuesSTM < A[midIndex] // 2:
        return False
    return A
