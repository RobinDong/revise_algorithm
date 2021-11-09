# Max increasing number sequence


def max_increase_numbers(sequence):
    seq_len = len(sequence)
    max_lengths = [1] * seq_len

    if seq_len <= 1:
        return sequence[seq_len - 1]

    for i in range(1, seq_len):
        # find all S(j) that S(j) < S(i)
        max_l = 0
        for j in range(i):
            if sequence[j] < sequence[i] and max_lengths[j] > max_l:
                max_l = max_lengths[j]
        max_lengths[i] = max_l + 1
        if max_lengths[i] > max_lengths[i - 1]:
            print(sequence[j])

    result = max(max_lengths)
    # Find which item has the max length
    for index in range(seq_len):
        if max_lengths[index] == result:
            print(sequence[index])
    return max(max_lengths)


if __name__ == "__main__":
    print("Max increasing numbers: ", max_increase_numbers("932846751"))
