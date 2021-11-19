# Projeto Módulo 1 [T12] Resília

# Autor: Gabriel Kanarski
# Development: 09/11/2021 - 19/11/2021


#   FUNÇÕES

def inputLetra():
    escolhaABC = input('Insira A, B ou C como opção:   ')
    escolhaABC = str.upper(escolhaABC)
    if escolhaABC == 'A':
        print('Você escolheu a alternativa: ', escolhaABC)
        return escolhaABC
    elif escolhaABC == 'B':
        print('Você escolheu a alternativa: ', escolhaABC)
        return escolhaABC
    elif escolhaABC == 'C':
        print('Você escolheu a alternativa: ', escolhaABC)
        return escolhaABC
    else:
        print('Alternativa inválida.')
        return inputLetra()

def inputMenu():
    print('\nOlá. \nEu sou Aziz, seu assistente virtual. Vou interagir com você e direcioná-lo às suas escolhas.\n\nQuer tentar a sorte jogando? \nDigite (S) para sim ou (N) para não.\n')
    escolhaMenu = input('Você escolheu:  ')
    escolhaMenu = str.upper(escolhaMenu)
    if escolhaMenu == str('S'):
        print('Legal. É muito bom ter você por aqui.\nEntão vamos lá.')
        escolhaMenu = 1
        return escolhaMenu 
    elif escolhaMenu == str('N'):
        print('Que pena. Se futuramente mudar de idéia, estarei aqui.\nAté logo.')
        exit()
    else:
        print('Alternativa inválida.')
        return inputMenu('Insira apenas Sim (S) ou Não (N): ')

def escolhaDoPersonagem():
    print('Agora escolha o personagem com o qual jogará:\n\n (A)  Anny\n (B)  Bart\n (C)  Chloe\n')
    escolhaPersonagem = input('Insira A, B ou C como opção:   ')
    escolhaPersonagem = str.upper(escolhaPersonagem)
    if escolhaPersonagem == str('A'):
        print('Legal. Você estará na pele de Anny, nossa agente de negociações.')
        return escolhaPersonagem
    elif escolhaPersonagem == str('B'):
        print('Legal. Você estará na pele de Bart, pai da vítima sequestrada.')
        return escolhaPersonagem
    elif escolhaPersonagem == str('C'):
        print('Legal. Você estará na pele de Chloe, a sequestradora.')
        return escolhaPersonagem
    else:
        print('Alternativa inválida.')
        return escolhaDoPersonagem()