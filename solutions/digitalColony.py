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


def calculate_weight(colony, generations):
    cycle_start = None
    cycle_length = None
    colony_map = {}
    weight = sum(colony)
    addedWeight = 0
    for i in range(generations):
        weight += addedWeight
        addedWeight = 0
        new_colony = []
        for j in range(len(colony) - 1):
            diff = (colony[j] - colony[j+1])
            signature = diff if diff >= 0 else 10 + diff
            newDig = (signature + weight) % 10
            new_colony.append(colony[j])
            new_colony.append(newDig)
            addedWeight += newDig
        new_colony.append(colony[-1])
        
        if tuple(new_colony) in colony_map:
            cycle_start = colony_map[tuple(new_colony)]
            cycle_length = i - colony_map[tuple(new_colony)] + 1
            break
        colony_map[tuple(new_colony)] = i
        colony = new_colony
    
    if cycle_start is not None:
        remaining_generations = (generations - cycle_start) % cycle_length
        for _ in range(remaining_generations):
            weight = sum(colony)
            new_colony = []
            for j in range(len(colony) - 1):
                diff = abs(colony[j] - colony[j+1])
                signature = diff if diff < 10 else 10 - diff
                new_colony.append(weight % 10)
                weight += signature
            new_colony.append(weight % 10)
            colony = new_colony
    
    return sum(colony), new_colony

def digitalColonyEntry(input):
    output = []

    genTen = input[0]
    colony = [int(x) for x in genTen['colony']]
    result = calculate_weight(colony, genTen['generations'])
    print(genTen['generations'], colony)
    output.append(str(result[0]))

    genFifty = input[1]
    colony = [int(x) for x in genFifty['colony']]
    result = calculate_weight(colony, genFifty['generations'])
    output.append(str(result[0]))

    return output