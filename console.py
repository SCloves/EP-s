#############################################################
#                                                           #
#  MAC0122 Princípos de Desenvolvimento de Algoritmos       #
#                                                           #
#  MÓDULO console.py                                        #
#                                                           #
#  Módulo responsável pela animação.                        #
#                                                           #
#  Não altere nada neste arquivo.                           #
#                                                           #
#  Não altere o nome do arquivo.                            #
#                                                           #     
#  A documentação sobre "Turtle graphic for Tk" pode ser    #
#  vista em http://docs.python.org/3/library/turtle.html    #
#                                                           #
#############################################################

# módulo responsável pela animação
import turtle

#-------------------------------------------------------------
# constantes referentes aos pontos e linhas

# define a cor de cada ponto
COR_PONTO = "white"

# define o diâmetro de cada ponto
DIAMETRO_PONTO = 3 # hmmm, este diâmetro é um chute.

# define a cor 'default' das linhas
COR_LINHA = "yellow"

# define cor de fundo da janela
COR_FUNDO = "black"

# título da janela
TITULO = "MAC0122 2016 - Par Mais Próximo"

# parâmetros para o tracer (são chutes)
TRACER_RAPIDO  = 500
TRACER_DEFAULT = 3

# delay para desenhar
DELAY_DEFAULT = 5
DELAY_MIN = 1

