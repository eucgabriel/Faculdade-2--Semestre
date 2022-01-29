# Recebe notas
nota1 = int(input("Qual a sua nota no 1º Bimestre?"))
nota2 = int(input("Qual a sua nota no 2º Bimestre?"))
# Cálculos
result = (nota1 + nota2)/2
# Ifs
if(result >= 0 and result <= 4.9):
    print("Sua média foi D!!")
elif(result >= 5 and result <= 6.9):
    print("Sua média foi C!!")
elif(result >= 7 and result <= 8.9):
    print("Sua média é B!!")
elif(result <= 9 and result <= 10):
    print("Sua média é A!!")
else:
    print("Error 404!!!")
