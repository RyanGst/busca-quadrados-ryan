import pygame

cor_base = (60, 179, 113)
cor_parede = (0, 0, 0)
cor_conhecido = (72, 209, 204)
cor_verificado = (255, 0, 0)
cor_inicio = (30, 144, 255)
cor_fim = (218, 165, 32)

cor_borda = (169, 169, 169)
cor_texto = (220, 220, 220)

espessura_borda = 2

janela = 0
font = 0


class Quadrado:
    #VÁRIAVEIS DO OBJETO QUADRADO###################
    x = 0
    y = 0
    tamanho = 0
    rect = -1
    pai = None

    #VÁRIAVEIS PRIVADAS#############################
    _f = -1
    _g = -1
    _h = 2

    _cor_atual = cor_base
    _parede = False
    _inicio = False
    _fim = False
    _bloqueado = False

    #MÉTODO CONSTRUTOR###############################
    def __init__(self, x, y, tamanho):
        self.x = x
        self.y = y
        self.tamanho = tamanho
        self.atualiza_quadrado()

    #OUTROS MÉTODOS###################################
    def atualiza_textos(self):
        img_f = font.render("F=" + str(self._f), True, cor_texto)
        img_g = font.render("G=" + str(self._g), True, cor_texto)
        img_h = font.render("H=" + str(self._h), True, cor_texto)
        janela.blits([
            (img_f, (self.rect.x + 2, self.rect.y + self.tamanho / 5 * 1)),
            (img_g, (self.rect.x + 2, self.rect.y + self.tamanho / 5 * 2)),
            (img_h, (self.rect.x + 2, self.rect.y + self.tamanho / 5 * 3))
        ])

    def atualiza_quadrado(self):
        self.rect = pygame.draw.rect(
            janela, self._cor_atual,
            pygame.Rect(self.x * self.tamanho, self.y * self.tamanho,
                        self.tamanho, self.tamanho))
        pygame.draw.rect(
            janela, cor_borda,
            pygame.Rect(self.x * self.tamanho, self.y * self.tamanho,
                        self.tamanho, self.tamanho), espessura_borda)
        self.atualiza_textos()

    def caminho(self):
        self._parede = False
        self._inicio = False
        self._fim = False
        self._cor_atual = cor_base
        self.atualiza_quadrado()

    def parede(self):
        self._parede = not self._parede
        if (self._parede):
            self._inicio = False
            self._fim = False
            self._cor_atual = cor_parede
            self.atualiza_quadrado()
        else:
            self.caminho()

    def conhecido(self, g, h, pai):
        if (not self._inicio and not self._fim):
            self._cor_atual = cor_conhecido
            self._g = g
            self._h = h
            self.pai = pai
            self.calculaF()

    def verificado(self):
        if (not self._inicio and not self._fim):
            self._bloqueado = True
            self._cor_atual = cor_verificado
        self.atualiza_quadrado()

    def inicio(self):
        self._inicio = True
        self._fim = False
        self._parede = False
        self._cor_atual = cor_inicio
        self.atualiza_quadrado()
      
    def fim(self):
        self._inicio = False
        self._fim = True
        self._parede = False
        self._cor_atual = cor_fim
        self.atualiza_quadrado()

    #GETTERS E SETTERS##############################
    def calculaF(self):
        if (self._g > 0 and self._h > 0):
            self._f = self._g + self._h

        self.atualiza_quadrado()

    @property
    def g(self):
        print("Geter de G: ", self._g)
        return self._g

    @g.setter
    def g(self, g):
        self._g = g
        print("Setter de G", g)
        self.calculaF()

    @property
    def h(self):
        print("Geter de H: ", self._h)
        return self._h

    @h.setter
    def h(self, h):
        self._h = h
        print("Setter de H", h)
        self.calculaF()
