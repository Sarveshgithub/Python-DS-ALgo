# Block swap algorithm for array rotation
def rotate(arr, d):
    return arr[d:] + arr[:d]


arr = [1, 2, 3, 4, 5, 6, 7]
d = 4


def blockSwap(arr, d, size):
    A = d
    B = size - d
    while A != B:
        if A < B:
            swap(arr, A, B)
            B -= A
        if A > B:
            swap(arr, B, A)
            A -= B
    swap(arr, A, B)


def swap(arr, A, B):
    arr[0:A], arr[B : B + A] = arr[B : B + A], arr[0:A]
    print(arr, A, B)


blockSwap(arr, d, len(arr))

