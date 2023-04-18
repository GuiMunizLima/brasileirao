'''
J = Jogos
V = Vitórias
E = Empate
D = Derrotas
GP = Gols Pró
GC = Gols Contras
SG = Saldo de Gols
'''

#Função para obter o resultado da partida
def Partida(gols1, gols2, primeiro_time, segundo_time, times, pontos):
    times1 = primeiro_time
    times2 = segundo_time
    SG1 = gols1 - gols2
    SG2 = gols2 - gols2

    #Para poder separar os times e somar os pontos, gols, saldos de gols, vitorias, derrotas, empate
    if times1 in times and times2 in times:
        time1 = times[times1]
        time2 = times[times2]

        #if para ver se o time de casa ganhou
        if gols1 > gols2:
            time1[2] += 1
            time1[0] += 3
            pontos += 3
            time2[4] += 1
            time1[9] += '⭕'
            time2[9] += '❌'

        #if para ver se o time de fora ganhou    
        elif gols2 > gols1:
            time2[2] += 1
            time2[0] += 3
            pontos += 3
            time1[4] += 1
            time2[9] += '⭕'
            time1[9] += '❌'

        #if para ver se os times empataram     
        elif gols1 == gols2:
            time1[3] = 1
            time2[3] = 1
            time1[0] += 1
            time2[0] += 1
            time1[9] += '➖'
            time2[9] += '➖'

        #Gols feitos na partida por cada time
        time1[5] += gols1
        time2[5] += gols2

        #Gols tomado na partida por cada time
        time1[6] += gols2
        time2[6] += gols1

        #Saldo de gols na partida de cada time
        time1[7] += SG1
        time2[7] += SG2

        #A soma de jogos de cada time por partida
        time1[1] += 1
        time2[1] += 1

    return times, pontos

#Função para obter o atual time na liderança do brasileirão
def Ranking_Brasileirao(times):
    print('-' * 119)
    print(f'{classificacao:<38}|  P   |  J   |  V   |  E   |  D   |  GP  |  GC  |  SG  |  %  |  ÚLTIMOS JOGOS  |')
    print('-' * 119)

    
    lider = 0
    pontuacoes = []

    #Saber quem esta com a maior pontuação
    for chave, valor in times.items():
        ponto = valor[0]
        if ponto > lider:
            lider = ponto
            lider += 1

    #Pegar o maior 
    while lider >= 0:
        lider -= 1
        for chave, valor in times.items():
            ponto_max = times[chave]
            ponto_max = ponto_max[0]
            if ponto_max == lider:
                print(f'{chave:<38}|  {valor[0]:<4}|  {valor[1]:<4}|  {valor[2]:<4}|  {valor[3]:<4}|  {valor[4]:<4}|  {valor[5]:<4}|  {valor[6]:<4}|  {valor[7]:<4}|  {valor[8]}  |{valor[9]:<7}')
                print('-' * 119)

classificacao = 'CLASSIFICAÇÃO'
pontos = 10
times = {'América-MG': [0,0,0,0,0,00,00,00,0,''],'Athletico-PR': [0,0,0,0,0,00,00,00,0,''],'Atlético-MG': [0,0,0,0,0,00,00,00,0,'']
         ,'Bahia': [0,0,0,0,0,00,00,00,0,''],'Botafogo': [0,0,0,0,0,00,00,00,0,''],'Bragantino': [0,0,0,0,0,00,00,00,0,'']
         ,'Chapecoense': [0,0,0,0,0,00,00,00,0,''],'Corinthians': [0,0,0,0,0,00,00,00,0,''],'Coritiba': [0,0,0,0,0,00,00,00,0,'']
         ,'Cruzeiro': [0,0,0,0,0,00,00,00,0,''],'Cuiabá': [0,0,0,0,0,00,00,00,0,''],'Flamengo': [0,0,0,0,0,00,00,00,0,'']
         ,'Fluminense': [0,0,0,0,0,00,00,00,0,''],'Fortaleza': [0,0,0,0,0,00,00,00,0,''],'Goiás': [0,0,0,0,0,00,00,00,0,'']
         ,'Grêmio': [0,0,0,0,0,00,00,00,0,''],'Internacional': [0,0,0,0,0,00,00,00,0,''],'Palmeiras': [0,0,0,0,0,00,00,00,0,'']
         ,'Santos': [0,0,0,0,0,00,00,00,0,''],'São_Paulo': [0,0,0,0,0,00,00,00,0,''],'Vasco': [0,0,0,0,0,00,00,00,0,'']}

print('-' * 119)
print(f'{classificacao:<38}|  P  |  J  |  V  |  E  |  D  |  GP  |  GC  |  SG  |  %  |  ÚLTIMOS JOGOS  |')
print('-' * 120)
for time, pontuacao in times.items():
    print(f'{time:<38}|  {pontuacao[0]}  |  {pontuacao[1]}  |  {pontuacao[2]}  |  {pontuacao[3]}  |  {pontuacao[4]}  |  {pontuacao[5]:<4}|  {pontuacao[6]:<4}|  {pontuacao[7]:<4}|  {pontuacao[8]}  |')
    print('-' * 119)

continuar = ''
while continuar != 'NÃO':
    print('Exemplo de como digitar o placar: Flamengo 2 a 1 Vasco')
    jogo = input('JOGO: ').split(' ', 4)
    gols1 = int(jogo[1])
    gols2 = int(jogo[3])

    Partida(gols1, gols2, jogo[0], jogo[4], times, pontos)
    Ranking_Brasileirao(times)

    continuar = input('Continuar? ')
