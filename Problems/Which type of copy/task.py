import copy

obj = [[1, 2], [3, 4]]

def detect_copy():
    copy_obj = copying_machine(obj)
    if id(copy_obj[1]) == id(obj[1]):
        return "shallow copy"
    return "deep copy"
