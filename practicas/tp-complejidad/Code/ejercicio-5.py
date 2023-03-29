# Implementar un algoritmo Contiene-Suma(A,n) que recibe una lista de enteros A y un entero n y
# devuelve True si existen en A un par de elementos que sumados den n. Analice el costo computacional: O(nlogn).

def ContieneSuma(A, n):
    try:
        nIndex = A.index(n)
    except:
        print("The value given is not in the Array")
    # We create an array for the numbers that have been checked already
    checked = []
    for num in A:
        # We checked if the complemento of n, is already in the checked array
        if n - num in checked:
            return True
        checked.append(num)
    return False
