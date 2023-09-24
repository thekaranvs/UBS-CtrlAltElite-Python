import math

def calculate_min_distance_delivery1(k, p, q):
    total_distance = 0
    current_location = [0, 0]

    # Iterate over each delivery location
    for i in range(len(q)):
        # Check if there are remaining teleportation orbs
        if k > 0:
            min_teleport_distance = math.sqrt((q[i][0] - current_location[0])**2 + (q[i][1] - current_location[1])**2)
            teleport_hub_index = -1
            for j in range(len(p)):
                teleport_distance = math.sqrt((p[j][0] - q[i][0])**2 + (p[j][1] - q[i][1])**2)
                if teleport_distance < min_teleport_distance:
                    min_teleport_distance = teleport_distance
                    teleport_hub_index = j

            if min_teleport_distance < math.sqrt((current_location[0] - q[i][0])**2 + (current_location[1] - q[i][1])**2):
                total_distance += min_teleport_distance
                k -= 1
                current_location = q[i]
            else:
                # Calculate Euclidean distance from current location to delivery location
                distance = math.sqrt((current_location[0] - q[i][0])**2 + (current_location[1] - q[i][1])**2)
                total_distance += distance
        else:
            # Calculate Euclidean distance from current location to delivery location
            distance = math.sqrt((current_location[0] - q[i][0])**2 + (current_location[1] - q[i][1])**2)
            total_distance += distance
        current_location = q[i]

    return round(total_distance, 2)

import math

def calculate_min_distance_delivery(k, p, q):
    memo = {}  # Memoization table to store minimum distances

    def dp(current_index, k):
        # Check if the current state has already been computed
        if (current_index, k) in memo:
            return memo[(current_index, k)]

        # Base case: No remaining delivery locations
        if current_index == len(q):
            return 0

        min_distance = math.inf

        if k > 0:
            # Calculate the minimum distance between teleporting now and teleporting later
            min_dist_now = distance_to_nearest_teleport(current_index) + dp(current_index + 1, k - 1)
            min_dist_later = dp(current_index + 1, k)
            min_distance = min(min_distance, min_dist_now, min_dist_later)
        else:
            min_distance = distance_to_nearest_teleport(current_index) + dp(current_index + 1, k)

        # Store the computed minimum distance in the memoization table
        memo[(current_index, k)] = min_distance

        return min_distance

    def distance_to_nearest_teleport(current_index):
        min_distance = math.inf

        for i in range(len(p)):
            # Calculate Euclidean distance from current delivery location to the teleportation hub
            teleport_distance = math.sqrt((q[current_index][0] - p[i][0])**2 + (q[current_index][1] - p[i][1])**2)
            min_distance = min(min_distance, teleport_distance)

        return min_distance

    # Call the DP function with the initial state
    min_distance = dp(0, k)
    return round(min_distance, 2)

k = 10
p = [[0, 0], [0, 100], [100, 0], [100, 100]]
q = [[1, 0], [1, 100], [99, 0], [99, 100]]

distance = calculate_min_distance_delivery(k, p, q)
print(distance)

def teleportationEntry(input):
    return calculate_min_distance_delivery(input['k'], input['p'], input['q'])
