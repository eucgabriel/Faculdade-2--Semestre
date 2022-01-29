# Recebe notas
nado = int(input("Qual a idade do nadador?"))
# Ifs
if(nado >= 5 and nado <= 7):
    print("A categoria do nadador é Infantil A!!")
elif(nado >= 8 and nado <= 10):
    print("A categoria do nadador é Infantil B!!")
elif(nado >= 11 and nado <= 13):
    print("A categoria do nadador é Juvenil A!!")
elif(nado >= 14 and nado <= 17):
    print("A categoria do nadador é Juvenil B!!")
elif(nado >= 18):
    print("A categoria do nadador é Adulto!!")
else:
    print("O nadador é muito jovem ainda pra estar em uma categoria!!")
