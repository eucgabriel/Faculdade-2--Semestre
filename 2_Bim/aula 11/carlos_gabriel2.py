arquivo = open("notas_estudantes.txt", "r")
parte = arquivo.readlines()
arquivo.close()
for produto in parte:
    soma = 0
    num = produto.split()
    for x in num[1:50]:
        soma += int(x)
    print(num[0], ':', soma/(len(num)-1))
