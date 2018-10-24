# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("\nOk!\n")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:\n")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: \n")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: \n")
print(data_list[1])

input("\nAperte Enter para continuar...")

# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras\n")

# TAREFA 1 ** INICIO **
# Loop para apresentar as 20 primeiras amostras
for index in range(1,21):
      print("Row {}: {}".format(index,data_list[index]))

# TAREFA 1 ** FIM **


# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("\nAperte Enter para continuar...\n")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras\n")

# TAREFA 2 ** INICIO **
# Loop para apresentar as 20 primeiros gêneros das amostras
for index in range(0,20):
      print("Row {} Gênero: {}".format(index+1,data_list[index][-2]))

# TAREFA 2 ** FIM **

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("\nAperte Enter para continuar...\n")

# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista

# TAREFA 3 ** INICIO
# Loop para adicionar as colunas(features) de uma lista em outra lista,
    for linhas in data:
        column_list.append(linhas[index])

    return column_list
# TAREFA 3 ** FIM


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras\n")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("\nAperte Enter para continuar...\n")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0

# TAREFA 4 ** INICIO
# Loop para realizar a contagem de cada gênero
for linha in data_list:
    if linha[-2].lower() == "male":
        male += 1
    elif linha[-2].lower() == "female":
        female += 1

# TAREFA 4 ** FIM


# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos:\n")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("\nAperte Enter para continuar...\n")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    male = 0
    female = 0

# TAREFA 5 ** INICIO
# Loop para realizar a contagem de cada gênero e retorno uma lista
    for linha in data_list:
            if linha[-2].lower() == "male":
                male += 1
            elif linha[-2].lower() == "female":
                female += 1

    return [male, female]

# TAREFA 5 ** FIM

print("\nTAREFA 5: Imprimindo o resultado de count_gender\n")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...\n")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list):
    answer = ""

# TAREFA 6 ** INICIO
# Função seguida de uma conversão para retornar uma string
    popular_gender = count_gender(data_list)
    if popular_gender[0] > popular_gender[1]:
        answer = 'Male'
    elif popular_gender[0] < popular_gender[1]:
        answer = 'Female'
    else:
        answer = "Equal"

    return answer

# TAREFA 6 ** FIM


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("\nAperte Enter para continuar...\n")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.

# TAREFA 7 ** INICIO
print("\nTAREFA 7: Verifique o gráfico!\n")
# Função para realizar a contagem de tipos de usuários

def count_user_type(data_list):
    customer = 0
    subscriber = 0

    for linha in data_list:
        if linha[-3].lower() == "customer":
            customer += 1
        elif linha[-3].lower() == "subscriber":
            subscriber += 1

    return [customer, subscriber]

# Apresentação do gráfico com as informações geradas pela função acima
user_type_list = column_to_list(data_list, -3)
types = ["Customer", "Subscriber"]
quantity = count_user_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por tipo de usuário')
plt.show(block=True)

# TAREFA 7 ** FIM

input("\nAperte Enter para continuar...\n")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))

# TAREFA 8 ** INICIO
# Variavel (answer) com a resposta da pergunta
answer = "Male + female não equivalem a len(data_list, pois  esse set (coluna) possui células com valores nulos. Resultando em uma condição como falsa."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("\nAperte Enter para continuar...\n")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

# TAREFA 9 ** INICIO

for i in trip_duration_list: # trip MIN
    i = float(i)
    if min_trip==0.:
        min_trip = i
    elif i < min_trip:
        min_trip = i


for i in trip_duration_list: # trip MAX
    i = float(i)
    if max_trip==0.:
        max_trip = i
    elif i > max_trip:
        max_trip = i


for i in trip_duration_list: # Principal - Mean
    i = float(i)
    mean_trip += i
mean_trip = mean_trip / len(trip_duration_list)

# Fonte : https://www.safaribooksonline.com/library/view/python-data-structures/9781786467355/83b3af24-5563-475e-8aa1-0f5e63c8ec37.xhtml
# Fonte: https://www.quora.com/How-do-I-find-the-median-value-in-Python
# Cálculo da 
ordem = sorted(float(i) for i in trip_duration_list)
size = len(ordem)
indice = (size - 1) // 2
if size % 2:
    median_trip = ordem[indice]
else:
    median_trip = (ordem[indice] + ordem[indice+1]) / 2

# TAREFA 9 ** FIM


print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("\nMin: ", min_trip, "\nMax: ", max_trip, "\nMédia: ", mean_trip, "\nMediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("\nAperte Enter para continuar...\n")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()


# TAREFA 10 ** Inicio
# Variavel (start_stations) para apresentação das estações
start_stations = set(column_to_list(data_list, 3))

# TAREFA 10 ** FIM

print("\nTAREFA 10: Imprimindo as start stations:\n")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("\nAperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:

# aqui o trecho  de instru;'oes'

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "no"

def count_items(column_list):
    item_types = []
    count_items = []
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
