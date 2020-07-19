from copy import deepcopy

def contains_upto_permutations(text, pattern):
    p_list = list(pattern)
    # print(len(text) - len(pattern) + 1)
    for i in range(len(text) - len(pattern) + 1):
        print(i)
        found = True

        cp_list = deepcopy(p_list)
        # print(cp_list)
        for j in range(len(pattern)):

            if text[i + j] not in pattern:
                found = False
                break
            else:
                cp_list.remove(text[i + j])

        if found and cp_list == []:
            return True
    return False

text = input()
pattern = input()

print(contains_upto_permutations(text, pattern))
