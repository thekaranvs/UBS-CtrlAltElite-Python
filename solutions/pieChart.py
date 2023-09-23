import math

def getFirstViz(input):
    amtInvested = []

    for instrument in input['data']:
        amtInvested.append(instrument['quantity'] * instrument['price'])\

    amtInvested.sort(reverse=True)
    totalAmt = sum(amtInvested)
    radianBounds = [0]
    tinyInvestmentsMade, radiansToSubtract = 0, 0

    for amt in amtInvested:
        angle = (amt / totalAmt) * 2 * math.pi

        if angle < 0.00314159:
            tinyInvestmentsMade += 1
            radiansToSubtract += (0.00314159 - angle)
            angle = 0.00314159

        radianBounds.append(radianBounds[-1] + angle)
    
    if tinyInvestmentsMade != 0:
        for i, angle in enumerate(radianBounds):
            if angle == 0 or angle == 0.00314159: continue
            else:
                radianBounds[i] = radianBounds[i] - (radiansToSubtract / (len(amtInvested) - tinyInvestmentsMade))

    return radianBounds

def getSecondViz(input):

    radianRightArk = 0.5212425666666
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
    
    tinyInvestmentsMade, radiansToSubtract = 0, 0

    for amt in amtInvested:
        angle = (amt / totalAmt) * (2/3) * math.pi

        if angle < 0.00314159:
            tinyInvestmentsMade += 1
            radiansToSubtract += (0.00314159 - angle)
            angle = 0.00314159

        instrumentBounds.append(instrumentBounds[-1] + angle)
    
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
    
    # if tinyInvestmentsMade != 0:
    #     for i, angle in enumerate(radianBounds):
    #         if angle == 0 or angle == 0.00314159: continue
    #         else:
    #             radianBounds[i] = radianBounds[i] - (radiansToSubtract / (len(amtInvested) - tinyInvestmentsMade))
    return {
        "instruments": instrumentBounds,
        "currency": currencyBounds,
        "sector": sectorBounds,
        "assetClass": assetBounds,
        "region": regionBounds
    }

def pieChartEntry(input):
    if input['part'] == 'FIRST':
        return getFirstViz(input)
    else:
        return getSecondViz(input)