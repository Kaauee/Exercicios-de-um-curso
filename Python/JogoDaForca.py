
palavra = input('Usuario 1, Por favor insira a palavra: ')
palavra = palavra.lower()

for i in range(20):
    print('/-/-/-/-/')
lista_cert = []

while True:
    letra = input('Digite uma letra ')
  #Somente 1 letra por vez
    if len(letra) > 1:
        print('Digite denovo apenas uma letra ')
        continue
    #
    else:
        #Comando para adicionar
        lista_cert.append(letra)
        # Se há a letra na palavra
        if letra in palavra:
            print(f'Acertou, a letra "{letra}" existe ')
        # Se NÃO há a letra na palavra
        else:
            print(f'Errou, a letra "{letra}" nao existe')
            lista_cert.pop()

        palavra_temp = ''
        for letra_descoberta in palavra:
            # Se a letra descoberta contem na lista_cert
            if letra_descoberta in lista_cert:
                palavra_temp += letra_descoberta
            # Se nao ele troca por asterisco
            else:
                palavra_temp += '*'

    if palavra_temp == palavra:
        print(f'Voce Venceu, a palavra era "{palavra}"')
        exit()
    else:
        print(f'A palavra atualmente esta assim: "{palavra_temp}"')
    print(lista_cert)
    print()