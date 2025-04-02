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

