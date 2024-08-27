# Utilizamos apenas para colocar um tempo entre uma linha e outra.
import time
# Utilizamos para 'limpar' o terminal.
import os


# Função que realiza a criptografia.
def cifra_de_locomocao_unitaria(texto, chave1, chave2):
    resultado = ""
    
    # Inicia um looping sobre cada caractere do texto.
    for i, caractere in enumerate(texto):

        # Ignora caracteres acentuados deixando-os do mesmo jeito.
        if caractere in 'áàãâäéèêëíìîïóòõôöúùûüçÁÀÃÂÄÉÈÊËÍÌÎÏÓÒÕÔÖÚÙÛÜÇ':
            resultado += caractere
            continue

        # Se o que for digitado for uma letra do alfabeto...
        if caractere.isalpha():
            # Converte o caractere para minúsculo.
            # 'A' e 'a' têm valores diferentes na tabela ASCII.
            caractere = caractere.lower()
            # 97 é o valor onde as letras minúsculos iniciam na tabela ASCII.
            shift = 97
            
            # Obtém o deslocamento para cada letra posta pelo usuário.
            deslocamento1 = int(chave1[i % len(chave1)])
            # len(chave1) é uma função que retorna o comprimento de caracteres.
            # O operador % é o operador de módulo, que retorna o resto da divisão entre o valor de i e o comprimento da chave.

            # Obtém o segundo deslocamento.
            deslocamento2 = int(chave2[i % len(chave2)])
            
            # Aplica a cifra de substituição com a primeira chave.
            nova_letra = chr(((ord(caractere) - shift + deslocamento1) % 26) + shift)
            # chr transforma numeros em letras.
            # ord() retorna o valor numérico do caractere.
            # % 26 é usado para garantir que o resultado da operação esteja dentro do intervalo de 0 a 25.

            # Aplica a cifra de substituição com a segunda chave.
            nova_letra = chr(((ord(nova_letra) - shift + deslocamento2) % 26) + shift)

            # Imprime a informação sobre como o caractere é criptografado.
            print(f"Caractere '{caractere}' é criptografado usando o deslocamento {deslocamento1} da primeira chave e {deslocamento2} da segunda chave.")
            time.sleep(0.2)

            # Adiciona a nova letra ao resultado.
            resultado += nova_letra
        
        # Já se o caractere for um dígito...
        elif caractere.isdigit():

            # Obtém o deslocamento para cada dígito posto pelo usuário.
            deslocamento1 = int(chave1[i % len(chave1)])

            # Calcula o novo dígito.
            novo_digito = str((int(caractere) + deslocamento1) % 10)

            # Imprime a informação sobre como o dígito é criptografado.
            print(f"Dígito '{caractere}' é criptografado usando o deslocamento {deslocamento1} da primeira chave.")
            time.sleep(0.2)
            
            # Adiciona o novo dígito ao resultado.
            resultado += novo_digito

        else:
            # Se o caractere não for uma letra comum, com acento ou um dígito, ele é adicionado ao resultado sem alterações.
            resultado += caractere
    
    # Retorna o texto criptografado.
    return resultado


# Função que realiza a descriptografia, (invertendo valores).
def decifra_de_locomocao_unitaria(texto, chave1, chave2):
    resultado = ""
    
    for i, caractere in enumerate(texto):

        if caractere in 'áàãâäéèêëíìîïóòõôöúùûüçÁÀÃÂÄÉÈÊËÍÌÎÏÓÒÕÔÖÚÙÛÜÇ':
            resultado += caractere
            continue

        if caractere.isalpha():
            caractere = caractere.lower()
            shift = 97
            
            deslocamento1 = int(chave1[i % len(chave1)])
            deslocamento2 = int(chave2[i % len(chave2)])
            
            # Aplica a cifra de substituição com a primeira chave.
            nova_letra = chr(((ord(caractere) - shift - deslocamento1) % 26) + shift)
            # chr transforma numeros em letras.
            # ord() retorna o valor numérico do caractere.
            # % 26 é usado para garantir que o resultado da operação esteja dentro do intervalo de 0 a 25.

            # Obtém o segundo deslocamento.
            nova_letra = chr(((ord(nova_letra) - shift - deslocamento2) % 26) + shift)
            
            resultado += nova_letra

        elif caractere.isdigit():

            # Obtém o deslocamento para cada dígito posto pelo usuário.
            deslocamento1 = int(chave1[i % len(chave1)])
        
            # Calcula o novo dígito.
            novo_digito = str((int(caractere) - deslocamento1) % 10)
            
            resultado += novo_digito

        else:
            # Se o caractere não for uma letra comum, com acento ou um dígito, ele é adicionado ao resultado sem alterações.
            resultado += caractere
    
    return resultado


while True:

    # \n e print() pulam linha.
    print("\n- Menu do app KeyVault -\n")
    time.sleep(0.2)
    print("1. Descriptografar")
    time.sleep(0.2)
    print("2. Criptografar")
    time.sleep(0.2)
    print("3. Sobre\n")
    time.sleep(0.2)
    print("4. Sair...\n")

    opcao = input("Escolha uma das opções (1/2/3/4): ")
    os.system('cls')

