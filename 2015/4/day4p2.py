from hashlib import md5

key = open('input2.txt').read().strip()
num = 1
while True:
    text = key + str(num)
    H = md5(text.encode()).hexdigest()
    if H.startswith('000000'):
        break
    num += 1

print(num)