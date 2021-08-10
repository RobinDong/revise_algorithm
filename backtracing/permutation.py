# print out all permutations of word "abc"
word = ["a", "b", "c"]
max_len = 3

def construct_candidates(problem, k) -> list:
    if k <= 0:
        return word
    else:
        word_set = set(word)
        for index in range(k):
            word_set.remove(problem[index])
        return list(word_set)

def is_solution(problem, k):
    return k == max_len

def construct_solution(problem, candidate):
    return problem + candidate

def solve(problem, k):
    if is_solution(problem, k):
        print("solution:", problem)
    else:
        candidates = construct_candidates(problem, k)
        k += 1
        for candidate in candidates:
            new_problem = construct_solution(problem, candidate)
            solve(new_problem, k)

solve("", 0);
