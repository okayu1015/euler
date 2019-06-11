s = 1000000 
max_cnt = 0
max_s = 0
cnt = 0
for s in range(13,999999,2):
    tmp = s
    cnt = 0
    while s != 1:
        if s % 2 == 0:
            s = s/2
        else:
            s = 3*s + 1
            cnt += 1
    if max_cnt < cnt + 1:
        max_cnt += (cnt+1)
        max_s = tmp
print(max_cnt)
print(max_s)

while max_s < 1000000:
    max_s *=2
print(max_s)
