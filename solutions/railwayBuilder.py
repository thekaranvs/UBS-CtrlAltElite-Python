def buildRailway(totalLength, lengthOfTrackPiece):
    cache = {}

    def dfs(i, a):
        if a == totalLength:
            return 1
        if a > totalLength:
            return 0
        if i == len(lengthOfTrackPiece):
            return 0
        if (i, a) in cache:
            return cache[(i, a)]
        
        cache[(i, a)] = dfs(i, a + lengthOfTrackPiece[i]) + dfs(i + 1, a)
        return cache[(i, a)]
    return dfs(0, 0)

def railwayBuilderEntry(input):
    output = []
    for case in input:
        tmpData = case.split(', ')

        lengthOfRailWay = int(tmpData[0])
        lengthOfTrackPiece = [int(x) for x in tmpData[2:]]

        output.append(buildRailway(lengthOfRailWay, lengthOfTrackPiece))
    return output