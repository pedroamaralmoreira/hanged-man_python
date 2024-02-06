import random 
def jogar_forca():
    palavra = "python"
    letras_usuario = []      #DETERMINANDO AS VARIÁVEIS
    chances = 5
    ganhou = False
    while True: #CRIAÇÃO DA LÓGICA/PENSAMENTO LÓGICO DE ACORDO À LINGUAGEM 
        
        for letra in palavra:
            if letra.lower() in letras_usuario:
                print(letra, end=" " )
            else:
                print("_", end=" ")
        print(f"Você tem {chances} chances") # Mostra o número de chances, retomando a VARIÁVEL
        tentativa = input("Escolha uma letra para adivinhar: ")
        letras_usuario.append(tentativa.lower())
        
        if tentativa.lower() not in palavra.lower(): #Reduz as chances SE o usuario errar, Ag. Condicional
            chances -= 1 
            
        ganhou = True # Faz o usuário ganhar SE acertar todas as letras
        for letra in palavra:
            if letra.lower() not in letras_usuario:
                ganhou = False
                break
            
        if chances == 0 or ganhou: 
            break
                
    if ganhou: # Escreve uma mensagem SE o usuário acertar a palavra (retomo a VARIÁVEL ''palavra'') ou errar a palavra
        print(f"Parabéns, você ganhou!. A palavra era: {palavra}")
    else:
        print(f"Você perdeu! :c . A palavra era:{palavra}")

    print("GAME OVER!") # Escreve a mensagem de jogo acabado
    answer_user = input("Gostou do jogo? (S/N)")

    
    
    opçao=input(f"deseja jogar novamente (S/N)").lower() 
    if opçao=="s":
        jogar_forca()
    else:
     quit   
jogar_forca() 