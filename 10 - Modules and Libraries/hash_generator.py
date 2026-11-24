from hashlib import md5

text = input()

hashed = md5(text.encode("utf-8"))

print(hashed.hexdigest())
