def calculateWeight(colony, generations):
    weight = sum(colony)
    addedWeight = 0

    for _ in range(generations):
        newColony = []

        weight += addedWeight
        addedWeight = 0

        for i in range(len(colony) - 1):
            diff = colony[i] - colony[i+1]
            signature = diff if diff >= 0 else 10 + diff
            newDigit = (signature + weight) % 10
            addedWeight += newDigit
            newColony.extend([colony[i], newDigit])
        newColony.append(colony[-1])

        colony = newColony
    return weight, colony


def digitalColonyEntry(input):
    output = []

    genTen = input[0]
    colony = [int(x) for x in genTen['colony']]
    result = calculateWeight(colony, genTen['generations']+1)
    print(genTen['generations'], colony)
    output.append(str(result[0]))

    genFifty = input[1]
    newColony = result[1]
    remainingGens = genFifty['generations'] - genTen['generations']
    result = calculateWeight(newColony, remainingGens)
    output.append(str(result[0]))

    return output