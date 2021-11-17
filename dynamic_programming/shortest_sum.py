# Find the shortest sub-sequence for the target SUM


def shortest_sum(target_sum, array, mem):
    if target_sum in mem:
        return mem[target_sum]

    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    shortest_arr = None
    for item in array:
        remain = target_sum - item
        result = shortest_sum(remain, array, mem)
        if result is None:
            continue
        result = result + [item]
        if shortest_arr is None or len(shortest_arr) > len(result):
            shortest_arr = result

    mem[target_sum] = shortest_arr
    return shortest_arr


if __name__ == "__main__":
    print(shortest_sum(20, [2, 3, 5, 7], {}))
    print(shortest_sum(30, [2, 3, 5, 7], {}))
    print(shortest_sum(50, [2, 3, 5, 7], {}))
    print(shortest_sum(500, [2, 3, 5, 7], {}))
