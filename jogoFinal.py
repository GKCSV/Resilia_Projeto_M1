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
        return inputMenu()

def annyFaseUmApresentacao():
    print('Anny é uma agente federal de negociação. Ela possui 10 anos de carreira e é a melhor desta região.')
    print('Certo dia, Anny foi requisitada para uma operação de negociação, onde um indivíduo havia sido sequestrado. A sequestrador, em posse do indivíduo, estava solcitatando um pagamento para libertá-lo e, caso não fosse atendida sua solicitação, o mesmo mataria a vítima.')
    print('Sendo assim, Anny preparou seus equipamentos e seguiu até Adventure\'s Park para iniciar a negociação com o sequestrador.')
    print('Chegando ao parque, Anny seguiu para o local da negociação, onde havia várias pessoas e autoridades locais.')
    print('Para sua surpresa, ninguém possuia qualquer prova de que o sequestrador estava de fato com a vítima.')
    print('Sendo assim, Anny decidiu tirar a prova real.\n')
    print('Fase 1:\n\nComo Anny deverá proceder para confirmar se a vítima existe?')
    print('Opção A: Pedir para o sequetrador mostrar a vítima na janela\nOpção B: Pedir para o sequestrador entregar 1 (um) dedo da vítima para leitura da digital\nOpção C: Solicitar informações pessoais da vítima')
    
def annyFaseUmExecucao():
    annyUm = inputLetra()
    if annyUm == 'A':
        print('O sequestrador negou sua solicitação.\n\nGAME OVER\n\nMais sorte na próxima.')
        return exit()
    elif annyUm == 'B':
        print('O sequestrador acabou enviando a cabeça da vítima.\n\nGAME OVER\n\nMais sorte na próxima.')
        return exit()
    elif annyUm == 'C':
        print('Ótimo. O sequestrador jogou a carteira da vítima pela janela.\n')
        print('Você passou de fase! Vamos para a próxima')
        annyI = int(1)
        return annyI
    else:
        return inputLetra(input('Insira apenas A, B ou C: '))
                
def annyFaseDoisApresentacao():
    print('Agora Anny precisa verificar se os documentos fornecidos.')
    print('Com uma equipe especializada de prontidão, Anny solicita a verificação da documentação.')
    print('A equipe então inicia a verificação.')
    print('\n\n\"Verificação concluida com sucesso\"')
    input('Pressione Enter para continuar: ')
    print('Com os dados verificados, Anny questiona o sequestrador sobre a possibilidade de trocar o refém por algo do seu interesse.')
    print('O sequestrador então solicita que poderá trocá-lo por um helicóptero com piloto.\n')
    print('\n Fase 2:\n\n Anny deverá decidir se atende ou não.\n')

def annyFaseDoisExecucao():
    annyDois = input('Opção A: Atender a solicitação\nOpção B: Negar a solicitação\nOpção C: Solicitar a um atirador de elite que abata o sequestrador')
    annyDois = str.upper(annyDois)
    if annyDois == 'A':
        print('Ótimo. O sequestrador está aguardando a chegada do helicóptero.')
        print('Você passou de fase! Vamos para a próxima')
        annyII = int(2)
        return annyII
    elif annyDois == 'B':
        print('Como você negou a solicitação do sequestrador, ele matou a vítima.\n\nGAME OVER\n\nMais sorte na próxima.')
        return exit()
    else:
        print('O atirador de elite errou o alvo e acertou a vítima que veio a óbito instantaneamente.\n\nGAME OVER\n\nMais sorte na próxima.')
        return exit()

def annyFaseTresApresentacao():
    print('Agora Anny precisa fazer com que a vítima fique viva.')
    print('Sendo assim, ela avisa ao sequestrador que o helicóptero chegará em 10 minutos.')
    print('Anny então deverá tomar a decisão final do caso.')
    print('\n Fase 2:\n\n Anny deverá finalizar este caso O que ela poderá fazer?.\n')

def annyFaseTresExecucao():
    annyTres = input('Opção A: Aguardar a chegada do helicóptero para a troca pela vítima\nOpção B: Tentar outra solução\nOpção C: Prender o sequestrador no momento da libertação do refém')
    annyTres = str.upper(annyTres)
    if annyTres == 'A':
        print('O sequestrador libertou o refém, mas fugiu.\n\nGAME OVER\n\nMais sorte na próxima.')
        return exit()
    elif annyTres == 'B':
        print('O sequestrador não quis outra solução e matou a vítima.\n\nGAME OVER\n\nMais sorte na próxima.')
        return exit()
    else:
        print('O refém foi liberado e o sequestrador foi preso.')
        print('Mais um caso solucionado pela melhor agente!')
        print('\nParabéns.\nVocê conseguiu libertar o refém e chegou ao fim deste mini-game.\n\n Obrigado pela participação.')
        return exit()

