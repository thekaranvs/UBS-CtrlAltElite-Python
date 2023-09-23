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

    modifiedPassengers = []
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
    
    if (passengers[-1].askTimeToDeparture() < cutOffTime):
        toBeRemoved.add(len(passengers) - 1)

    for i, passenger in enumerate(passengers):
        if i in toBeRemoved:
            continue
        modifiedPassengers.append(passenger)

    return modifiedPassengers
        


def execute(prioritisation_function, passenger_data, cut_off_time):
    totalNumberOfRequests = 0
    passengers = []

    # Initialise list of passenger instances
    for departureTime in passenger_data:
        passengers.append(Passenger(departureTime))

    # Apply solution and re-shuffle with departure cut-off time
    prioritised_and_filtered_passengers = prioritisation_function(passengers, cut_off_time)

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

    return {
        "total_number_of_requests": totalNumberOfRequests,
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