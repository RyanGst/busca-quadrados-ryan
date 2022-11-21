import pygame, sys, recursos
from pygame.locals import QUIT

#################VARIAVEIS#######################
altura_janela = 300
largura_janela = 400
tamanho_quadrado = 50

inicio = None
fim = None

#M - lista para guardar os quadrados conhecidos porém não visitados
lista_aberta = []

linhas = int(altura_janela / tamanho_quadrado)
colunas = int(largura_janela / tamanho_quadrado)
quadrados = [[0 for x in range(linhas)] for y in range(colunas)]
print(quadrados)

########INICIALIZACAO#####################
pygame.init()
recursos.janela = janela = pygame.display.set_mode(
    (largura_janela, altura_janela))
pygame.display.set_caption('Projeto Aestrela')
recursos.font = font = pygame.font.SysFont(None, int(tamanho_quadrado / 4))

#####################################################

for x in range(0, colunas):
    for y in range(0, linhas):
        print("X:", x, "Y:", y)
        quadrados[x][y] = recursos.Quadrado(x, y, tamanho_quadrado)

#quadrado_teste = recursos.Quadrado(10, 10, tamanho_quadrado)
#quadrado_teste.verificado()


def cliqueQuadrado(event):
    global inicio
    global fim
    for x in range(0, colunas):
        for y in range(0, linhas):
            if (quadrados[x][y].rect.collidepoint(event.pos)):
                quadrado_clicado = quadrados[x][y]
                if (pygame.key.get_pressed()[pygame.K_LSHIFT]):
                    if (inicio != None):
                        inicio.caminho()

                    inicio = quadrado_clicado
                    quadrado_clicado.inicio()

                elif (pygame.key.get_pressed()[pygame.K_LCTRL]):
                    if (fim != None):
                        fim.caminho()
                    fim = quadrado_clicado
                    quadrado_clicado.fim()

                else:
                    quadrado_clicado.parede()


def encontraMenorF():
    menor = lista_aberta[0]
    for quadrado in lista_aberta:
        if (quadrado._f < menor._f):
            menor = quadrado
    return menor


#M - #########Função para busca de Caminho##########
def aEstrela():
    print("AESTTRELA")
    #M - chamando as variaveis globais para serem utilizadas dentro da funcao
    global inicio
    global fim
    global lista_aberta

    #########SEU CÓDIGO A PARTIR DAQUI-->
    #DEFINIR O QUADRADO INICIAL COM G = 0
    inicio.g = 0
    #ADICIONAR O QUADRADO INICIAL NA LISTA ABERTA
    """lista_aberta.append(inicio)"""
    lista_aberta.append(inicio)

    #ENQUANTO A LISTA ABERTA FOR MAIOR QUE ZERO(ITENS)
    while len(lista_aberta) > 0:
        """retorna quantos itens tem na lista -> print(len(lista_aberta))"""
        print("Lista aberta qtd: ", len(lista_aberta))

        ##BUSCAR QUAL QUADRADO POSSUI MENOR F
        ##SALVAR O QUADRADO EM UMA VARIÁVEL TEMPORARIA PARA FACILITAR O USO
        """
      para encontrar o menor f podem usar um for duplo (igual o que add os quadrados
      no vetor 'quadrados') OU usar alguma função lambda/operator que retorne o menor f
      """
        quadrado_atual = encontraMenorF()
        ##REMOVER O QUARADO ATUAL DA LISTA ABERTA (IMPORTANTE PARA NÃO FICAR EM LOOP ETERNO)
        lista_aberta.remove(quadrado_atual)

        ##VERIFICAR SE O QUADRADO ATUAL NÃO É IGUAL AO QUADRADO FIM
        """ALUNOS"""
        ##CHAMAR A FUNÇÃO '.verificado()' DO QUADRADO ATUAL
        quadrado_atual.verificado()

        #vetor auxiliar para encontrar os vizinhos
        vizinhos = [
            [0, -1],  #cima
            [0, 1],  #baixo
            [-1, 0],  #esquerda
            [1, 0]  #direita
        ]

        ##FOR PASSANDO POR TODOS OS VIZINHOS DO QUARADO ATUAL
        for vizinhoID in vizinhos:
            aux_X = quadrado_atual.x + vizinhoID[0]
            aux_Y = quadrado_atual.y + vizinhoID[1]

            if (aux_X < 0 or aux_X > colunas or aux_Y < 0 or aux_Y > linhas):
                print("Quadrado nao existe")
            else:
                quadrado_vizinho = quadrados[aux_X][aux_Y]

                ###VERIFICAR SE O VIZINHO NÃO É PAREDE E NÃO ESTÁ BLOQUEADO
                if (not quadrado_vizinho._parede
                        and not quadrado_vizinho._bloqueado):

                    ####CALCULAR A DISTANCIA DO VIZINHO ATÉ O FIM
                    """ALUNOS - - distancia_fim = abs(vizinho.x - fim.x) + abs(vizinho.y - fim.y)"""
                    """a distancia do inicio é o 'g' + 1 do quadrado atual """
                    ###CHAMAR A FUNÇÃO '.conhecido()' PASSANDO A DISTANCIA DO inicio DISTANCIA DO fim E O QUADRADO ATUAL
                    quadrado_vizinho.conhecido(10, 10, quadrado_atual)

                    ###ADICIONAR O VIZINHO NA LISTA ABERTA
                    """ALUNOS"""
                    lista_aberta.append(quadrado_vizinho)
                    pygame.display.update()
                    pygame.time.delay(500)


##########LAÇO PRINCIPAL########################
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            cliqueQuadrado(event)
        #M - verificar se tem alguma tecla 'down'
        if event.type == pygame.KEYDOWN:
            #M - verifica se é o ENTER e executa a função
            if event.key == pygame.K_RETURN:
                aEstrela()

    pygame.display.update()
