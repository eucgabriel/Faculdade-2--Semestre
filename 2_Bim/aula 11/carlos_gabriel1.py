arquivo = open("notas_estudantes.txt", "r")
nomes = []
linhas = arquivo.readlines()
for a in linhas:
    a = a.split()
    if (len(a)) > 6:
        nomes.append(a[0])
arquivo.close()
print(nomes)
