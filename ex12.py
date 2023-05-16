# 
# autores:
# Michel

# data: 16/05/2023
# descrição:

# 12. uma função em Python que simula a vacinação de pessoas 
# e armazena as informações em um dicionário:

# funcao que simula a vacinacao de pessoas
def vacinacao():
    quantidade_pessoas = int(input("Quantas pessoas serão vacinadas? "))

    dados_vacinacao = {}

    for i in range(1, quantidade_pessoas + 1):
        nome = input(f"Informe o nome da pessoa {i}: ")
        idade = int(input(f"Informe a idade da pessoa {i}: "))
        vacinada = input(f"A pessoa {i} já foi vacinada? (S/N) ").upper()

        dados_vacinacao[nome] = {
            "idade": idade,
            "vacinada": vacinada == "S"
        }
    
    return dados_vacinacao


# uso da função
dados = vacinacao() # chamada da função e atribuição do retorno a variável dados 
print(type(dados))  # exibição do tipo da variável dados (dicionario)

# Exemplo de acesso aos dados:
for nome, info in dados.items(): # iteração sobre os itens do dicionario dados 
    print(f"Nome: {nome}")
    print(f"Idade: {info['idade']}")
    print(f"Vacinada: {'Sim' if info['vacinada'] else 'Não'}")
    print()
