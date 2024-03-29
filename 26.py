def cycle(n):
    while n % 2 == 0:
        n /= 2
    while n % 5 == 0:
        n /= 5
    if n == 1:
        return 0
    count = 1
    while 10**count % n != 1:
        count += 1
    return count

print(cycle(7))

'''
循環小数の秘密というサイトによると，既約分数を少数になおしたものは次の3つに分類されます．

有限小数
純循環小数
混循環小数
これらは分母の値を素因数分解することで次のように区別できます．

素因数が2と5のみで構成されるならば，有限小数
素因数に2と5が含まれていなければ，純循環小数
それ以外の場合，混循環小数
'''