# -----------------------------------------------------------------------------------------------------------------------
    if opcao == '1':

        # Tenta acessar a variável 'texto_cifrado'.
        try: texto_cifrado
        # Se 'texto_cifrado' não foi definido antes, inicializa vazio.
        except NameError: texto_cifrado = ""

        try: chave1
        except NameError: chave1 = ""

        try: chave2
        except NameError: chave2 = ""

        # Imprime o texto cifrado e as chaves usadas anteriormente.
        print("Texto cifrado anteriormente:", texto_cifrado)
        print("Primeira chave:", chave1)
        print("Segunda chave:", chave2)
        print()
        
        # Solicita ao usuário que insira o texto original.
        texto_original = input("Digite uma mensagem a ser descriptografada: ")

        # Solicita a primeira chave ao usuário até que ele insira apenas números.
        while True:
            chave1 = input("Agora a primeira chave de deslocamento usada em sua cifração: ")
            if chave1.isdigit():
                break
            else:
                print("Por favor, digite apenas números para a chave.")

        # Faz o mesmo para a segunda chave
        while True:
            chave2 = input("Agora a segunda chave de deslocamento usada em sua cifração: ")
            if chave2.isdigit():
                break
            else:
                print("Por favor, digite apenas números para a chave.")
                
        # Chama a função para descriptografar o texto
        texto_decifrado = decifra_de_locomocao_unitaria(texto_original, chave1, chave2)

        # Imprime o texto descriptografado
        print("\nTexto descriptografado:", texto_decifrado)
# -----------------------------------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------------------------------
    elif opcao == '2':
        texto_original = input("Digite uma mensagem a ser criptografada: ")
        print()
        print("Agora a primeira chave de deslocamento, (válida para letras e números).")
        while True:
            chave1 = input("Por exemplo, '023': ")
            if chave1.isdigit():
                break
            else:
                print("Por favor, digite apenas números para a chave.")

        print()

        print("Agora a segunda chave de deslocamento, (válida para somente letras).")
        while True:
            chave2 = input("Por exemplo, '7913': ")
            if chave2.isdigit():
                break
            else:
                print("Por favor, digite apenas números para a chave.")

        print()
        texto_cifrado = cifra_de_locomocao_unitaria(texto_original, chave1, chave2)
        print("\nTexto cifrado:", texto_cifrado)
# -----------------------------------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------------------------------
    elif opcao == '3':
        print("A Cifra de Deslocamento Unitária é um tipo de cifra de substituição")
        print("que faz o uso de inúmeras Cifras de César.")
        time.sleep(0.2)
        print()
        print("Sobre a Cifra criada:")
        print()
        time.sleep(0.2)
        print("1. Nesta cifra, cada dígito do texto original é deslocado com um valor específico.")
        time.sleep(0.2)
        print("2. Tal valor específico, é determinado por duas chaves fornecidas pelo usuário.")
        time.sleep(0.2)
        print("3. Cada dígito do texto original é primeiro deslocado pelo valor da primeira chave.")
        time.sleep(0.2)
        print("4. Em seguida, o resultado é novamente deslocado pelo valor da segunda chave.")
        time.sleep(0.2)
        print()
        print("Como funciona:")
        print()
        time.sleep(0.2)
        print("1. Logo de início, inicia um looping sobre cada caractere do texto.")
        time.sleep(0.2)
        print("2. Se o texto digitado possuir um caractere acentuado ou símbolo, ele será mantido como está e ignorado.")
        time.sleep(0.2)
        print("3. Letras comuns maiúsculas são transformadas em minúsculas para uniformizar o processo.")
        time.sleep(0.2)
        print("4. Caso o texto possuir um dígito, apenas a primeira chave será aplicada a ele.")
        time.sleep(0.2)
        print("5. O resultado final é o texto cifrado.")
# -----------------------------------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------------------------------
    elif opcao == '4':
        print("Encerrando o programa...")
        time.sleep(1)
        os.system('cls')
        print("Programa encerrado.")
        break
# -----------------------------------------------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------------------------------------------
    else:
        print("Opção inválida...")
        time.sleep(0.5)
        print("Digite apenas 1, 2, 3 ou 4.")
        time.sleep(1)
        continue

    print()
    time.sleep(0.5)
# -----------------------------------------------------------------------------------------------------------------------



    continuar = input("Deseja voltar ao menu ou sair? (menu/sair): ")
    if continuar.lower() == "menu":
        os.system('cls')
        if opcao == '2':
            print("Texto cifrado anteriormente:", texto_cifrado)
            print("Primeira chave:", chave1)
            print("Segunda chave:", chave2)
            time.sleep(0.5)
        continue
    elif continuar.lower() == "sair":
        os.system('cls')
        print("Encerrando o programa...")
        time.sleep(1)
        os.system('cls')
        print("Programa encerrado.")
        break
    else:
        os.system('cls')
        print("Opção inválida...")
        time.sleep(0.5)
        print("Você será redirecionado ao menu.")
        time.sleep(1)