def bartFaseUmApresentacao():
    print('Bart é um empresário de sucesso.')
    print('Certo dia, seu filho não estava na cama como de costume.')
    print('Achando aquilo muito estranho, tentou contato com o filho pelo celular.')
    print('Porém não houve êxito.')
    print('Sendo assim, Bart procurou a delegacia de polícia imediatamente.')
    print('Ele explicou a situação aos agentes.')
    print('O agente registrou a ocorrência, entregou alguns panfletos de como agir em caso de desaparecimento e pediu para aguardar ali.')
    print('Enquanto aguardava, recebeu uma ligação do sequestrador. Este lhe pedia a quantida de R$ 100 mil pelo resgate.')
    print('Fase 1: Como Bart deverá proceder?')

def bartFaseUmExecucao():
    bartUm = input('\n\nOpção A: Pedir para os agentes agirem logo\nOpção B: Pedir para falar com o filho\nOpção C: Concordar com o sequestrador para ganhar tempo')
    bartUm = str.upper(bartUm)
    if bartUm == 'A':
        print('A ação dos agente causou alarde. Seu filho foi morto pelo sequestrador.\n\nGAME OVER\n\nMais sorte na próxima.')
        return exit()
    elif bartUm == 'B':
        print('O sequestrador negou sua solicitação e não fez mais contato. Seu filho está desaparecido desde então.\n\nGAME OVER\n\nMais sorte na próxima.')
        return exit()
    else:
        print('O sequestrador pediu que Bart aguardasse mais instruções\n')
        print('Você passou de fase! Vamos para a próxima')
        bartUm = str('1')
        bartUm = int(bartUm)
        return bartUm
    
def bartFaseDoisApresentacao():
    print('Após os agentes terem contactado a agente de negociações, Bart aguarda nova ligação do criminoso')
    print('Dentro de 20 minutos o sequestrador fez contato novamente.')
    print('Ele solicitou que o dinheiro fosse entregue a um parceiro do outro lado da cidade.')
    print('Fase 2:\n\n O que Bart deverá fazer?')

def bartFaseDoisExecucao():
    bartDois = input('\n\nOpção A: Falar que não tem o dinheiro\nOpção B: Falar que está com o dinheiro e marcar de fazer a troca pelo filho\nOpção C: Pedir ao banco empréstimo do dinheiro e marcar de fazer a troca pelo filho')
    bartDois = str.upper(bartDois)
    if bartDois == 'A':
        print('Se não tem grana como vai negociar? Seu filho está morto. \n\nGAME OVER\n\nMais sorte na próxima.')
        return exit()
    elif bartDois == 'B':
        print('O sequestrador está lhe fornecendo o endereço para entregar o dinheiro e o endereço para pegar o filho.')
        print('Você passou de fase! Vamos para a próxima')
        bartDois = str('2')
        bartDois = int(bartDois)
        return bartDois
    else:
        print('O sequestrador está lhe fornecendo o endereço para entregar o dinheiro e o endereço para pegar o filho.')
        print('Você passou de fase! Vamos para a próxima')
        bartDois = str('2')
        bartDois = int(bartDois)
        return bartDois

def bartFaseTresApresentacao():
    print('Após o fornecimento dos endereços, uma equipe de polícia disfarçada acompanhou Bart até o endereço do pagamento do resgate.')
    print('Enquanto isso, a agente de negociações Anny e a esposa de Bart seguiram para o endereço de entrega do refém, que era dentro do Adventure\s Park')
    print('Enquanto Anny trabalhava, Bart teria que agir conforme combinado para trazer seu filho para casa a salvo')
    print('Fase 3: A saída que Bart tem é concordar com o pagamento do resgate até Anny conseguir uma negociação. Como ele deve proceder?')

def bartFaseTresExecucao():
    bartTres = input('\n\nOpção A: Aguardar Anny ter uma solução\nOpção B: Entregar a maleta vazia esperando que o filho seja libertado.\nOpção C: Entregar a maleta com o dinheiro esperando que o filho seja libertado..')
    bartTres = str.upper(bartTres)
    if bartTres == 'A':
        print('Anny derrubou o criminoso e seu filho foi lebertado.')
        print('\nParabéns.\nSeu filho voltou para casa e você chegou ao fim deste mini-game.\n\n Obrigado pela participação.')
        return exit()
    elif bartTres == 'B':
        print('O criminoso descobriu que a maleta estava vazia. O filho de Bart está morto.\n\nGAME OVER\n\nMais sorte na próxima.')
        return exit()
    else:
        print('Você pagou o resgate e libertou seu filho. Porém, os R$ 100 mil eram emprestados do banco. De qualquer maneira você está morto.\n\nGAME OVER\n\nMais sorte na próxima.')
        return exit()

