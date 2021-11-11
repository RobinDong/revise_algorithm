# Find the most average way for partitions
import numpy as np


def maximum_partition(sequence, M, nr_partitions, sum_array):
    for n in range(2, len(sequence) + 1):
        for k in range(2, nr_partitions + 1):
            array = []
            for i in range(1, n + 1):
                select = max(M[i][k - 1], sum_array[n - 1] - sum_array[i - 1])
                array.append(select)
            M[n][k] = min(array)
    return M[len(sequence)][nr_partitions]


def init_matrix(sequence, nr_partitions, M, sum_array):
    for index in range(len(sequence)):
        sum_array.append(sum(sequence[: index + 1]))
    for k in range(1, nr_partitions + 1):
        M[1][k] = sequence[0]
    for n in range(1, len(sequence) + 1):
        M[n][1] = sum(sequence[:n])


if __name__ == "__main__":
    # The sequence and the number of partitions
    sequence = [1, 2, 3, 4, 5, 6]
    partitions = 3
    # init
    M = np.zeros((len(sequence) + 1, partitions + 1), dtype=int)
    sum_array = []
    init_matrix(sequence, partitions, M, sum_array)
    # call the main function
    range_sum_max = maximum_partition(sequence, M, partitions, sum_array)
    print("Sum of the maximum range:", range_sum_max)
    # split the sequence by using maximum sum of one range
    current_sum = 0
    for index in range(len(sequence)):
        if (current_sum + sequence[index]) > range_sum_max:
            print("| ", end="")
            current_sum = 0
        current_sum += sequence[index]
        print(sequence[index], end=" ")
    print("\r")
