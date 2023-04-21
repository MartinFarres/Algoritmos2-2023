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
    return


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


def printHT(D):
    for i in range(len(D.slots)):
        if D.slots[i] == None:
            print("||", i, "|| ---> ", D.slots[i], end=" ")
        else:
            print("||", i, "|| ---> ",
                  [f"{i.key}, {i.value[0]}, {i.value[1]}" for i in D.slots[i]], end=" ")
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
# Ejercicio 1 & 2


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
    print(search(dic, 20))


# Ejercicio 4
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


testEj7()
