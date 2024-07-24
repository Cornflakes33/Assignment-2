from collections import Counter

def reverse_complement(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(seq))

def find_errors(sequences):
    counts = Counter(sequences + [reverse_complement(seq) for seq in sequences])
    correct = {seq for seq, count in counts.items() if count > 1}
    errors = [seq for seq in sequences if counts[seq] == 1 and counts[reverse_complement(seq)] == 1]
    corrections = []
    for error in errors:
        for correct_seq in correct:
            if sum(1 for a, b in zip(error, correct_seq) if a != b) == 1:
                corrections.append((error, correct_seq))
                break
    return corrections

if __name__ == "__main__":
    sequences = [
        "TTCAT",
        "TTGAT",
        "TTGTT",
        "TGCAA",
        "TTGAT",
        "TTGTA"
    ]
    corrections = find_errors(sequences)
    for error, correction in corrections:
        print(f"{error}->{correction}")