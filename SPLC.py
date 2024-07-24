def dna_to_protein(dna, introns):
    for intron in introns:
        dna = dna.replace(intron, '')
    rna = dna.replace('T', 'U')
    codon_table = {
        'AUG': 'M', 'UGG': 'W', 'UAA': '', 'UAG': '', 'UGA': '',
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'UAU': 'Y', 'UAC': 'Y', 'CAU': 'H', 'CAC': 'H',
        'CAA': 'Q', 'CAG': 'Q', 'AAU': 'N', 'AAC': 'N',
        'AAA': 'K', 'AAG': 'K', 'GAU': 'D', 'GAC': 'D',
        'GAA': 'E', 'GAG': 'E', 'UGU': 'C', 'UGC': 'C',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    protein = ''
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if codon in codon_table:
            protein += codon_table[codon]
    return protein

dna = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
introns = ["GCCGCTGAAAGGGTGCCCGATAG"]
print(dna_to_protein(dna, introns))