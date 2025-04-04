#-------------------------------
#1. Criar uma lista e acessar um elemento
#-------------------------------
lista = [10,20,30,40,50]
print(lista[2]) # Exibe o terceiro elemento (índice 2)

#--------------------------------
#2. Modificar um elemento da lista
#--------------------------------
lista = [10,20,30,40,50]
lista[1] = 99 # Substituir o segundo elemento (índice 1) por 99
print(lista)

#--------------------------------
#3.Adicionar e remover elementos da lista

lista = [10,20,30,40,50]
lista.append(60)  # Adiciona 60 ao final
lista.pop(0) # Remove o primeiro elemento
print(lista)

#-----------------------------------
#4.Ordenar a lista
#----------------------------------

lista = [10,20,30,40,50]
lista.sort() # Ordem crescente
print("Ordenado crescente:", lista)
lista.sort(reverse=True) # Ordem decrescente
print("Ordem decrescente:", lista)

#------------------------------------
#5. Soma e media dos valores da lista
#------------------------------------

lista = [10,20,30,40,50]
soma = sum(lista)
media = soma / len(lista)
print(f"soma: {soma}, Média: {media}")

#-------------------------------------
#6.Crie uma tupla com 4 nomes e exiba o segundo nome.
#-------------------------------------
tupla = ("luiz", "Luiza", "Maria", "João")
print(tupla[2])


#-------------------------------------
#7.Converta uma tupla para uma lista, altere um valor e converta de volta para tupla.
#--------------------------------------

tupla = (0,1,2,3,4,5)
lista = [0,1,2,3,4,5]
lista [3] = 15 # substituir o quarto elemento (índice 3) por 15
tupla = (lista)
print(tupla)

#--------------------------------------
#8. Verifique se um determinado valor existe dentro da tupla.
#-------------------------------------

tupla = (2,4,6,8,10)
if 8 in tupla:
   print("sim, 8 existe dentro da tupla")


#--------------------------------------
#9.Crie duas tuplas e una ambas em uma nova tupla.
#--------------------------------------

tupla1 = (3,5,7,9)
tupla2 = (2,4,6,8)
tupla3 = tupla1 + tupla2
print(tupla3)

#----------------------------------------
#10. Use index() para encontrar a posição de um elemento na tupla.
#----------------------------------------

tupla = (10,20,30,15,27,45,50)
tupla = tupla.index(27)
print(tupla)

#--------------------------------------------
#11. Crie um array NumPy com 5 números e some 2 a cada elemento.
#--------------------------------------------

import numpy as np
my_array = np.array([3,4,5,6,7])
print(my_array+2)


#-------------------------------------------
#12. Multiplique todos os elementos do array por 3.
#-------------------------------------------

import numpy as np
my_array = np.array([3,4,5,6,7])
print(my_array*3)

#--------------------------------------------
#13. Crie dois arrays e some os elementos correspondentes.
#--------------------------------------------

import numpy as np
array1 = np.array([2,4,7,9,6])
array2 = np.array([1,3,5,6,10])
array3 = array1 + array2
print(array3)

#---------------------------------------------
#14. Calcule a média e o desvio padrão de um array.
#---------------------------------------------
#-----------------------------------------
#15. Exiba apenas os números pares do array.
#-----------------------------------------

array = np.array([1,2,3,5,6,8,9])
print(array[array % 2 == 0]) 


#----------------------------------------
#16.Crie um dicionário com 3 produtos e seus preços. Acesse o preço de um produto específico.
#---------------------------------------

produtos = {
   'Anel': 350,
   'Esmalte': 9,
   'Tesoura': 15

}

print(produtos['Anel']) 

#------------------------------------------
#17. Adicione um novo produto e altere o preço de um existente.
#-----------------------------------------


produtos['Corretivo'] = 5

produtos['esmalte'] = 3

print(produtos)


#--------------------------------------------
#18. Remova um item do dicionário.
#------------------------------------------


produtos.pop('anel')

print(produtos)

#----------------------------------------
#19.Percorra o dicionário e exiba cada chave e valor.
#----------------------------------------

for chave, valor in produtos.items():
   print(f"produto: {chave}, preço: R${VALOR}")


