# Funcao de leitura de um numero em qualquer base #############################

# Entrada: Inteiro numerico que representa quantidade de simbolos na base
# Saida: lista num que contem os digitos antes da virgula, lista posvirgula 
#        que contem os digitos depois da virgula
def leiaNum(base):
  num = []            # Lista que vai conter os valores antes da virgula (parte decimal)
  posvirgula = []     # Lista que vai conter os valores depois da virgula (parte fracionaria)
  lendoFrac = False   # False - Lendo a lista num; True - lendo a lista posvirgula
  leuNegativo = False # Diz se ja leu um valor negativo ou nao - indica final do loop
  
  # Enquanto nao ler um valor negativo
  while(leuNegativo == False):
    valor = input("Digite um novo numero, virgula para ponto decimal, ou negativo para finalizar: ")
    
    # Se o valor lido for numerico
    if valor != ",":    
      valor=int(valor)  # Conversao para tipo inteiro - possibilita operacoes
      
      # Se estiver no intervalo de numeros na base e nao leu virgula
      if valor < base and valor >= 0 and lendoFrac == False: 
        num.append(valor)
      
      # Fora do intervalo e continua leitura
      elif valor >= base: 
        print("Numero fora do intervalo, tente novamente.") 
      
      # Dentro do intervalo e leu virgula
      elif valor < base and valor >= 0 and lendoFrac == True:
        posvirgula.append(int(valor))
      
      # Usuario deseja finalizar a leitura de valores
      elif valor < 0:
        leuNegativo = True
    
    # Se o valor lido for nao numerico - indica inicio de leitura da parte fracional
    elif valor == ",": 
      lendoFrac = True

  return num,posvirgula

# Conversao de um numero em uma base qualquer para o numero em base decimal ###
# Entrada: A porcao inteira do numero, Porcao fracionaria do numero, a base de
#          em que ambas porcoes do numero se encontra
# Saida: Tupla contendo respectivamente a porcao inteira  e a porcao 
#        fracionaria de entrada em base decimal 
def convertB10(num,numvirg,bEntrada):
  soma = 0      # Acumulador das conversoes dos digitos da parte inteira
  somaVirg = 0  # Acumulador das conversoes do digitos da parte fracionaria
  
  # Para todos os digitos na lista de digitos da parte inteira
  for i in range(len(num)):
    # Acumula o produto entre o digito e a base elevada a posicao do digito
    soma += num[i] * bEntrada **(len(num) - i - 1) 
    
  for j in range(len(numvirg)):
     # Acumula o produto entre o digito e a base elevada a posicao do digito
    somaVirg += numvirg[j] * bEntrada **(-(j + 1))
  
  return soma,somaVirg

# Conversao de um numero em base decimal para uma base qualquer especificada
# Entrada:  A porcao inteira do numero, Porcao fracionaria do numero, a base
#          em que o numero deve ser convertido e com quantas casas decimais de
#          precisao
# Saida: lista num que contem os digitos antes da virgula, lista posvirgula 
#        que contem os digitos depois da virgula
def convertBX(num,numvirg,bSaida,precisao):
  saidanum = []   # Lista que vai conter os digitos inteiros na base de saida
  saidavirg = []  # Lista que vai conter os digitos fracionarios na base de saida
  
  # Enquanto eh possivel realizar divisoes inteiras pela base
  while num >= bSaida:
    saidanum.append(num % bSaida) # Pega o resto da divisao pela base e insere na lista de digitos
    num = num // bSaida # Divisao inteira para pegar o proximo digito

  saidanum.append(num % bSaida) # Pega o ultimo resto apos sair do while
  saidanum.reverse() # Inverte a lista (devido ao processo de conversao ser feito de tras para frente)

  cont = 0 # Contador para verificar quantas casas decimais o numero fracionario ja possui
  while numvirg != 0 and cont < precisao:
    numvirg = numvirg * bSaida
    saidavirg.append(int((numvirg // (1)))) 
    numvirg = numvirg - (numvirg // (1))
    cont += 1 # Apos insercao acrescenta o contador de digitos

  return saidanum,saidavirg

############### MAIN FUNCTION #################################################
# Exemplo de execucao para transformar 15FA3,AA em base 16 para base 2
# Qual a base de entrada?
  # 16 ENTER
# Digite um novo numero, virgula para ponto decimal, ou negativo para finalizar:
  # 1  ENTER
  # 5  ENTER
  # 15 ENTER
  # 10 ENTER
  # 3  ENTER
  # ,  ENTER
  # 10 ENTER
  # 10 ENTER
  # -1 ENTER
# Qual a base de saida do numero?
  # 2  ENTER
# Quantas casas de precisao deseja ter apos a virgula?
  # 8  ENTER
# Saida: 1 0 1 0 1 1 1 1 1 1 0 1 0 0 0 1 1 , 1 0 1 0 1 0 1

  
bEntrada = int(input("Qual a base de entrada numero? "))
numero,numvirg = leiaNum(bEntrada)
numero,numvirg = convertB10(numero,numvirg,bEntrada)

bSaida = int(input("Qual a base de saida do numero? "))
if numvirg%1 != 0:
    precisao = int(input("Quantas casas de precisao deseja ter apos a virgula? "))
else:
    precisao = 0
    
s1,s2 = convertBX(numero,numvirg,bSaida,precisao)
print(*s1,",",*s2)