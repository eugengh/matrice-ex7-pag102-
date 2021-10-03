"""
Elaboraţi un program care afişează pe ecran codurile următoarelor caractere,
introduse de la tastatură:
a) cifrele zecimale 0, 1, 2, ..., 9;
b) literele latine mari A, B, C, ..., Z;
c) literele latine mici a, b, c, ..., z;
d) semnele operaţiilor aritmetice;
e) caracterele speciale ;, <, =, >, ?, [, ], {, }, /, \.
"""
# introduceti orice litera, cifra, numar sau simbol, nu conteaza in ce oridine sau tipul caracterului!
x = input("Introduecti ceea ce se va conferta in cuv. binar: ")
print("Originalul: ", x)
res = ' '.join(format(ord(i), '08b') for i in x)
d = res.split(' ')
d = [s[1:] for s in d]
print(d)

