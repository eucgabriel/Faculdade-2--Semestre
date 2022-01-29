arquivo = open("notas_estudantes.txt", "r")
parte = arquivo.readlines()
arquivo.close()
for produto in parte:
    lista = produto.split()
    estudantes = lista[0]
    del lista[0]
    notas = list(map(int, lista))
    print("{} teve a nota máxima: {} e nota mínima : {}".format(
        estudantes, max(notas), min(notas)))
