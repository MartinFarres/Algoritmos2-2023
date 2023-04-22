class Dictionary:
    slots = None

    def __init__(self, length, hashF, *args, **kwargs):
        self.slots = [[] for i in range(length)]
        self.hashF = hashF
        self.args = args
        self.kwargs = kwargs

    def hashF(self):
        return self.hashF(*self.args, **self.hashF)


class DictionaryItem:
    key = None
    value = None

    def __init__(self, key, value):
        self.key = key
        self.value = value


def insert(D, key, value):
    item = DictionaryItem(key, value)
    slotIndex = D.hashF(key, len(D.slots))
    if (D.slots[slotIndex] == None):
        D.slots[slotIndex] = []
    slotList = D.slots[slotIndex]
    slotList.append(item)


def search(D, key):
    slotIndex = D.hashF(key, len(D.slots))
    keyList = D.slots[slotIndex]
    for i in keyList:
        if i.key == key:
            return i.key
    return False


def delete(D, key):
    slotIndex = D.hashF(key, len(D.slots))
    keyList = D.slots[slotIndex]
    for i in keyList:
        if i.key == key:
            i.key = None
            i.value = None
    return D


def isPermutationSTR(S, P):
    if len(S) != len(P):
        return False
    dicS = Dictionary(26, hashFAscii)
    dicP = Dictionary(26, hashFAscii)
    for i in range(0, len(S)):
        insert(dicS, S[i], S[i])
        insert(dicP, P[i], P[i])
    for i in range(0, len(dicS.slots)):
        if len(dicS.slots[i]) != len(dicP.slots[i]):
            return False
    return True


def uniqueKeys(arr):
    D = Dictionary(len(arr), hashFMod)
    for i in arr:
        res = search(D, i)
        insert(D, i, i)
        if res != None:
            return True
    return False


def strCompression(S):
    S.lower()
    D = Dictionary(26, hashFAscii)
    k = S[0]
    count = 0
    j = 0
    for i in range(0, len(S)):
        if S[i] != k or i == len(S)-1:
            insert(D, S[i-1], (j, count))
            k = S[i]
            count = 1
            j += 1
        else:
            count += 1
    res = [None] * (j)
    for i in D.slots:
        if i != []:
            for n in i:
                res[n.value[0]] = f"{n.key}{n.value[1]}"
    res = "".join(res)
    if len(res) < len(S):
        return res
    return S


# Rabin-Karp Algorythm
# Complejidad Temporal es de O(m*n) en el peor caso y de O(m+n) en el caso promedio
# d = len(conjunto) Ej: d=26 en el conjunto de abecedario
def patterMatching(pattern, text, d):
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0

    # Calculate hash value for pattern and first text itter of len n
    for i in range(m):
        p = (d*p + hashFAscii(pattern[i], 0)) % 13
        t = (d*t + hashFAscii(text[i], 0)) % 13

    # Finding the match
    matched = True
    for i in range(n-m+1):
        if p == t:  # Same hash values
            for j in range(m):
                if text[i+j] != pattern[j]:
                    matched = False
            if matched:
                return i + 1
        if i < n-m:  # Recalculate Hash value for next text itter
            for j in range(m):
                t = (d*t + hashFAscii(text[j+i], 0)) % 13
    return False


def isSubset(subSet, t):
    dic = Dictionary(nearest_prime(len(t)), hashFMod)
    for i in t:
        insert(dic, i, i)
    for i in subSet:
        if search(dic, i) == False:
            return False
    return True


def nearest_prime(n):
    if n <= 1:
        return 2
    for i in range(n, 2*n):
        if all(i % j != 0 for j in range(2, int(i**0.5)+1)):
            return i


def printHT(D):
    for i in range(len(D.slots)):
        if D.slots[i] == None:
            print("||", i, "|| ---> ", D.slots[i], end=" ")
        else:
            print("||", i, "|| ---> ", [i.key for i in D.slots[i]], end=" ")
        print("")


# ---------------------------------------------------Hash Functions---------------------------------


def hashFMod(k, m):
    return k % m


def hashFAscii(k, m):
    return ord(k)-97


def hashFPostalCode(k, m):
    k0 = 0
    for i in k:
        if isinstance(i, int) == True:
            k0 = k0 + i
        else:
            k0 = k0 + ord(i)
    return (k0 % m)


# --------------------------------------------------Test--------------------------------------------

def testEj1_2():
    dic = Dictionary(9, hashFMod)
    insert(dic, 5, 5)
    insert(dic, 28, 28)
    insert(dic, 20, 20)
    insert(dic, 19, 19)
    insert(dic, 15, 15)
    insert(dic, 33, 33)
    insert(dic, 12, 12)
    insert(dic, 17, 17)
    insert(dic, 10, 10)
    printHT(dic)
    print(search(dic, 20))


def testEj4():
    s = "hola"
    p = "ohla"
    print(isPermutationSTR(s, p))


def testEj5():
    a = [1, 5, 12, 1, 2]
    print(uniqueKeys(a))


def testEj7():
    s = "aabcccccaaa"
    print(strCompression(s))


def testEj8():
    text = "ABCCDDAEFG"
    pattern = "CDD"
    print(patterMatching(pattern, text))


def testEj9():
    t = [5, 8, 3, 9, 1, 2]
    subset = [5, 3, 2]
    print(t, subset)
    print(isSubset(subset, t))
    t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    subset = [5, 3, 12]
    print(t, subset)
    print(isSubset(subset, t))


testEj1_2()
