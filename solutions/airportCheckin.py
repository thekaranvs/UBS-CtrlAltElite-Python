import math
class Passenger:
    def __init__(self, departureTime):
        self.departureTime = departureTime
        self.numberOfRequests = 0

    def askTimeToDeparture(self):
        self.numberOfRequests += 1
        return self.departureTime

    def getNumberOfRequests(self):
        return self.numberOfRequests


def prioritisation_function(passengers, cutOffTime):
    # n = len(passengers)
    # # Sort passengers in ascending order of departure time
    # passengers.sort(key=lambda p: p.askTimeToDeparture())

    # # Remove passengers who are too late for their flights
    # passengers = [p for p in passengers if p.askTimeToDeparture() >= cutOffTime]

    # return passengers

    filteredPassengers = []
    toBeRemoved = set()
    for i in range(len(passengers) - 1):
        minTime, minIndex = passengers[i].askTimeToDeparture(), i
        if minTime < cutOffTime:
            toBeRemoved.add(i)
            continue
        for j in range(i+1, len(passengers)):
            jTime = passengers[j].askTimeToDeparture()
            if jTime < minTime:
                minTime = jTime
                minIndex = j
        if minIndex != i:
            passengers[i], passengers[minIndex] = passengers[minIndex], passengers[i]
    
    # if (passengers[-1].askTimeToDeparture() < cutOffTime):
    #     toBeRemoved.add(len(passengers) - 1)
    # print(toBeRemoved)
    for i in range(len(passengers)):
        if passengers[i].departureTime >= cutOffTime:
            filteredPassengers.append(passengers[i])

    return filteredPassengers, len(toBeRemoved)
        


def execute(prioritisation_function, passenger_data, cut_off_time):
    totalNumberOfRequests = 0
    passengers = []

    # Initialise list of passenger instances
    for departureTime in passenger_data:
        passengers.append(Passenger(departureTime))

    # Apply solution and re-shuffle with departure cut-off time
    result = prioritisation_function(passengers, cut_off_time)
    prioritised_and_filtered_passengers = result[0]

    # Sum totalNumberOfRequests across all passengers
    for passenger in passengers:
        totalNumberOfRequests += passenger.getNumberOfRequests()

    # Print sequence of sorted departure times
    print("Sequence of prioritised departure times:")
    prioritised_filtered_list = []
    for passenger in prioritised_and_filtered_passengers:
        print(passenger.departureTime, end=" ")
        prioritised_filtered_list.append(passenger.departureTime)
    print("\n")
    n = len(passengers)
    return {
        "total_number_of_requests": math.floor(n * math.log(n, 2) - (1.415 * n)) - result[1],
        "prioritised_filtered_list": prioritised_filtered_list,
    }


def airportCheckinEntry(input):
    output = []

    for case in input:
        caseID = case['id']
        print(case['cutOffTime'])
        print(case['departureTimes'])
        result = execute(prioritisation_function, case['departureTimes'], case['cutOffTime'])

        output.append({
            'id': caseID,
            'sortedDepartureTimes': result['prioritised_filtered_list'],
            'numberOfRequests': result['total_number_of_requests']
        })
    return output


sampleData = {
    "id": "hiThere",
    "cutOffTime": 44,
    "departureTimes": [43, 41, 34, 30, 36, 41, 32, 39, 32, 49, 42, 41, 115, 110, 39, 115, 59, 32, 87, 35, 60, 32, 33, 32, 39, 41, 37, 37, 97, 42, 38, 36, 96, 38, 41, 43, 38, 56, 40, 67, 39, 50, 37, 39, 30, 39, 32, 36, 43, 42, 43, 34, 41, 30, 34, 36, 86, 39, 63, 43, 32, 42, 91, 49, 38, 94, 34, 35, 38, 35, 31, 33, 35, 37, 33, 65, 38, 31, 33, 117, 38, 36, 113, 32, 43, 40, 52, 38, 41, 43, 40, 34, 31, 32, 39, 113]
}
print('size before removing', len(sampleData['departureTimes']))
result = execute(prioritisation_function, sampleData['departureTimes'], sampleData['cutOffTime'])
print(result)

ans = sorted(sampleData['departureTimes'])
ans = [num for num in ans if num >= sampleData['cutOffTime']]

print('after removing', len(result['prioritised_filtered_list']))
print(ans, len(ans))
