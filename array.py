def CyclicRotation(A, K):
    """
    CyclicRotation:
    An array A consisting of N integers is given. Rotation of the array means
    that each element is shifted right by one index, and the last element of
    the array is moved to the first place. For example, the rotation of array
    A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one
    index and 6 is moved to the first place).
    The goal is to rotate array A K times; that is, each element of A will be
    shifted to the right K times.
    :return:
    """
    if K == len(A) or A == []:
        return A
    else:
        for _ in range(K):
            A.insert(0, A.pop())
        return A


# print(CyclicRotation([], 5))


def solution(A):
    """
    A non-empty array A consisting of N integers is given. The array contains
    an odd number of elements, and each element of the array can be paired
    with another element that has the same value, except for one element
    that is left unpaired.
    For example, in array A such that:
      A[0] = 9  A[1] = 3  A[2] = 9
      A[3] = 3  A[4] = 9  A[5] = 7
      A[6] = 9
    the elements at indexes 0 and 2 have value 9,
    the elements at indexes 1 and 3 have value 3,
    the elements at indexes 4 and 6 have value 9,
    the element at index 5 has value 7 and is unpaired.
    :return:
    that, given an array A consisting of N integers fulfilling the above
    conditions, returns the value of the unpaired element.
    """
    s = set(A)
    for i in s:
        print(A)
        if A.count(i) == 1:
            return i
        elif A.count(i) > 1:
            A = list(filter(lambda a: a != i, A))
            continue
    # 100% other's sol
    # s = set()
    # for v in t:
    #     s.add(v) if v not in s else s.remove(v)
    # return list(s)


print(solution([9, 3, 9, 3, 9, 7, 9]))
