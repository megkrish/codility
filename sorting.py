class Sorting:
    def Distinct(self, A):
        """
        given an array A consisting of N integers, returns the number of
        distinct values in array A. For example, given array A consisting of
        six elements such that:
             A[0] = 2    A[1] = 1    A[2] = 1
             A[3] = 2    A[4] = 3    A[5] = 1
        the function should return 3, because there are 3 distinct values
        appearing in array A, namely 1, 2 and 3.
        Write an efficient algorithm for the following assumptions:
        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range
        [−1,000,000..1,000,000].
        :return:
        """
        return len(set(A))

    def MaxProductOfThree(self, A):
        """
        A non-empty array A consisting of N integers is given. The product of
        triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).
        For example, array A such that:
          A[0] = -3
          A[1] = 1
          A[2] = 2
          A[3] = -2
          A[4] = 5
          A[5] = 6
        contains the following example triplets:
        (0, 1, 2), product is −3 * 1 * 2 = −6
        (1, 2, 4), product is 1 * 2 * 5 = 10
        (2, 4, 5), product is 2 * 5 * 6 = 60
        Your goal is to find the maximal product of any triplet.
        given a non-empty array A, returns the value of the maximal product
        of any triplet.
        Write an efficient algorithm for the following assumptions:
        N is an integer within the range [3..100,000];
        each element of array A is an integer within the range [−1,000..1,000].
        :return:
        """
        # import functools
        # first_3_1 = functools.reduce((lambda x, y: x * y), A[:3])
        # last_3_1 = functools.reduce((lambda x, y: x * y), A[-3:])
        # A.sort()
        # first_3_2 = functools.reduce((lambda x, y: x * y), A[:3])
        # last_3_2 = functools.reduce((lambda x, y: x * y), A[-3:])
        # return max(first_3_1, first_3_2, last_3_1, last_3_2)
        if len(A) < 3:
            raise Exception("Invalid input")
        A.sort()
        return max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])

    def Triangle(self, A):
        """
        An array A consisting of N integers is given. A triplet (P, Q, R) is
        triangular if 0 ≤ P < Q < R < N and:
            A[P] + A[Q] > A[R],
            A[Q] + A[R] > A[P],
            A[R] + A[P] > A[Q].
        For example, consider array A such that:
            A[0] = 10    A[1] = 2    A[2] = 5
            A[3] = 1     A[4] = 8    A[5] = 20
        Triplet (0, 2, 4) is triangular.
        given an array A consisting of N integers, returns 1 if there exists a
        triangular triplet for this array and returns 0 otherwise.
        For example, given array A such that:
            A[0] = 10    A[1] = 2    A[2] = 5
            A[3] = 1     A[4] = 8    A[5] = 20
        the function should return 1, as explained above. Given array A such
        that:
            A[0] = 10    A[1] = 50    A[2] = 5
            A[3] = 1
        the function should return 0.
        Write an efficient algorithm for the following assumptions:
        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range
         [−2,147,483,648..2,147,483,647].
        :return:
        """
        A.sort()
        output = 0
        for i in range(len(A) - 3):
            if A[i] + A[i + 1] > A[i + 3]:
                return 1
        return 0


sorting = Sorting()
# print(f"Distinct: {sorting.Distinct([2, 1, 1, 2, 3, 1])}")
# print(f"MaxProductOfThree: {sorting.MaxProductOfThree([-4, -6, 3, 4, 5])}")
print(f"Triangle: {sorting.Triangle([10, 2, 5, 1, 8, 20])}")
