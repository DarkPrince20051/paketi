from itertools import permutations

# Kamioni imaju kapacitet 70 tona svaki
kapacitet_kamiona = 70

# Paketi koje treba rasporediti
paketi = [10, 20, 30, 40, 50]

# Skladištenje svih mogućih rješenja
sva_rjesenja = set()

# Generisanje svih mogućih raspodela paketa u tri kamiona
for p in permutations(paketi):
    # Grupisanje paketa u tri kamiona
    kamion1, kamion2, kamion3 = p[:2], p[2:4], p[4:]
    
    # Provera da li svaki kamion ostaje unutar dozvoljene težine
    if sum(kamion1) <= kapacitet_kamiona and sum(kamion2) <= kapacitet_kamiona and sum(kamion3) <= kapacitet_kamiona:
        rjesenje = tuple(sorted([tuple(sorted(kamion1)), tuple(sorted(kamion2)), tuple(sorted(kamion3))]))
        sva_rjesenja.add(rjesenje)

# Prikaz svih mogućih rasporeda
for r in sorted(sva_rjesenja):
    print(r)