#--------------------------------------------------------------
class Console:
    #----------------------------------------------------------
    def __init__(self, l_pontos, cantos):
        '''(Console, list, list) -> None

        Recebe uma referência `self` para um objeto Console, uma 
        lista com as coordenadas de pontos `l_pontos` e uma lista 
        `cantos` com as coordenadas de dois pontos.

        Cada ponto é representado por uma lista [x,y] em que x e y
        são números inteiros.

        Se cantos = [[x_min,y_min],[x_max,y_max]], então [x_min,y_min] 
        é a coordenada do ponto no canto inferior esquerdo e 
        [x_max,y_max] é a coordenada do ponto superior direito 
        da região retangular do plano que contém os pontos em l_pontos.
        Desta forma, se l_pontos[i] = [x,y], então 

           x_min <= x < x_max   e   y_min <= y < y_max

        '''
        # crie o atributo de estado com os pontos
        # AVISO: self.l_pontos é um apelido, não um clone
        self.l_pontos = l_pontos

        # crie o atributo de estado com a dimensão da região
        # AVISO: self.cantos é um apelido, não um clone
        self.cantos = cantos

        # crie um contador para o número de chamadas do método desenhe_linha
        self.no_linhas = 0

        # crie o atributo de estado do console
        self.canvas = turtle.Screen()

        # crie o atributo de estado com a 'pena' para desenharmos na janela
        self.pena = turtle.Turtle()

        # prepara a janela, pena, etc.
        self.setup()
        
        # desenhe os pontos
        self.desenhe_pontos()

    #----------------------------------------------------------
    def setup(self):
        '''(Console) -> None

        Recebe uma referência self para um objeto Console e faz as
        definições iniciais da janela e pena.
        '''
        # apelidos
        cantos = self.cantos
        canvas = self.canvas
        pena   = self.pena

        # (volta) pena para valores default
        # necessário quando não é primeira chamada para setup() 
        pena.reset()
        
        # não queremos que a tartaruga seja vista
        pena.hideturtle()        
        
        # defina a cor de fundo da janela
        canvas.bgcolor(COR_FUNDO)

        # coloque um título na barra superior da janela
        canvas.title(TITULO)

        # a janela representará uma região retangular do plano cartesiano que
        # tem o canto inferior esquerdo na coordenada [x_min,y_min] e
        # tem o canto superior direito  na coordenada [x_max,y_max].
        x_min, y_min = cantos[0]
        x_max, y_max = cantos[1]

        # fixe a área do janela
        canvas.setworldcoordinates(x_min,y_min,x_max,y_max)

        # vamos agora diminuir o valor do argumento de tracer 
        canvas.tracer(TRACER_DEFAULT)

        # volte o delay para o default
        canvas.delay(DELAY_DEFAULT)

        # definimos o tamanho da janela em pixels?
        # hmmm, será que é bom fixar?!
        # os valores default são uma porcentagem da tela: 
        #
        #      width  == 0.5  que corresponde a 50% da largura da tela
        #      height == 0.75 que corresponde a 75% da altura  da tela
        # 
        # se os valores de width e height forem inteiros, então 
        # eles são considerados como sendo número de pixels.
        # Por exemplo:
        # 
        #    width  = 800
        #    height = 675
        #
        # depois basta fazermos 
        #
        #    canvas.setup(width,height)
        #
        # hmmm, vamos deixar width e height variáveis em função da tela 
        # do computador, ok?!
        # width  = canvas.window_width()
        # height = canvas.window_height()


    #----------------------------------------------------------
    def desenhe_pontos(self):
        '''(Console) -> None

        Recebe um referência self a um objeto Console e desenha 
        os pontos do console na janela.
        '''
        # apelidos 
        canvas   = self.canvas   # janela e 
        l_pontos = self.l_pontos # lista de pontos
        pena     = self.pena     # pena

        # levante a pena para não deixar rastros na janela
        pena.penup()  
        
        # delay para desenhar os pontos na janela mais rapidamente
        canvas.delay(DELAY_MIN)

        # aumentando o valor do argumento de tracer tornamos
        # o surgimento dos pontos na janela aparentemente instantâneo
        canvas.tracer(TRACER_RAPIDO)

        # pegue o número de pontos na lista
        n = len(l_pontos)

        # desenhe os pontos
        for i in range(n):
            # pegue coordenadas do ponto i
            x, y = l_pontos[i]
            
            # vá para está a posição do pontos 
            pena.setpos(x,y)

            # desenhe o ponto
            pena.dot(DIAMETRO_PONTO,COR_PONTO)

        # vamos agora diminuir o valor do argumento de tracer 
        canvas.tracer(TRACER_DEFAULT)

        # volte o delay para o default
        canvas.delay(DELAY_DEFAULT)

    #----------------------------------------------------------    
    def desenhe_linha(self, par_pontos, cor_linha = COR_LINHA):
        '''(Console, list, list) -> None

        Recebe uma referência `self` a um objeto Console e
        uma lista `par_pontos` com as coordenadas de dois pontos.
        A função desenha uma linha linha entre esses pontos.
        '''
        # caso o método seja chamado sem um par de pontos
        if par_pontos == []: return None
        
        # atualize contador
        self.no_linhas += 1
        
        # apelidos
        canvas = self.canvas
        pena   = self.pena

        # defina a cor da linha 
        pena.color(cor_linha)

        # levante a pena para não deixar rastro na janela
        pena.penup()  

        # apelido para os dois pontos
        p0, p1 = par_pontos
        
        # leve a pena para o ponto p0
        pena.setposition(p0)

        # baixe a pena
        pena.pendown()

        # leve a pena para o ponto p1
        pena.setposition(p1)

        # levante a pena para terminar a linha
        pena.penup()  

    #----------------------------------------------------------    
    def no_call_dist(self):
        '''(Console) -> int

        Recebe uma referência `self` a um objeto Console e
        retorna o número de chamadas feitas ao método 
        desenhe_linhas(). O número de linhas deve ser o 
        número de chamadas feitas à função distancia() do 
        módulo NUSP_ep6.py.
        '''
        return self.no_linhas
    
    #----------------------------------------------------------    
    def exitonclick(self):
        '''(Console) -> None

        Recebe uma referência `self` e a um objeto Console e
        fecha a janela assim que seja feito um click sobre ela.
        '''
        print("\nClick na janela da animação para fechá-la.")
        self.canvas.exitonclick()

    #----------------------------------------------------------    
    def reset(self):
        '''(Console) -> None

        Recebe uma referência `self` e a um objeto Console e
        fecha a janela assim que seja feito um click sobre ela.
        '''
        self.canvas.clear()
        self.setup()
        self.desenhe_pontos()
