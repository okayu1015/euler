import math
def listExcludedIndices(data, indices=[]):
  return [x for i, x in enumerate(data) if i not in indices]
data = [0,1,2,3,4,5,6,7,8,9]
D = []
result = []
cnt = 0
for i in range(len(data)):
  for j in range(len(data) - 1):
    for k in range(len(data) - 2):
        for l in range(len(data) - 3):
            for m in range(len(data) - 4):
                for n in range(len(data) - 5):
                    for o in range(len(data) - 6):
                        for p in range(len(data) - 7):
                            for q in range(len(data) - 8):
                                for r in range(len(data) - 9):
                                    jData = listExcludedIndices(data, [i])
                                    kData = listExcludedIndices(jData, [j])
                                    lData = listExcludedIndices(kData, [k])
                                    mData = listExcludedIndices(lData, [l])
                                    nData = listExcludedIndices(mData, [m])
                                    oData = listExcludedIndices(nData, [n])
                                    pData = listExcludedIndices(oData, [o])
                                    qData = listExcludedIndices(pData, [p])
                                    rData = listExcludedIndices(qData, [q])
                                    ans = (str(data[i]) + str(jData[j]) + str(kData[k]) +
                                    str(lData[l]) + str(mData[m]) + str(nData[n]) + str(oData[o]) +
                                    str(pData[p])
                                           + str(qData[q])
                                           + str(rData[r]))
                                    result.append(ans)
                                    cnt += 1
                                    if cnt == 1000000:
                                        print(result[-1])
        
print(cnt)
print(math.factorial(10))
