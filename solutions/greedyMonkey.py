import json

def returnFruits(text):

    case = json.loads(text)

    print(case)

    w = case["w"]
    v = case["v"]
    f = case["f"]

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
                    values.append(f[i][2], i)
                    break
        elif (currWeight + f[i][0]) <= w and (currVolume + f[i][1]) > v:
            values.sort()
            for value in values:
                if value[0] < f[i][2] and currVolume - f[value[1]][1] + f[i][1] <= v:
                    values.remove(value)
                    values.append(f[i][2], i)
                    break
        else:
            values.sort()
            for value in values:
                if value[0] < f[i][2] and  currVolume - f[value[1]][1] + f[i][1] <= v and currWeight - f[value[1]][0] + f[i][0] <= w:
                    values.remove(value)
                    values.append((f[i][2], i))
                    break
        
    output = ""
    for value in values:
        output += str(value[1]+1)

    output += "0"

    return(output)



