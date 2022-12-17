nucleotides = ['A', 'T', 'C', 'G']

def generate_all_sequences(n):

    if n < 1:
        return []

    if n == 1:
        return nucleotides

    sub_sequences = generate_all_sequences(n - 1)
    
    base_pairs = []

    for sequence in sub_sequences:

        for nucleotide in nucleotides:

                 base_pairs.append(nucleotide + sequence)
    
    return base_pairs


print(len(generate_all_sequences(5)))

print(len(set(generate_all_sequences(5))))