data = {'1':len('one'), '2':len('two'), '3':len('three'), '4':4, '5':4,
        '6':3, '7':5, '8':5, '9':4, '10':3,
        '11':6, '12':6, '13':8, '14':8, '15':7,
        '16':7, '17':9, '18':8, '19':8, '20':6,
        '30':6, '40':5, '50':5, '60':5,
        '70':7, '80':6, '90':6, '100':len('hundred'), '1000':len('thousand'), '0':0, '00':0}

num = 1000
sum_ = 0
for i in range(1,num+1):
    if str(i) in data.keys():
        if i != 100 and i != 1000:
            sum_ += data[str(i)]
        elif i == 100:
            sum_ += 10
        elif i == 1000:
            sum_ += 11
    elif i < 100:
        n = str(i)
        n0 = n[0]
        n1 = n[1]
        n0 += '0'
        sum_ += (data[n0] + data[n1])
    elif i > 100 and i != 100:
        n = str(i)
        n0 = n[0]
        n1 = n[1]
        n2 = n[2]
        if i % 100 == 0:
            sum_ += (data[n0] + data['100'])
        elif n[1:] in data.keys():
            sum_ += (data[n0] + data['100'] + 3 + data[n[1:]])
        else:
            n1 += '0'
            sum_ += (data[n0] + data['100'] + 3 + data[n1] + data[n2])
    else:
        print(i)

print(sum_)
