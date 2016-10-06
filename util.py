#############################################################
#                                                           #
#  MAC0122 Princípos de Desenvolvimento de Algoritmos       #
#                                                           #
#  MÓDULO util.py                                           #
#                                                           #
#  Contém funções auxiliares do EP6                         #
#                                                           #
#  Não altere nada neste arquivo.                           #
#                                                           #
#  Não altere o nome do arquivo.                            #
#                                                           #     
#############################################################

# módulo para geração de números aleatorios
import random

# para cronometrar o tempo das funções
import time

# módulo responsável pela animação
import console

# constantes
# retângulo onde os pontos serão gerados é definido por
#    - canto inferior esquerdo [X_MIN,Y_MIN] e
#    - canto superior direito  [X_MAX,Y_MAX].
X_MIN = -1024
Y_MIN = -1024
X_MAX =  1024
Y_MAX =  1024
CANTOS = [[X_MIN,Y_MIN],[X_MAX,Y_MAX]]

# cada ponto é representando por um para [x,y] 
X = 0 # abscissa do ponto é valor na posição 0 
Y = 1 # ordenada do ponto é valor na posição 1 

#-------------------------------------------------------------    
def gere_pontos(n, semente, cantos=CANTOS):
    '''(int, int, list) -> list

    Recebe um número inteiro não negativo `n`, um número inteiro 
    `semente` e uma lista `cantos` com de pares de números inteiros 
    [[x_min,y_min],[x_max,y_max]] que definem uma região retangular do 
    plano cartesiano. 

    A função cria e retorna uma lista de coordenadas inteiras de 
    n pontos gerados aleatoriamente na região retangular. 
    Assim, para cada ponto [x,y] na lista retornada temos que:

        - x e y são números inteiros;
        - x_min <= x < x_max
        - y_min <= y < y_max

    O valor de semente é usado para inicializar o gerador de números 
    aleatórios do Python.

    Não altere está função.
    '''
    # avise que estamos trabalhando
    print("\ngere_pontos(): gerando %d pontos ..." %n)
    
    # crie a lista a ser retornada
    l_pontos = []
    
    # inicialize a semente do gerador 
    random.seed(semente)

    # cantos da região retangular
    x_min, y_min = cantos[0]
    x_max, y_max = cantos[1]

    # gere os pontos
    for i in range(n):
        # sorteie uma posição no retângulo 
        x = random.randrange(x_min,x_max)
        y = random.randrange(y_min,y_max)

        # coloque o ponto na lista
        l_pontos.append([x,y])

    # avise que terminamos o serviço e estamos voltando
    print("gere_pontos(): pontos gerados.")
    
    return l_pontos
    
#------------------------------------------------------------
def execute(par_mais_proximo, lista_pontos, ordene_x):
    '''(function, list, bool) -> None

    Recebe uma função `par_mais_proximo()`, uma lista de pontos
    `lista_pontos` e um booleano ordene_x. A função mede o consumo 
    de tempo e imprime pequeno um pequeno relatório referente
    a execução da chamada

        para_mais_proximo(0,len(lista_pontos),lista_pontos)

    Se ordene_x == True, antes dessa chamada, a lista de 
    ponto é ordenada em relação as coordenadas x (= da esquerda
    para a direita). O tempo dessa ordenação é levado em 
    consideração.

    Nota:

    https://docs.python.org/3.0/library/time.html#time.clock

    time.clock():

    On Unix, return the current processor time as a floating point
    number expressed in seconds. The precision, and in fact the very
    definition of the meaning of “processor time”, depends on that of
    the C function of the same name, but in any case, this is the
    function to use for benchmarking Python or timing algorithms.

    On Windows, this function returns wall-clock seconds elapsed since
    the first call to this function, as a floating point number, based
    on the Win32 function QueryPerformanceCounter. The resolution is
    typically better than one microsecond.
    '''
    # começe a cronometrar 
    start = time.clock()

    # função mac0122() necessita pré-processamento
    if ordene_x:
        # ordene os pontos de acordo com as coordenadas x (= abscissas)
        # chave = função que indica que a lista deve ser ordenada em relação
        #         a coordenada X
        print("\nexecute(): pontos sendo ordenados em relação a coordenada x...")
        lista_pontos.sort(key=chave)
        print("execute(): pontos ordenados.")
        
    # execute a função
    dist, par = par_mais_proximo(0,len(lista_pontos),lista_pontos)

    # trave o cronômetro 
    end = time.clock()

    # calcule o tempo gasto
    elapsed = end - start

    print("\nResultado: ")
    print("  par mais próximo  =", par)
    # caso ainda não tenha implementado a função
    if dist == None:
        print("  menor distância   = None")
    else:
        print("  menor distância   = %.2f" %dist)
    print("  tempo de execução = %.2fs" %elapsed)


#------------------------------------------------------------
def animacao(par_mais_proximo, lista_pontos):
    '''(function, list) -> None

    Recebe uma função `par_mais_proximo()` e uma lista de pontos
    `lista_pontos`. A função apresenta uma pequena aninamação da
    execução da chamada

        para_mais_proximo(0,len(lista_pontos),lista_pontos)
    '''
    global janela
    
    # crie uma janela com os pontos
    janela = console.Console(lista_pontos, CANTOS)

    # contemple os pontos
    pause()

    # determine o par mais próximo
    print("\nVeja sua função em ação...")
    dist, par = par_mais_proximo(0,len(lista_pontos),lista_pontos)

    # contemple as linhas indicando chamadas à função distancia()
    pause()

    # mostre apenas um par mais próximo
    janela.reset()
    janela.desenhe_linha(par)

    # mostre pequeno relatório da execução da função
    no_chamadas_dist = janela.no_call_dist()
    print("\nResultado: ")
    print("  par mais próximo =", par)
    # caso ainda não tenha implementado a função
    if dist == None:
        print("  menor distância   = None")
    else:
        print("  menor distância   = %.2f" %dist)
    print("  no. chamadas da função distancia() = %d" %no_chamadas_dist)
        
    # contemple um par mais próximo antes de irmos embora
    janela.exitonclick()  

    
#------------------------------------------------------------
def pause(): 
    '''(None) -> None

    Para a execução do programa até que um ENTER seja teclado.

    Não altere está função
    '''
    input("\nPara continua, tecle ENTER _nesta_ janela. ")

#------------------------------------------------------------
def chave(ponto):
    ''' (list) -> valor

    Recebe uma lista e retorna o valor da posição X.

    Usado pelo método sort() para ordenar os pontos 
    de acordo com a coordenada X.
    '''
    return ponto[X]

#------------------------------------------------------------
def desenhe_linha(p0, p1):
    '''(function) -> function

    Recebe a função distancia, desenha uma linha e retorna 
    a distância entre os pontos.

    Não altere está função.
    '''
    if janela == None:
        print("ERRO >>> não estamos em uma animação")
        return None
    janela.desenhe_linha([p0,p1])
