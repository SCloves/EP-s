
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

  Nome : Cloves Adriano Paiva Sousa
  NUSP : 9292218
  Turma: MAE, MAP, MAT etc
  Prof.: Jose Coelho de Pina Junior

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  Exemplo:
  - O algoritmo Quicksort foi baseado em http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html

"""

'''
   TAREFA:
   Escreva a função conta_caracteres() e indice(), como definidas
       abaixo nesse esqueleto.
   Não modifique a função main().
   Implemente outras funções que você achar necessário.

'''

def main():
    nome = input("Digite o nome do arquivo: ")

    with open(nome, 'r', encoding='utf-8') as entrada:
        texto = entrada.read()

    caracter, quantidade = conta_caracteres( texto )

    i, n = 0, len(caracter)
    
    print("Quantidade de caracteres distintos no arquivo %s: %d"%( nome, n))
    print(" Caractere | Quantidade")

    while i<n:
        if caracter[i] == '\n':
            print("%10s | %d"%('\\n', quantidade[i]))
        elif caracter[i] == ' ':
            print("%10s | %d"%('branco', quantidade[i]))
        
        else:
            print("%10s | %d"%(caracter[i], quantidade[i]))
        i += 1
        
    print("\nFIM!\n")
        

def conta_caracteres( texto ):
    lista_0 = []
    lista_1 = []
    lista_2 = []
    
    # transforma o texto numa lista
    for i in texto:
        lista_0.append(i)
    
    for item in lista_0:
        # aqui eu uso a tão pedida função índice
        # que para mim não é a melhor maneira 
        # de se resolver esse problema, mas enfim...
        if indice(item, lista_1) == None: 
            lista_1.append(item)
            lista_2.append(conta_item(item, lista_0))
    
    return lista_1, lista_2 
            
# retorna o índice do caracter na lista_1 e None caso não exista na lista_1 
def indice(item, lista):       
    for i in range(len(lista)):
        if item == lista[i]:
            return i
            break
    return None

# conta quantas vezes o caracter aparece no texto
def conta_item(item, lista): 
    n = 0
    for i in lista:
        if item == i:
            n += 1
    return n
    

if __name__ == "__main__":
    main()





