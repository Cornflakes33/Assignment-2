def merge_strings(a, b):
    max_overlap = 0
    for i in range(1, len(a)):
        if b.startswith(a[i:]):
            max_overlap = len(a) - i
            break
    return a + b[max_overlap:]

def shortest_superstring(strings):
    while len(strings) > 1:
        max_len = -1
        a, b = -1, -1
        for i in range(len(strings)):
            for j in range(len(strings)):
                if i != j:
                    merged = merge_strings(strings[i], strings[j])
                    overlap_len = len(strings[i]) + len(strings[j]) - len(merged)
                    if overlap_len > max_len:
                        max_len = overlap_len
                        a, b = i, j
        if a != -1 and b != -1:
            strings[a] = merge_strings(strings[a], strings[b])
            strings.pop(b)
    return strings[0]

strings = ["ATTAGACCTG", "CCTGCCGGAA", "AGACCTGCCG", "GCCGGAATAC"]
print(shortest_superstring(strings))