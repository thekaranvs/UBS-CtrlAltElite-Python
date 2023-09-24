import math

def calculate_min_distance_delivery(k, p, q):
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

def teleportationEntry(input):
    return calculate_min_distance_delivery(input['k'], input['p'], input['q'])
