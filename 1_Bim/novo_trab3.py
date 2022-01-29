global prod, qnt, prc, fat
prod = []
prc = []
qnt = []
fat = float()


def CalcularFat():
    while True:
        sair = input("Insira o Produto:(e quando terminar digar 'SAIR')")
        if sair.upper() == 'SAIR':
            break
        else:
            prod.append(sair)
            qnt.append(int(input('Quantidade: ')))
            prc.append(float(input("Preço: ")))
    teste = len(prod)
    fat = float(0)
    for l in range(teste):
        fat += (qnt[l] * prc[l])
    print(" \n \n faturamento: R${} " .format(fat))


CalcularFat()
