def has_prefix(word, prefix):
    if word.startswith(prefix):
        return True


prefix = input()
words = input().split()

for word in words:
    if has_prefix(word, prefix):
        print(word)