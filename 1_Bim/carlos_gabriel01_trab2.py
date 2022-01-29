import os
# Contar Votos
branco = 0
samuca = 0
neto = 0
baltazar = 0
nulo = 0
num_eleitores = int(input("Digite o nº de eleitores nessa seção:"))

for i in range(0, num_eleitores):
    voto = input(
        "Em quem vc vai votar?(samuca(1), neto(2), baltazar(3), branco(0) ou nulo(4))")
    if voto == "1":
        samuca = samuca + 1
        os.system("cls")
    elif voto == "2":
        neto = neto + 1
        os.system("cls")
    elif voto == "3":
        baltazar = baltazar + 1
        os.system("cls")
    elif voto == "0":
        branco = branco + 1
        os.system("cls")
    elif voto == "4":
        nulo = nulo + 1
        os.system("cls")
    else:
        print("O que você ta querendo fazer? Uma macarronada?")
        os.system("cls")

if samuca > neto and samuca > baltazar:
    print(f"""
         O vencedor foi o Samuca com {samuca} votos!!
         Teve {nulo} votos nulos e {branco} votos em branco
         O nº de eleitores foi de {num_eleitores}
         """)
    os.system("pause")
elif neto > samuca and neto > baltazar:
    print(f"""
         O vencedor foi o Neto com {neto} votos!!
         Teve {nulo} votos nulos e {branco} votos em branco
         O nº de eleitores foi de {num_eleitores}
         """)
    os.system("pause")
elif baltazar > neto and baltazar > samuca:
    print(f"""
         O vencedor foi o Samuca com {baltazar} votos!!
         Teve {nulo} votos nulos e {branco} votos em branco
         O nº de eleitores foi de {num_eleitores}
         """)
    os.system("pause")
elif samuca == neto:
    print("Vai ter segundo turno entre Samuca e Neto!")
    os.system("pause")
elif samuca == baltazar:
    print("Vai ter segundo turno entre Samuca e Baltazar!")
    os.system("pause")
elif baltazar == neto:
    print("Vai ter segundo turno entre Baltazar e Neto!")
    os.system("pause")
