import math

def getFirstViz(input):
    amtInvested = []

    for instrument in input['data']:
        amtInvested.append(instrument['quantity'] * instrument['price'])

    amtInvested.sort(reverse=True)
    totalAmt = sum(amtInvested)
    radianBounds = [0]
    tinyAngles, radiansToSubtract = 0, 0

    for amt in amtInvested:
        angle = (amt / totalAmt) * 2 * math.pi

        if (amt / totalAmt) < 0.0005:
            tinyAngles += 1
            radiansToSubtract += (0.0005 * 2 * math.pi - angle)
            angle = 0.0005 * 2 * math.pi

        radianBounds.append(radianBounds[-1] + angle)
    if tinyAngles != 0:
        angleDiffs = [radianBounds[i+1] - radianBounds[i] for i in range(0, len(radianBounds)-1)]
        for i, angleDiff in enumerate(angleDiffs):
            if not (math.isclose(angleDiff, 0.0005 * 2 * math.pi)):
                print('adjusting', amtInvested[i], radianBounds[i+1], (totalAmt - (0.005 * totalAmt * tinyAngles)))
                subValue = (radiansToSubtract * (amtInvested[i] / (totalAmt - (0.0005 * totalAmt * tinyAngles))))
                for j in range(i+1, len(radianBounds)):
                    radianBounds[j] = radianBounds[j] - subValue

    return {"instruments": radianBounds}

def getSecondViz(input):

    radianRightArk = 0.5212425667
    currencyBounds, currencyMap = [0.52359878], {}
    sectorBounds, sectorMap = [1.04798295], {}
    assetBounds, assetMap = [1.57236712], {}
    regionBounds, regionMap = [2.09675130], {}
    amtInvested = []

    for instrument in input['data']:
        currencyMap[instrument['currency']] = currencyMap.get(instrument['currency'], 0) + (instrument['quantity'] * instrument['price'])
        sectorMap[instrument['sector']] = sectorMap.get(instrument['sector'], 0) + (instrument['quantity'] * instrument['price'])
        assetMap[instrument['assetClass']] = assetMap.get(instrument['assetClass'], 0) + (instrument['quantity'] * instrument['price'])
        regionMap[instrument['region']] = regionMap.get(instrument['region'], 0) + (instrument['quantity'] * instrument['price'])
        amtInvested.append(instrument['quantity'] * instrument['price'])

    amtInvested.sort()
    totalAmt = sum(amtInvested)
    instrumentBounds = [3.66519143]
    
    tinyAngles, radiansToSubtract = 0, 0

    for amt in amtInvested:
        angle = (amt / totalAmt) * (2/3) * math.pi
        if angle < 0.00314159:
            tinyAngles += 1
            radiansToSubtract += (0.00314159 - angle)
            angle = 0.00314159
        instrumentBounds.append(instrumentBounds[-1] + angle)
    
    if tinyAngles != 0:
        denom = len(amtInvested) - tinyAngles - 1
        for i, angle in enumerate(instrumentBounds):
            if i == 0:
                continue
            if angle == 0 or angle == 0.00314159: continue
            else:
                instrumentBounds[i] = instrumentBounds[i] - (radiansToSubtract / denom)
    
    tinyAngles, radiansToSubtract = 0, 0
    currencyMap = sorted(currencyMap.items(), key=lambda x:x[1], reverse=True)
    for currency, value in currencyMap:
        angle = (value / totalAmt) * radianRightArk # 0.52123714083
        currencyBounds.append(currencyBounds[-1] + angle)
    
    sectorMap = sorted(sectorMap.items(), key=lambda x:x[1], reverse=True)
    for sector, value in sectorMap:
        angle = (value / totalAmt) * radianRightArk # 0.52123714083
        sectorBounds.append(sectorBounds[-1] + angle)
    
    assetMap = sorted(assetMap.items(), key=lambda x:x[1], reverse=True)
    for assetClass, value in sectorMap:
        angle = (value / totalAmt) * radianRightArk # 0.52123714083
        assetBounds.append(assetBounds[-1] + angle)
    
    regionMap = sorted(regionMap.items(), key=lambda x:x[1], reverse=True)
    for region, value in regionMap:
        angle = (value / totalAmt) * radianRightArk # 0.52123714083
        regionBounds.append(regionBounds[-1] + angle)
    
    return {
        "instruments": instrumentBounds,
        "currency": currencyBounds,
        "sector": sectorBounds,
        "assetClass": assetBounds,
        "region": regionBounds
    }

def pieChartEntry(input):
    print(input)
    print('-------------------')
    if input['part'] == 'FIRST':
        result = getFirstViz(input)
        print(result)
        return result
    else:
        result = getSecondViz(input)
        print(result)
        return result
