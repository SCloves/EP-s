
# coding: utf-8

# In[1]:

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
import math as mt

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
    
    x1 = p0[0]
    x2 = p1[0]
    y1 = p0[1]
    y2 = p1[1]
    x = (x2 - x1)**2 + (y2 -y1)**2
    raiz = mt.sqrt(x)
    
    return raiz
#-------------------------------------------------------------    
def mac0110(p, r, lista_pontos):
    
    lista = lista_pontos[p:r]
    n = len(lista)
    
    if len(lista) == 1:
        return None, []
    
    menor_distancia = distancia(lista[0], lista[1])
    pontos = [lista[0], lista[1]]
    
    for i in range(n):
        for j in range(n):
            if i != j:
                dist = distancia(lista[i], lista[j])
            
                if dist < menor_distancia:
                    menor_distancia = dist
                    pontos = [lista[i], lista[j]]
    
    return menor_distancia, pontos
#-------------------------------------------------------------
def par_mais_proximo_faixa(d, p, q, r, lista_pontos):
   
    inicio = lista_pontos[q][0] - d # início da faixa
    final = lista_pontos[q][0] + d  # final da faixa
    
    p0_faixa = []
    for i in range(p, q):
        if lista_pontos[i][0] > inicio: # p0_faixa só terá pontos dentro da faixa esquerda
            p0_faixa.append(lista_pontos[i])
    
    p1_faixa = []
    for i in range(q, r):
        if lista_pontos[i][0] < final:
            p1_faixa.append(lista_pontos[i]) # p1_faixa só terá pontos dentro da faixa direita
            
    
    if len(p0_faixa) == 0 or len(p1_faixa) == 0:
        return None, []
    
    menor_d_faixa = distancia(p0_faixa[0], p1_faixa[0])
    pontos = [p0_faixa[0], p1_faixa[0]]
    
    for i in p0_faixa:
        for j in p1_faixa:
            d_faixa = distancia(i, j)
            if d_faixa < menor_d_faixa:
                menor_d_faixa = d_faixa
                pontos = [i, j]
                
    return float(menor_d_faixa), pontos 

#-------------------------------------------------------------
def mac0122(p, r, lista_pontos):
    '''(int, int, list) -> float, list

    Recebe inteiros `p` e `r` e uma lista `lista_pontos` 
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
    resultado = []
    nova_lista = lista_pontos[p:r]
    n = len(nova_lista)
    if n <= 1:
        return None, []
    
    if n == 2:
        d = distancia(nova_lista[0], nova_lista[1])
        resultado.append(nova_lista[0])
        resultado.append(nova_lista[1])
        return d, resultado
    
    meio = int(n/2)
    
    d_esq, p0 = mac0122(p, meio, nova_lista) # aqui estão as chamadas recursivas 
    d_dir, p1 = mac0122(meio, r, nova_lista)
    
    
    if d_esq == None and type(d_dir) == float:
        d =  abs(p1[0][0])
      
        d_faixa , p_faixa = par_mais_proximo_faixa(d, 0, meio, n, nova_lista)
    
        if d_faixa == None:
            return None, []
        if d_faixa > d_dir:
            return d_dir, p1
        else:
            return d_faixa, p_faixa
    elif d_dir == None and type(d_esq) == float:
        d =  abs(p0[0][0])
        d_faixa, p_faixa = par_mais_proximo_faixa(d, 0, meio, n, nova_lista)
        if d_faixa == None:
            return None, []
        elif d_faixa > d_esq:
            return d_esq, p0
        else:
            return d_faixa, p_faixa
    elif d_esq == None and d_dir == None:
        return None, []
    
    else:
        d = min(d_esq, d_dir)
        d_faixa, p_faixa = par_mais_proximo_faixa(d, 0, meio, n, nova_lista)
        
        if d_faixa == None:
            if d_esq <= d_dir:
                return d_esq, p0
            else:
                return d_dir, p1
        
        if d_esq <= d_dir and d_esq <= d_faixa:
            return d_esq, p0
        if d_dir <= d_esq and d_dir <= d_faixa:
            return d_dir, p1
        else:
            return d_faixa, p_faixa

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


# In[1]:

t = -1
abs(t)


# In[8]:

d = 1
float(d)


# In[ ]:



