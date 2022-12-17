pairs = {
    "A":"T",
    "C":"G",
    "G":"C",
    "T":"A",
}

input_sequence = input("Enter a nucleotide sequence: ")
reverse_complement = ""

for index in range(len(input_sequence) - 1, 0, -1):

    base = input_sequence[index]
    complement = pairs[base]
    reverse_complement += complement

print(reverse_complement)