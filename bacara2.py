#EP - Desing de Software
#Equipe: Pedro Henrique Britto Aragão Andrade
#Data:18/10/2020
#oi
import random
from random import shuffle 

#quantidades de fichas inicialmente
fichas= 1000

controle= True
controle2= True
controle3= True
while controle:
#se o usuário não possuir mais fichas ele entra nessa condição e perde o jogo. 
    if fichas<= 0:
        print ('Que pena você zerou a banca!')
        break
#forma o baralho que será usado no jogo e pergunta quantos baralhos será usado
    while controle2:
        n= int(input('Quantos baralhos você quer usar (1, 6 ou 8) ? '))
        numero= [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]
        baralho= (numero*4)*n
    #caso o uduário ponha um número de baralhos que não exista o programa irá reclamar e mandar escolher outra quantidade de baralhos
        if n!= 1 and n!= 6 and n!= 8:
            print ('não existe esse número de baralhos.')
        else:
            controle2= False
    else:    
    #transforma as fichas em inteiro.
        fichas= int(fichas)
    #i é um contador para entregar as cartas.
        i=0
    #o programa irá falar quantas fichas o usuário tem naquele momento e depois pergunta quantas fichas ele(a) quer apostar.
        print ('Você possui {0} fichas.'. format(fichas))
        aposta= int(input('Quantas fichas você quer apostar ? '))
    #caso o que o usuário queira apostar mais fichas do que possui ele(a) entrará nessa condição e o programa irá dizer que possui fichas insuficientes.
        if aposta>fichas or aposta<0:
            print ('fichas insuficientes')
    #caso o usuário aposte zero o jogo acaba e fala quantas fichas ele(a) terminou.
        elif aposta== 0:
            print ('Fim de jogo você terminou com {0} fichas.'. format(fichas))
            break
        else:
            #o programa pergunta em quem o jogador quer apostar.    
            while True:
                aonde= input('Em quem você quer apostar (banco/jogador/empate) ? ')
                if aonde!= 'banco' and aonde!= 'jogador' and aonde!= 'empate':
                    print ('Desculpa, não entendi a sua resposta!')
                else:
                    break
        #o programa irá embaralhar as cartas.
            random.shuffle(baralho)
            print (baralho)
        #o programa vai entregar as cartas para o jogador e para o banco (utilizando o contador i).
            primeira_carta= baralho[i]
            i+= 1
            segunda_carta= baralho[i]
            i+= 1

            terceira_carta= baralho[i]
            i+= 1
            quarta_carta= baralho[i]
            i+= 1
        #o programa irá somar as cartas do jogador e da mesa.
            soma_do_jogador= primeira_carta + segunda_carta
            soma_da_banca= terceira_carta + quarta_carta

        #caso nem o banco e nem o jogador tiverem, na soma, 8 ou 9 eles entrarão nos while e receberão novas cartas.
            while soma_do_jogador!=8 and soma_do_jogador!=9 and soma_da_banca!= 8 and soma_da_banca!= 9:
                if soma_do_jogador<=5:
                    quinta_carta= baralho[i]
                    i+= 1
                    soma_do_jogador+= quinta_carta
                elif soma_do_jogador>= 10:
                    a= str(soma_do_jogador)
                    b= a[1]
                    soma_do_jogador= int(b)
                elif soma_da_banca<=5:
                    sexta_carta= baralho[i]
                    i+= 1
                    soma_da_banca+= sexta_carta
                elif soma_da_banca>=10:
                    a= str(soma_da_banca)
                    b= a[1]
                    soma_da_banca= int(b)
                else:
                    break
        
        #caso o jogador tenha apostado nele mesmo ele(a) entra nessa condição.    
            if aonde=='jogador':
            #caso tenha apostado certo o programa entra nessa condição e o jogador ganha as fichas.
                if soma_do_jogador>soma_da_banca:
                    fichas+= aposta 
                    print ('parabens você ganhou!')
                #irá descontar, do que o jogador ganhou, a comissão do cassino.
                    if n== 1:
                        fichas-= aposta*0.0129
                    elif n== 6:
                        fichas-= aposta*0.0124
                    elif n== 8:
                        fichas-= aposta*0.0124
            #caso tenha apostado errado o programa entra nessa condição e o jogador perde as fichas apostadas.
                elif soma_da_banca>soma_do_jogador:
                    fichas-= aposta
                    print ('Você perdeu, o banco ganhou!') 
                else:
                    fichas-= aposta
                    print ('Você perdeu, deu empate!')
        
        #caso o jagador tenha apostado no banco ele(a) entra nessa condição.
            elif aonde== 'banco':
            #caso tenha apostado certo o programa entra nessa condição e o jogador ganha as fichas.
                if soma_da_banca>soma_do_jogador:
                    fichas= fichas + (aposta*0.95)
                    print ('parabens você ganhou!')
                #irá descontar, do que o jogador ganhou, a comissão do cassino.
                    if n== 1:
                        fichas-= aposta*0.0101
                    elif n== 6:
                        fichas-= aposta*0.0106
                    elif n== 8:
                        fichas-= aposta*0.0106
            #caso tenha apostado errado o programa entra nessa condição e o jogador perde as fichas apostadas.
                elif soma_do_jogador>soma_da_banca:
                    fichas-= aposta
                    print ('Você perdeu, o jogador ganhou!')
                else:
                    fichas-= aposta
                    print ('Você perdeu, deu empate!')
        
        #caso o jogador tenha apostado em empate ele(a) entra nessa condição.
            elif aonde == 'empate':
            #caso tenha apostado certo o programa entra nessa condição e o jogador ganha as fichas.
                if soma_da_banca==soma_do_jogador:
                    fichas= fichas + (8*aposta)
                    print ('parabens você ganhou!')
                #irá descontar, do que o jogador ganhou, a comissão do cassino.
                    if n== 1:
                        fichas-= aposta*0.1575
                    elif n== 6:
                        fichas-= aposta*0.1444
                    elif n== 8:
                        fichas-= aposta*0.1436
                elif soma_do_jogador>soma_da_banca:
                    fichas-= aposta
                    print ('Você perdeu, o jogador ganhou!')
            #caso tenha apostado errado o programa entra nessa condição e o jogador perde as fichas apostadas.
                else:
                    fichas-= aposta
                    print ('Você perdeu, o banco ganhou!')
        
        #o programa irá perguntar se o jogador quer continuar ou não.
            while fichas>0:
                d= input('Você quer continuar jogando (sim/não) ? ')
            #caso digite sim entra nessa condição.
                if d== 'sim':
                    break
            #caso digite não entra nessa condição.    
                elif d== 'não':
                #tranforma as fichas em um numero inteiro
                    fichas= int(fichas)
                    print ('Até a próxima! \nVocê terminou com {0} fichas.'. format(fichas))
                    controle= False
                    break
            #caso o jogador escreva qualquer coisa entra nessa condição.
                else:
                    print ('Desculpa, não entendi a sua resposta!')
        #irá "reativar" o while de quantas cartas o usuário deseja usar.
            controle2= True