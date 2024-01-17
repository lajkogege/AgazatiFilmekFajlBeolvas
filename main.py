import beolvas

filmem_lista=beolvas.fajlbeolvas()
legrovidebb_index=beolvas.legrovidebbcim(filmem_lista)
print(f"3.feladat:")
print(f"\tA legrövidebb film címe: {filmem_lista[legrovidebb_index].cim}")
szaztiesfilm=beolvas.szaztizperses(filmem_lista)
print("4.feladat:")
print(f"\t{szaztiesfilm}db legalább 110 perces film van")
print("5.feladat")