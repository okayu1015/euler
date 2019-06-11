cir_list = []
def binary(i):
    s = ''
    while i >= 1:
        if i == 1:
            s = str(i) + s
            break
        else:
            s = str(i % 2) + s
            i = int(i / 2)
    return s

for i in range(1,10):
    print(binary(i))

for i in range(1,1000000,2):
    s = str(i)
    if s == s[::-1]:
        cir_list.append(i)
sum = 0
print(cir_list)
for i in cir_list:
    s = str(binary(i))
    if s == s[::-1]:
        sum += int(i)
print(sum)
