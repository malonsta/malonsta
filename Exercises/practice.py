message = 'I LOVE GOD UNCONDITIONALLY'

count = {}

for characters in message:
    count.setdefault(characters, 0)
    count[characters] = count[characters] + 1


print(count)
