num = [i for i in range(1,10)]
ans = []
cnt = 0    
for i in range(1234,10000):
    for j in range(12,100):
        k = int(i / j)
        if i == k * j:
            s = ''
            s += str(i)
            s += str(j)
            s += str(k)
            n = []
            if len(s) == 9:
                for l in range(len(s)):
                    n.append(int(s[l]))
                n.sort()
                if n == num and i not in ans:
                    cnt += 1
                    ans.append(i)
                
for i in range(1234,10000):
    for j in range(1,10):
        k = int(i / j)
        if i == k * j:
            s = ''
            s += str(i)
            s += str(j)
            s += str(k)
            n = []
            if len(s) == 9:
                for l in range(len(s)):
                    n.append(int(s[l]))
                n.sort()
                if n == num and i not in ans:
                    cnt += 1
                    ans.append(i)

print(cnt)
print(ans)
n = 0
for i in range(len(ans)):
    n += int(ans[i])
print(n)
