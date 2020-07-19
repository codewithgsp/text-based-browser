text = input()
pattern = input()

def find_last(text, pattern):
    index = text.rfind(pattern)
    print(index)

find_last(text, pattern)
