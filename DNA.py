# A <--> T
# C <--> G

def DNA_strand(dna):
    resultant_dna = ''
    for i in range(len(dna)):
        if dna[i] == 'A':
            resultant_dna += 'T'
        elif dna[i] == 'T':
            resultant_dna += 'A'
        elif dna[i] == 'C':
            resultant_dna += 'G'
        elif dna[i] == 'G':
            resultant_dna += 'C'
    return resultant_dna

DNA_strand("AAAA")
DNA_strand("ATTGC")
DNA_strand("GTAT")