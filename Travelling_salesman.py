import itertools

def traveling_salesman_bruteforce(distance_matrix):
    """
    Solves the Traveling Salesman Problem using brute-force.
    Args:
        distance_matrix (list of list of int/float): Square matrix of distances.
    Returns:
        tuple: (min_path, min_cost)
    """
    n = len(distance_matrix)
    cities = list(range(n))
    min_cost = float('inf')
    min_path = []

    for perm in itertools.permutations(cities[1:]):
        path = [0] + list(perm) + [0]
        cost = sum(distance_matrix[path[i]][path[i+1]] for i in range(n))
        if cost < min_cost:
            min_cost = cost
            min_path = path

    return min_path, min_cost

# Example usage:
if __name__ == "__main__":
    dist = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    path, cost = traveling_salesman_bruteforce(dist)
    print("Optimal path:", path)
    print("Minimum cost:", cost)