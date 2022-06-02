class CountingElements:
    def FrogRiverOne(x, a):
        """
        A small frog wants to get to the other side of a river. The frog is
        initially located on one bank of the river (position 0) and wants to get
        to the opposite bank (position X+1). Leaves fall from a tree onto the
        surface of the river.
        You are given an array A consisting of N integers representing the falling
        leaves. A[K] represents the position where one leaf falls at time K,
        measured in seconds. The goal is to find the earliest time when the frog
        can jump to the other side of the river. The frog can cross only when
        leaves appear at every position across the river from 1 to X (that is, we
        want to find the earliest moment when all the positions from 1 to X are
        covered by leaves). You may assume that the speed of the current in the
        river is negligibly small, i.e. the leaves do not change their positions
        once they fall in the river.
        For example, you are given integer X = 5 and array A such that:

          A[0] = 1
          A[1] = 3
          A[2] = 1
          A[3] = 4
          A[4] = 2
          A[5] = 3
          A[6] = 5
          A[7] = 4
        In second 6, a leaf falls into position 5. This is the earliest time when
        leaves appear in every position across the river.
        given a non-empty array A consisting of N integers and integer X, returns
        the earliest time when the frog can jump to the other side of the river.
        If the frog is never able to jump to the other side of the river, the
        function should return −1.

        For example, given X = 5 and array A such that:

          A[0] = 1
          A[1] = 3
          A[2] = 1
          A[3] = 4
          A[4] = 2
          A[5] = 3
          A[6] = 5
          A[7] = 4
        the function should return 6, as explained above.
            :return:
        """
        pass

    def PermCheck(self, A):
        """
        A non-empty array A consisting of N integers is given.
        A permutation is a sequence containing each element from 1 to N once, and
        only once. For example, array A such that:
        A[0] = 4
        A[1] = 1
        A[2] = 3
        A[3] = 2
        is a permutation, but array A such that:
        A[0] = 4
        A[1] = 1
        A[2] = 3
        is not a permutation, because value 2 is missing.
        The goal is to check whether array A is a permutation.
        given an array A, returns 1 if array A is a permutation and 0 if it is not
        For example, given array A such that:
            A[0] = 4
            A[1] = 1
            A[2] = 3
            A[3] = 2
        the function should return 1.
        Given array A such that:
            A[0] = 4
            A[1] = 1
            A[2] = 3
        the function should return 0.
        Write an efficient algorithm for the following assumptions:
        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [1..1,000,000,000].
        :return:
        """
        A.sort()
        if A[0] != 1:
            return 0
        elif A[-1] != len(A):
            return 0
        else:
            return 1 if A == list(range(1, len(A) + 1)) else 0

    def MaxCounters(self, N, A):
        """
        You are given N counters, initially set to 0, and you have two possible
        operations on them:
        increase(X) − counter X is increased by 1,
        max counter − all counters are set to the maximum value of any counter.
        A non-empty array A of M integers is given. This array represents
        consecutive operations:
        if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
        if A[K] = N + 1 then operation K is max counter.
        For example, given integer N = 5 and array A such that:
            A[0] = 3
            A[1] = 4
            A[2] = 4
            A[3] = 6
            A[4] = 1
            A[5] = 4
            A[6] = 4
        the values of the counters after each consecutive operation will be:
            (0, 0, 1, 0, 0)
            (0, 0, 1, 1, 0)
            (0, 0, 1, 2, 0)
            (2, 2, 2, 2, 2)
            (3, 2, 2, 2, 2)
            (3, 2, 2, 3, 2)
            (3, 2, 2, 4, 2)
        The goal is to calculate the value of every counter after all operations.
        given an integer N and a non-empty array A consisting of M integers,
        returns a sequence of integers representing the values of the counters.
        Result array should be returned as an array of integers.
        For example, given:
            A[0] = 3
            A[1] = 4
            A[2] = 4
            A[3] = 6
            A[4] = 1
            A[5] = 4
            A[6] = 4
        the function should return [3, 2, 2, 4, 2], as explained above.
        Write an efficient algorithm for the following assumptions:
        N and M are integers within the range [1..100,000];
        each element of array A is an integer within the range [1..N + 1].
        :return:
        """
        # output = [0] * N
        # print(output)
        # for i in A:
        #     if i <= N:
        #         output[i - 1] = output[i - 1] + 1
        #     else:
        #         output = [max(output)] * N
        # return output
        res = [0] * N
        max_val = 0
        last_update = 0
        n1 = N + 1
        for i in A:
            if i < n1:
                if res[i - 1] < last_update:
                    res[i - 1] = last_update

                res[i - 1] += 1

                if res[i - 1] > max_val:
                    max_val = res[i - 1]
            else:
                last_update = max_val

        for i in range(len(res)):
            if res[i] < last_update:
                res[i] = last_update

        return res

    def MissingInteger(self, A):
        """
        given an array A of N integers, returns the smallest positive integer
        (greater than 0) that does not occur in A.
        For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
        Given A = [1, 2, 3], the function should return 4. Given A = [−1, −3], the
        function should return 1. Write an efficient algorithm for the following
        assumptions: N is an integer within the range [1..100,000]; each element
        of array A is an integer within the range [−1,000,000..1,000,000].
        :return:
        """
        if max(A) < 1:
            return 1
        elif len(A) == 1:
            return 2 if A[0] == 1 else A[0] - 1
        elif set(A) == {i for i in range(1, len(A) + 1)}:
            return max(A) + 1
        else:
            return list({i for i in range(min(A), len(A))} - set(A))[0]


counting = CountingElements()
print(f"PermCheck: {counting.PermCheck([9, 5, 7, 3, 2, 7, 3, 1, 10, 8])}")
print(f"MaxCounters: {counting.MaxCounters(1, [1])}")
# print(counting.MissingInteger([2, 10]))