def chloeFaseUmApresentacao():
    print('Chloe é uma ex-agente do governo federal. Atuou por 17 anos em cargo público.')
    print('Após sua demissão inesperada por motivos políticos, ela iniciou uma trama para vingar-se de quem a prejudicou.')
    print('Seu primeiro passo foi monitorar a família de seu inimigo.')
    print('Qual a primeira ação que Chloe deverá executar?')
    
def chloeFaseUmExecucao():
    chloeUm = input('Opção A: Executar um atentado contra a família.\nOpção B: Sequestrar um dos membros.\nOpção C: Derrubar o adversário por corrupção no governo.')
    chloeUm = str.upper(chloeUm)
    if chloeUm == 'A':
        print('A')
        return exit()
    elif chloeUm == 'B':
        print('B')
        return exit()
    else:
        print('C')
        print('Você passou de fase! Vamos para a próxima')
        chloeUm = str('1')
        chloeUm = int(chloeUm)
        return chloeUm

def chloeFaseDoisApresentacao():
    print('chloeFaseDoisApresentacao')
    print('chloeFaseDoisApresentacao')
    print('chloeFaseDoisApresentacao')
    print('chloeFaseDoisApresentacao')
    print('chloeFaseDoisApresentacao')
    print('chloeFaseDoisApresentacao')
    print('chloeFaseDoisApresentacao')

def chloeFaseDoisExecucao():
    chloeDois = input('')
    chloeDois = str.upper(chloeDois)
    if chloeDois == 'A':
        print('RespostachloeFaseDoisApresentacao\n')
        return exit()
    elif chloeDois == 'B':
        print('RespostachloeFaseDoisApresentacao\n')
        print('Você passou de fase! Vamos para a próxima')
        chloeDois = str('2')
        chloeDois = int(chloeDois)
        return chloeDois
    else:
        print('RespostachloeFaseDoisApresentacao')
        return exit()

def chloeFaseTresApresentacao():
    print('chloeFaseTresApresentacao')
    print('chloeFaseTresApresentacao')
    print('chloeFaseTresApresentacao')
    print('chloeFaseTresApresentacao')
    print('chloeFaseTresApresentacao')
    print('chloeFaseTresApresentacao')
    print('chloeFaseTresApresentacao')
        
def chloeFaseTresExecucao():
    chloeTres = input('')
    chloeTres = str.upper(chloeTres)
    if chloeTres == 'A':
        print('RespostachloeFaseTresApresentacao')
        return exit()
    elif chloeTres == 'B':
        print('RespostachloeFaseTresApresentacao')
        return exit()
    else:
        print('RespostachloeFaseTresApresentacao')
        return exit()


#   VARIÁVEIS:

start = ''
escolhaABC = ''
escolhaMenu = ''
escolhaPersonagem = ''
anny = str.upper('')
annyUm = int()
annyDois = int()
annyTres = int()
bart = str.upper('')
bartUm = int()
bartDois = int()
bartTres = int()
chloe = str.upper('C')
chloeUm = int()
chloeDois = int()
chloeTres = int()



########   Execução:    ########

#   INÍCIO:
start = str.upper(input('WELCOME TO ADVETURE\'S PARK\n\n\nPressione Enter para continuar\n'))

if  start == str(''):
    inputMenu()
    print('Agora escolha o personagem com o qual jogará:\n\n (A)  Anny\n (B)  Bart\n (C)  Chloe\n')
    escolhaPersonagem = input('Insira A, B ou C como opção:   ')
    escolhaPersonagem = str.upper(escolhaPersonagem)
    if escolhaPersonagem == str('A'):
        print('Legal. Você estará na pele de Anny, nossa agente de negociações.')
        annyFaseUmApresentacao()
        annyFaseUmExecucao()
        annyFaseDoisApresentacao()
        annyFaseDoisExecucao()
        annyFaseTresApresentacao()
        annyFaseTresExecucao()
    elif escolhaPersonagem == str('B'):
        print('Legal. Você estará na pele de Bart, pai da vítima sequestrada.')
        bartFaseUmApresentacao()
        bartFaseUmExecucao()
        bartFaseDoisApresentacao()
        bartFaseDoisExecucao()
        bartFaseTresApresentacao()
        bartFaseTresExecucao()
    elif escolhaPersonagem == str('C'):
        print('Legal. Você estará na pele de Chloe, a sequestradora.')
        chloeFaseUmApresentacao()
        chloeFaseUmExecucao()
        chloeFaseDoisApresentacao()
        chloeFaseDoisExecucao()
        chloeFaseTresApresentacao()
        chloeFaseTresExecucao()
else:
    start = input('Alternativa inválida. Escolha \'S\' ou \'N\':  ')
        
    
        

        