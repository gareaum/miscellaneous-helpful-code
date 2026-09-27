def leftchild(H, i):
    lc = (2 * i) + 1
    return lc

def rightchild(H, i):
    rc = (2 * i) + 2
    return rc

def parent(H, i):
    if i == 0:
        return 0

    p = (i - 1) // 2
    return p

def sift_up(H):
    position = len(H) - 1

    while (position != 0) and (H[parent(H, position)] > H[position]):
        H[parent(H, position)], H[position] = H[position], H[parent(H, position)]
        position = parent(H, position)

def sift_down(H, position):
    size = len(H)

    while True:
        LC = leftchild(H, position)
        RC = rightchild(H, position)

        if LC >= size:
            break

        if RC >= size:
            if H[LC] < H[position]:
                H[LC], H[position] = H[position], H[LC]
                position = LC
            else:
                break

        else:
            smaller = LC if H[LC] < H[RC] else RC

            if H[smaller] < H[position]:
                H[smaller], H[position] = H[position], H[smaller]
                position = smaller
            else:
                break

def insert(H, value):
    H.append(value)
    sift_up(H)

def extract(H):
    H[0], H[-1] = H[-1], H[0]
    H.pop()
    sift_down(H, 0)

def Heapify(H):
    size = len(H)

    for i in range(size // 2 - 1, -1, -1):
        sift_down(H, i)

def heap_sort(H):
    Heapify(H)
    size = len(H)

    while size > 0:
        H[0], H[size - 1] = H[size - 1], H[0]
        size -= 1

        if size == 0:
            break

        SH = H[:size]
        Heapify(SH)

        for j in range(size):
            H[j] = SH[j]

    H.reverse()