def find_missing_edges(n, edges):
    return n - 1 - len(edges)

if __name__ == "__main__":
    n = 5
    edges = [(1, 2), (2, 3), (3, 4)]
    missing_edges = find_missing_edges(n, edges)
    print(missing_edges)