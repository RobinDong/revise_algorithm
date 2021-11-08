# Get minimum edit distance for two strings

# Cost for match/substitute/insert/delete
MATCH = 0
SUBSTITUTE = 1
INSERT = 1
DELETE = 1


def edit_distance(source, target, i, j, memory):
    if (i, j) in memory:
        return memory[(i, j)]

    if i == -1:
        return (j + 1) * INSERT
    if j == -1:
        return (i + 1) * DELETE

    if source[i] == target[j]:
        dist = edit_distance(source, target, i - 1, j - 1, memory) + MATCH
        memory[(i, j)] = dist
        return dist

    sub_cost = edit_distance(source, target, i - 1, j - 1, memory) + SUBSTITUTE
    insert_cost = edit_distance(source, target, i, j - 1, memory) + INSERT
    del_cost = edit_distance(source, target, i - 1, j, memory) + DELETE

    min_cost = min(sub_cost, insert_cost, del_cost)
    memory[(i, j)] = min_cost
    return min_cost


if __name__ == "__main__":
    print("Edit distance: ", edit_distance("abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyza", 25, 25, {}))
