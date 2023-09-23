import json

def returnFruits(text):

    case = json.loads(text)

    print(case)

    w = case["w"]
    v = case["v"]
    f = case["f"]

    # n = len(f)
    # dp = [[0 for _ in range(v + 1)] for _ in range(w + 1)]

    # for i in range(1, n + 1):
    #     weight, volume, value = f[i-1]

    #     for j in range(w, weight-1, -1):
    #         for k in range(v, volume-1, -1):
    #             if weight <= j and volume <= k:
    #                 if dp[j - weight][k - volume] + value > dp[j][k]:
    #                     dp[j][k] = dp[j - weight][k - volume] + value


    # output = dp[w][v]

    # return str(output)

    currWeight = 0
    currVolume = 0
    values = []
    for i in range(len(f)):
        if (currWeight + f[i][0]) <= w and (currVolume + f[i][1]) <= v:
            values.append((f[i][2], i))
            currWeight += f[i][0]
            currVolume += f[i][1]
        elif (currWeight + f[i][0]) > w and (currVolume + f[i][1]) <= v:
            values.sort()
            for value in values:
                if value[0] < f[i][2] and currWeight - f[value[1]][0] + f[i][0] <= w:
                    values.remove(value)
                    values.append((f[i][2], i))
                    break
        elif (currWeight + f[i][0]) <= w and (currVolume + f[i][1]) > v:
            values.sort()
            for value in values:
                if value[0] < f[i][2] and currVolume - f[value[1]][1] + f[i][1] <= v:
                    values.remove(value)
                    values.append((f[i][2], i))
                    break
        else:
            values.sort()
            for value in values:
                if value[0] < f[i][2] and  currVolume - f[value[1]][1] + f[i][1] <= v and currWeight - f[value[1]][0] + f[i][0] <= w:
                    values.remove(value)
                    values.append((f[i][2], i))
                    break
        
    output = 0
    for value in values:
        output += value[0]

    return(str(output))



