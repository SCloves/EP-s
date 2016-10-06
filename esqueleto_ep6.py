"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome :
  NUSP :
  Turma: MAE, MAP, MAT, IF, Poli, ECA, etc
  Prof.:

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma referência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  Exemplo:
  - O algoritmo Quicksort foi baseado em 
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html

  Não altere as assinaturas/protótipos/cabeçalhos das funções.
"""

# módulo necessário para usar a função sqrt()
import math

# módulo com funções auxiliares usadas pela função main()
import util

#-------------------------------------------------------------
# constantes

# opções de funções
MAC0110 = '0'
MAC0122 = '1'

# deseja animação
SIM = 's'
NAO = 'n'

# prompts usados pelo programa
PROMPT_NO_PONTOS  = "no. de pontos >>> "
PROMPT_SEMENTE    = "semente >>> "
PROMPT_ALGORITMO  = "função ('%s' para mac0110, '%s' para mac0122) >>> " %(MAC0110,MAC0122)
PROMPT_ANIMACAO   = "\nexecutar animação ('%s' para sim, '%s' para não) >>> " %(SIM,NAO)

# mensagens de erro
ERRO_PONTOS  = "ERRO >>> número de pontos deve ser um inteiro positivo > 1 ('%s')"
ERRO_SEMENTE = "ERRO >>> semente deve ser um inteiro ('%s')"
ERRO_OPCAO   = "ERRO >>> opção inválida ('%s')"

# cada ponto é representando por um par [x,y] 
X = 0 # abscissa do ponto é o valor na posição 0 
Y = 1 # ordenada do ponto é o valor na posição 1 

#------------------------------------------------------------
def main():
    '''(None) -> None

    Coordena a execução do programa. Faz a leitura

        - do número de pontos a serem gerados aleatoriamente;
        - da semente para o gerador de números aleatório; e
        - da opção da função que deve ser executada.

    Chama a função escolhida e apresenta um pequeno relatório.

    Pergunta se uma animação da função escolhida deve ser executada.
    Se a reposta for SIM chama a função que apresenta a animação.

    O main() pode ser utilizado _parcialmente_ depois que as 
    funções

        - distancia() e
        - mac0110() 
 
    tiverem sido implementadas.

    Completamente utilizável depois que as funções 

        - par_mais_proximo_faixa() e
        - mac0122()
 
    tiverem sido implementadas.

    Não altere nada nesta função.
    '''
    global distancia
    
    # leia o número de pontos
    n_str = input(PROMPT_NO_PONTOS)

    # verifique se n_str é um string representando um inteiro positivo
    try:
        n = int(n_str)
        if n <= 1: raise ValueError
    except ValueError:
        print(ERRO_PONTOS %n_str)
        return None
    
    # leia a semente
    semente_str = input(PROMPT_SEMENTE)

    # verifique se semente_str é um string representando um inteiro
    try:
        semente = int(semente_str)
    except ValueError:
        print(ERRO_SEMENTE %semente_str)
        return None

    # escolha a função a ser executada
    opcao = input(PROMPT_ALGORITMO).strip()
    if   opcao == MAC0110:
        # selecionou mac0110()
        par_mais_proximo = mac0110
        
        # os pontos não devem ser ordenados da esquerda
        # para a direita
        ordene_x = False 

    elif opcao == MAC0122:
        # selecionou mac0122()
        par_mais_proximo = mac0122

        # os pontos devem ser ordenados da esquerda
        # para a direita
        ordene_x = True
        
    else:
        print(ERRO_OPCAO %opcao)
        return None

    # crie uma lista de n pontos aleatórios 
    lista_pontos = util.gere_pontos(n,semente)
    
    # execute a função selecionada    
    util.execute(par_mais_proximo,lista_pontos,ordene_x)

    # pergunte se a animação deve ser executada
    opcao = input(PROMPT_ANIMACAO).strip()
    if opcao == SIM:
        distancia = distancia_animacao
        util.animacao(par_mais_proximo,lista_pontos)
    elif opcao != NAO:
        print(ERRO_OPCAO %opcao)
        return None
    
    # termino normal... vaze    
    print("Fui!")

#----------------------------------------------------------
def distancia(p0, p1):
    ''' (list, list) -> float

    Recebe duas listas p0 e p1 com as coordenadas de dois 
    pontos pontos e calcula e retorna a distância euclidiana 
    entre eles.

    Nota: esta deve ser a primeira função a ser implementada.

    Exemplos:

    >>> distancia([0,0],[0,1])
    1.0
    >>> distancia([0,0],[1,0])
    1.0
    >>> distancia([0,0],[1,1])
    1.4142135623730951
    >>> distancia([1,2],[1,1])
    1.0
    >>> distancia([1,2],[-1,1])
    2.23606797749979
    >>> 
    '''
    print("Vixe! Ainda não fiz a função distancia().")
    return 0

#-------------------------------------------------------------    
def mac0110(p, r, lista_pontos):
    '''(int, int, list) -> float, list

    Recebe dois inteiros `p` e `r` e uma lista `lista_pontos` 
    de coordenadas de pontos. A função calcula e retorna 
 
        - a menor distância d entre um par de pontos
          em lista_pontos[p:r], e 

        - uma lista [[x0,y0],[x1,y1]] com as coordenadas de 
          dois pontos que estão a distância d.

    Para calcular a distância entre dois pontos, digamos,
    p0 = [x0,y0] e p1 = [x1,y1] está função __deve__ utilizar
    a função distancia() fazendo chamadas como

        distancia(p0,p1)  

    Se lista_pontos[p:r] não tem um par de pontos a função 
    __deve__ retornar None, []

    Nota: esta deve ser a segunda função a ser implementada.
          Após a implementação e teste desta função o main()
          pode ser utilizado parcialmente. Tente.

    Exemplos:

    >>> lista = [[0,0],[1,0],[0,1],[1,1]]
    >>> mac0110(0,4,lista)
    (1.0, [[0, 0], [1, 0]])
    >>> mac0110(1,4,lista)
    (1.0, [[1, 0], [1, 1]])
    >>> mac0110(2,4,lista)
    (1.0, [[0, 1], [1, 1]])
    >>> mac0110(3,4,lista)
    (None, [])
    >>> lista = [[0,0],[0.5,0.5],[0,2],[2,3]]
    >>> mac0110(0,4,lista)
    (0.7071067811865476, [[0, 0], [0.5, 0.5]])
    >>> mac0110(0,3,lista)
    (0.7071067811865476, [[0, 0], [0.5, 0.5]])
    >>> mac0110(1,3,lista)
    (1.5811388300841898, [[0.5, 0.5], [0, 2]])
    >>> lista = [[0,0],[0,1],[-1,-1],[1,1],[1,0]]
    >>> lista = [[0,3],[-1,-1],[0,0],[2,2],[3,0]]
    >>> mac0110(0,5,lista)
    (1.4142135623730951, [[-1, -1], [0, 0]])
    >>> mac0110(3,5,lista)
    (2.23606797749979, [[2, 2], [3, 0]])
    >>>   
    '''
    print("Vixe! Ainda não fiz a função mac0110().")
    return None, []

#-------------------------------------------------------------
def par_mais_proximo_faixa(d, p, q, r, lista_pontos):
    '''(float, int, int, int, list) -> float, list

    Recebe um float `d`, inteiros `p`, `q` e `r` tais que
    p <= q <= r e uma lista `lista_pontos` de coordenadas 
    de pontos em __ordem crescente__ em relação às suas 
    coordenadas x (= pontos ordenados da esquerda para a 
    direita). 

    A função retorna 

        - a menor distância d_faixa entre dois pontos 
          p0_faixa e p1_faixa tais que:

             . um ponto p0_faixa está em lista_pontos[p:q];
             . um ponto p1_faixa está em lista_pontos[q:r]; e
             . ambos os pontos estão na faixa de largura d
               em relação a q;

        - a lista [p0_faixa,p1_faixa] desses dois pontos que 
          estão à distância d_faixa.

    Para calcular a distância entre dois pontos, digamos,
    p0 = [x0,y0] e p1 = [x1,y1] está função __deve__ utilizar
    a função distancia() fazendo chamadas como

        distancia(p0,p1)  

    Se a faixa de largura d em relação a q não possui um par 
    de pontos satisfazendo as condições acima a função 
    __deve__ retornar None, []

    Nota: esta deve ser a terceira função a ser implementada.

    Exemplos:

    >>> pontos = [[-4, 0], [-2, 0], [0, 3], [1, -1], [2, 2], [3, 2]]
    >>> par_mais_proximo_faixa(8,0,3,6,pontos)
    (2.23606797749979, [[0, 3], [2, 2]])
    >>> par_mais_proximo_faixa(6,0,3,6,pontos)
    (2.23606797749979, [[0, 3], [2, 2]])
    >>> par_mais_proximo_faixa(36,0,3,6,pontos)
    (2.23606797749979, [[0, 3], [2, 2]])
    >>> par_mais_proximo_faixa(1,0,3,6,pontos)
    (None, [])
    >>> par_mais_proximo_faixa(2,0,3,6,pontos)
    (2.23606797749979, [[0, 3], [2, 2]])
    >>> par_mais_proximo_faixa(1.2,0,3,6,pontos)
    (2.23606797749979, [[0, 3], [2, 2]])
    >>> par_mais_proximo_faixa(2,0,2,6,pontos)
    (None, [])
    >>> par_mais_proximo_faixa(3,0,2,6,pontos)
    (3.1622776601683795, [[-2, 0], [1, -1]])
    >>> par_mais_proximo_faixa(4,0,2,6,pontos)
    (3.1622776601683795, [[-2, 0], [1, -1]])
    >>> par_mais_proximo_faixa(1,1,2,6,pontos)
    (None, [])
    >>> par_mais_proximo_faixa(2.5,1,2,6,pontos)
    (3.1622776601683795, [[-2, 0], [1, -1]])
    >>> par_mais_proximo_faixa(2,3,4,6,pontos)
    (3.1622776601683795, [[1, -1], [2, 2]])
    >>> par_mais_proximo_faixa(2,4,4,6,pontos)
    (None, [])
    >>> par_mais_proximo_faixa(2,4,5,6,pontos)
    (1.0, [[2, 2], [3, 2]])
    '''
    print("Vixe! Ainda não fiz a função par_mais_proximo_faixa().")
    return None, []

#-------------------------------------------------------------
def mac0122(p, r, lista_pontos):
    '''(int, int, list) -> float, list

    Recebe inteiros `p` e `q` e uma lista `lista_pontos` 
    de coordenadas de pontos em __ordem crescente__ em relação
    às suas coordenadas x (=pontos ordenados da esquerda para 
    a direita). 

    A função retorna 
 
        - a menor distância d entre um par de pontos
          em lista_pontos[p:r], e 

        - uma lista [p0,p1] com as coordenadas de dois 
          pontos em lista_pontos[p:r] que estão a distância d.

    Para calcular a distância entre dois pontos, digamos,
    p0 = [x0,y0] e p1 = [x1,y1] está função __deve__ utilizar
    a função distancia() fazendo chamadas como

        distancia(p0,p1)  

    Se lista_pontos[p:r] não tem um par de pontos a função 
    __deve__ retornar None, []

    Esta função deve ser uma implementação da simplificação do 
    algoritmo de Shamos e Hoey como descrito no enunciado do 
    exercício programa.

    Nota: esta deve ser a quarta e última função a ser implementada.

    Exemplos:

    >>> pontos = [[-4, 0], [-2, 0], [0, 3], [1, -1], [2, 2], [3, 2]]
    >>> mac0122(0,6,pontos)
    (1.0, [[2, 2], [3, 2]])
    >>> mac0122(0,3,pontos)
    (2.0, [[-4, 0], [-2, 0]])
    >>> mac0122(3,6,pontos)
    (1.0, [[2, 2], [3, 2]])
    >>> mac0122(4,6,pontos)
    (1.0, [[2, 2], [3, 2]])
    >>> mac0122(3,5,pontos)
    (3.1622776601683795, [[1, -1], [2, 2]])
    >>> mac0122(4,5,pontos)
    (None, [])
    >>> 
    '''
    print("Vixe! Ainda não fiz a função mac0122().")
    return None, []

#------------------------------------------------------------
def distancia_animacao(p0, p1, dist=distancia):
    '''(list, list) -> float

    Recebe dois pontos `p0` e `p1`, desenha uma linha e retorna 
    a distância entre eles. 

    Não altere está função.

    Não utilize está função.
    '''
    util.desenhe_linha(p0,p1)
    return dist(p0,p1)

#------------------------------------------------------------
# A chama main() mais adiante inicia a execução do programa.
# Comente as linhas a seguir enquanto estiver testando
# __individualmente__ cada função.
if __name__ == "__main__":
   main()
