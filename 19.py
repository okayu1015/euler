data = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
data_w = [i for i in range(1,7+1)]
# 月:1 - 日:7
cnt = 0
cnt_sunday = 0
week = 0
for i in range(1901,2000+1):
    for j in range(1,13):
        if i % 4 == 0 and (i % 400 == 0 and i % 100 != 0) and j == 2:
            day = data[j] + 1
        else:
            day = data[j]
        for k in range(1,day+1):
            cnt += 1
            week = data_w[cnt % 7]
            if week == 7 and k == 1:
                cnt_sunday += 1
                
print(week)
print(cnt_sunday)
