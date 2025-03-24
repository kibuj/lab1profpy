def sort_list(lst):
    return sorted(lst)

def find_element(lst, value):
    return lst.index(value) if value in lst else -1

def find_subsequence(lst, sub):
    sub_len = len(sub)
    for i in range(len(lst) - sub_len + 1):
        if lst[i:i + sub_len] == sub:
            return i
    return -1

def find_min_five(lst):
    return sorted(lst)[:5]

def find_max_five(lst):
    return sorted(lst, reverse=True)[:5]

def calculate_average(lst):
    return sum(lst) / len(lst)

def remove_duplicates(lst):
    seen = set()
    for x in lst:
        if x not in seen:
            seen.add(x)
    return seen
