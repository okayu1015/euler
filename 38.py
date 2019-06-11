num = [1,2,3,4,5,6,7,8,9]

for i in range(1,333):
    s = ''
    l = []
    s += str(i) + str(i*2) + str(i*3)
    for j in range(len(s)):
        l.append(int(s[j]))
    l.sort()
    if num == l:
        print(l)
        print(s)
        print(i)
