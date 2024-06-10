MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade =  int(input("informar sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Ainda não pode tirar a CNH, porem pode fazer as aulas teoricas")
else:
    print("Ainda não pode tirar a CNH")

## if Ternário

status =  "Maior de idade" if idade >= MAIOR_IDADE else "Menor de idade"