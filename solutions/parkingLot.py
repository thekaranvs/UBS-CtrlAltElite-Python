import json
def returnProfit(jsonObj):

    profit = 0
    busSlots = jsonObj["BusParkingSlots"]
    carSlots = jsonObj["CarParkingSlots"]
    busCharge, carCharge, bikeCharge = jsonObj["ParkingCharges"].values()
    numBuses = jsonObj["Buses"]
    numCars = jsonObj["Cars"]
    numBikes = jsonObj["Bikes"]

    # carBaseCharge = carCharge / 5
    # busBaseCharge = busCharge / 12

    # if bikeCharge > carBaseCharge:
    #     best = "Bike"
    # else:
    #     best = "Car"
    # # chargeAndSpaces = [(carBaseCharge, 5, numCars), (bikeCharge, 1, numBikes)].sort()

    # busSpace = busSlots * 12
    # carSpace = carSlots * 5

    # while carSpace != 0:
    #     if best == "Bike":
    #         if numBikes != 0:
    #             profit += bikeCharge
    #             carSpace -= 1
    #             numBikes -= 1
    #         elif carSpace >= 5 and numCars != 0:
    #             profit += carCharge
    #             carSpace -= 5
    #             numCars -= 1
    #         else:
    #             break
            
    #     else:
    #         if carSpace >= 5 and numCars != 0:
    #             profit += carCharge
    #             carSpace -= 5
    #             numCars -= 1
    #         elif numBikes != 0:
    #             profit += bikeCharge
    #             carSpace -= 1
    #             numBikes -= 1
    #         else:
    #             break
             
    # tempProfit = profit
    # tempNumBikes = numBikes
    # tempNumCars = numCars

    # if carSpace != 0:
    #     while carSpace < 5:
    #         carSpace += 1
    #         tempProfit -= bikeCharge
    #         tempNumBikes += 1
    #     tempProfit += carCharge
    #     carSpace -= 5
    #     tempNumCars -=1

    # if tempProfit > profit:
    #     numBikes = tempNumBikes
    #     numCars = tempNumCars
    #     profit = tempProfit
            
    # while busSpace != 0:
    #     if busSpace <= chargeAndSpaces[0][1] and chargeAndSpaces[0][3] != 0:
    #         profit += chargeAndSpaces[0][0] * chargeAndSpaces[0][1]
    #         busSpace -= chargeAndSpaces[0][1]
    #         chargeAndSpaces[0][3] = chargeAndSpaces[0][3] - 1
        
    #     elif busSpace <= chargeAndSpaces[1][1] and chargeAndSpaces[1][3] != 0:
    #         profit += chargeAndSpaces[1][0] * chargeAndSpaces[1][1]
    #         busSpace -= chargeAndSpaces[1][1]
    #         chargeAndSpaces[1][3] = chargeAndSpaces[1][3] - 1
        
    #     elif busSpace <= chargeAndSpaces[2][1] and chargeAndSpaces[2][3] != 0:
    #         profit += chargeAndSpaces[2][0] * chargeAndSpaces[2][1]
    #         busSpace -= chargeAndSpaces[2][1]
    #         chargeAndSpaces[2][3] = chargeAndSpaces[2][3] - 1
    #     else:
    #         break

    # return profit

    max_bikes = carSlots * 5 + busSlots * 12
    max_cars = carSlots + busSlots*2

    profits = []
    for buses_parked in range(min(numBuses + 1, busSlots + 1)):
        for cars_parked in range(min(numCars + 1, max_cars + 1)):
            for bikes_parked in range(min(numBikes + 1, max_bikes + 1)):
                # Check if the combination exceeds the available slots
                if buses_parked*12 + cars_parked*5 + bikes_parked > busSlots*12 + carSlots:
                    continue
                
                # Calculate the total profit for this combination
                bus_profit = buses_parked * busCharge
                car_profit = cars_parked * carCharge
                bike_profit = bikes_parked * bikeCharge
                total_profit = bus_profit + car_profit + bike_profit
                
                print(buses_parked, cars_parked, bikes_parked, total_profit)
                # Append the combination and its profit to the list
                profits.append((total_profit, buses_parked, cars_parked, bikes_parked))
    
    # Sort the list of profits in descending order
    profits.sort(reverse=True)
    
    # Find the combination with the highest profit
    max_profit, buses_assigned, cars_assigned, bikes_assigned = profits[0]
    
    # Calculate the rejected vehicles
    buses_rejected = max(numBuses - buses_assigned, 0)
    cars_rejected = max(numCars - cars_assigned, 0)
    bikes_rejected = max(numBikes - bikes_assigned, 0)
    
    # Return the results
    return {"Answer": {"Profit":max_profit, "BusRejections":buses_rejected, "CarRejections":cars_rejected, "BikeRejections":bikes_rejected}}