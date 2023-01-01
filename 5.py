def DNA_strand(dna):

    new = ""

    for i in dna:
        if i not in 'ATGC':
            print("Invalid Input")
            break
        if i == 'A':
            new += 'T'
        elif i == 'C':
            new += 'G'
        elif i == 'T':
            new += 'A'
        else:
            new += 'C'

    return new

print(DNA_strand("AAAA"))