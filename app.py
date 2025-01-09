import random

# cria uma lista de palavras para serem sorteadas
palavras = ['python', 'computador', 'programacao', 'aula' ]

# escolher uma palavra
palavra_sorteada = random.choice(palavras)

# criar uma string com traços para representar letras
palavra_escondida = '-' * len(palavra_sorteada)

# criar lista para as letras adivinhadas
letras_adivinhadas = []

max_tentativas = 6

while True:
    #  mostra a palavra escondida
    print(palavra_escondida)
    #  pedir ao usuario para digitar uma letra
    letra = input('Digite uma letra:').strip().lower()
    
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, digite apenas uma letra.")
        continue
    # verificar se a letra já foi digitada
    if letra in letras_adivinhadas:
        print('Você já digitou essa letra. Tente outra')
        continue

    # adiciona letra adivinhada na lista
    letras_adivinhadas.append(letra)
    
    # verifica se a letra está la palavra sorteada
    if letra in palavra_sorteada:
        lista =[]
        for indice in range(len(palavra_sorteada)):
            if letra == palavra_sorteada[indice]:
                lista.append(letra)
            else:
                lista.append(palavra_escondida[indice])
        palavra_escondida = ''.join(lista)
    else:
        max_tentativas -= 1
        print(f'Não tem essa letra. Você tem {max_tentativas} tentativa(s)')
        
    # verifica se o jogador ganhou ou perdeu
    if palavra_escondida == palavra_sorteada:
        print('Parabéns. Você ganhou!')
        break
    elif max_tentativas == 0:
        print(f'Você perdeu. A palavra sorteada foi {palavra_sorteada}')
        break