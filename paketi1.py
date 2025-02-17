def rasporedi_pakete(paketi, kamioni, indeks, rjesenja):
    if indeks == len(paketi):
        # Provjeri da li su svi kamioni unutar dozvoljenog kapaciteta
        if all(sum(k) <= 70 for k in kamioni):
            rjesenja.add(tuple(sorted(tuple(sorted(k)) for k in kamioni)))  # Sortirano radi uklanjanja duplikata
        return
    
    # Pokušaj dodati trenutni paket u svaki kamion
    for i in range(3):
        kamioni[i].append(paketi[indeks])
        rasporedi_pakete(paketi, kamioni, indeks + 1, rjesenja)
        kamioni[i].pop()  # Vrati stanje unazad (backtracking)

def nadji_sva_rjesenja():
    paketi = [10, 20, 30, 40, 50]
    rjesenja = set()
    rasporedi_pakete(paketi, [[] for _ in range(3)], 0, rjesenja)
    
    # Ispis svih rješenja
    for r in sorted(rjesenja):
        print(r)

nadji_sva_rjesenja()
