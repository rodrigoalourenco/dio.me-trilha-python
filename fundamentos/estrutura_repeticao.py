TEXTO = input("informe um texto: ")
VOGAIS = 'AEIOU'

for letra in TEXTO:
    if letra.upper() in VOGAIS:
        print (letra, end="")
print("\n\n")

# range
for numero in range(0, 51, 5):
    print(numero, end=" ")
else:
    print("\n\n")

#while
opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Estrato \n[0] Sair \n:  "))
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
    elif opcao == 10:
        print("erro 500")
        break
