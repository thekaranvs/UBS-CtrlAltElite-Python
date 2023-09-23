import math

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def minimum_distance_travel(k, p, q):
    n = len(q)
    
    # Calculate distances between starting point and teleportation hubs
    hub_distances = [calculate_distance((0, 0), hub) for hub in p]

    # Initialize the dynamic programming table
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    dp[0][k] = 0

    for i in range(1, n + 1):
        for j in range(k + 1):
            # Case 1: Teleport to the current item destination directly
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + calculate_distance(q[i - 1], q[i - 2]))

            for l in range(len(p)):
                # Case 2: Teleport to the current item destination from a teleportation hub
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + calculate_distance(p[l], q[i - 1]) + calculate_distance(q[i - 1], q[i - 2]))

    return dp[n][k]

# Test case
input_data = {
    "k": 10,
    "p": [[0, 0], [0, 100], [100, 0], [100, 100]],
    "q": [[1, 0], [1, 100], [99, 0], [99, 100]]
}

k = input_data["k"]
p = input_data["p"]
q = input_data["q"]

result = minimum_distance_travel(k, p, q)
print(result)