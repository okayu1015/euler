coin = [200,100,50,20,10,5,2,1]

def count(num,coin):
    cnt = 0
    if  len(coin) == 1:
        return 1
    else:
        for i in range(num // coin[0]+1):
            cnt += count(num - i * coin[0], coin[1:])
        return cnt
    
print(count(200,coin))
