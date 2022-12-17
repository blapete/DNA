nucleotides = ['A', 'T', 'C', 'G']

def generate_all_sequences(n):

    if n < 1:
        return []

    if n == 1:
        return nucleotides

    sub_sequences = generate_all_sequences(n - 1)
    
    sequences = []

    for sequence in sub_sequences:

        for nucleotide in nucleotides:

                 sequences.append(nucleotide + sequence)
    
    return sequences

print(generate_all_sequences(2))

print(len(generate_all_sequences(2)))