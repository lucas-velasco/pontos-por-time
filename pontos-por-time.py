'''Pontos por time

Faça uma função chamada pontos_por_time que receba uma lista de dois elementos, onde cada elemento é também uma lista. A lista completa tem informações do número de 
gols em dois jogos de futebol entre dois times (jogo da ida e jogo da volta), no seguinte formato: [['Cormengo'. 'Flaminthians', [10]]. [Flaminthians'. 'Cormengo', 
[2. 2]]]. Nesta lista de exemplo, no primeiro jogo entre Cormengo e Flaminthians, o Cormengo fez 1 gol e o Flaminthians não fez gol Sua função deve retornar um 
dicionário cujos mapeamentos são: <nome do time>> <numero total de poritos na fase>. Os pontos de um time na fase são calculados da seguinte forma: em cada jogo, 
os times recebem três pontos por vitória e um ponto por empate. Não são atribuídos pontos para derrotas. O total de pontos de uma fase é a soma de pontos dos dois 
jogos da fase. Na lista de exemplo, o total de pontos do Cormengo é 4 e do Flaminthians é 1.'''


def pontos_por_time(jogos):
    '''A função retorna um dicionário com o nome dos times e suas pontuações finais'''
    ida, volta= jogos   
    t1=ida[0]
    t2=ida[1]
    ida_pontos=ida[2]
    volta_pontos=volta[2]
    pontuacao={t1:0,t2:0}
    
    if ida_pontos[0]>ida_pontos[1]:
        pontuacao[t1]+=3
    elif ida_pontos[0]==ida_pontos[1]:
        pontuacao[t1]+=1
        pontuacao[t2]+=1
    else:
        pontuacao[t2]+=3
    if volta_pontos[0]>volta_pontos[1]:
        pontuacao[t2]+=3
    elif volta_pontos[0]==volta_pontos[1]:
        pontuacao[t1]+=1
        pontuacao[t2]+=1
    else:
        pontuacao[t1]+=3
    return {t2:pontuacao[t2], t1:pontuacao[t1]}
