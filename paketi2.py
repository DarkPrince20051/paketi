from itertools import combinations

# Svi paketi koji trebaju biti raspoređeni
paketi = [10, 20, 30, 40, 50]
kapacitet = 70

# Skladištimo sva moguća rješenja
sva_rjesenja = set()

# Generišemo sve kombinacije za prvi kamion
for k1 in combinations(paketi, 2):  # Prvi kamion uzima 2 paketa
    preostali1 = [p for p in paketi if p not in k1]
    
    # Generišemo sve kombinacije za drugi kamion iz preostalih paketa
    for k2 in combinations(preostali1, 2):  # Drugi kamion uzima 2 paketa
        preostali2 = [p for p in preostali1 if p not in k2]
        
        # Treći kamion dobija preostali paket
        k3 = tuple(preostali2)
        
        # Provjera da li svi kamioni poštuju ograničenje težine
        if sum(k1) <= kapacitet and sum(k2) <= kapacitet and sum(k3) <= kapacitet:
            rjesenje = tuple(sorted([tuple(sorted(k1)), tuple(sorted(k2)), tuple(sorted(k3))]))
            sva_rjesenja.add(rjesenje)

# Ispis svih mogućih validnih rješenja
for r in sorted(sva_rjesenja):
    print(r)
