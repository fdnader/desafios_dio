#   Desafio Classificador de nível de Herói

#  -> O Que deve ser utilizado**

#   - Variáveis
#   - Operadores
#   - Laços de repetição
#   - Estruturas de decisões

#  -> Objetivo

#   Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

#   Se XP for menor do que 1.000 = Ferro
#   Se XP for entre 1.001 e 2.000 = Bronze
#   Se XP for entre 2.001 e 5.000 = Prata
#   Se XP for entre 5.001 e 7.000 = Ouro
#   Se XP for entre 7.001 e 8.000 = Platina
#   Se XP for entre 8.001 e 9.000 = Ascendente
#   Se XP for entre 9.001 e 10.000= Imortal
#   Se XP for maior ou igual a 10.001 = Radiante

## Saída

#   Ao final deve se exibir uma mensagem:
#   "O Herói de nome **{nome}** está no nível de **{nivel}**"



nome_personagem = input("Digite o nome do personagem: ").upper()
xp = int(input("Digite a quantidade de experiência (XP) do personagem: "))

match xp:
    case xp if xp < 1000:
        nivel = "Ferro".upper()
    case xp if 1001 <= xp <= 2000:
        nivel = "Bronze".upper()
    case xp if 2001 <= xp <= 5000:
        nivel = "Prata".upper()
    case xp if 5001 <= xp <= 7000:
        nivel = "Ouro".upper()
    case xp if 7001 <= xp <= 8000:
        nivel = "Platina".upper()
    case xp if 8001 <= xp <= 9000:
        nivel = "Ascendente".upper()
    case xp if 9001 <= xp <= 10000:
        nivel = "Imortal".upper()
    case _:
        nivel = "Radiante".upper()

print(f"O herói \033[4m{nome_personagem}\033[0m está na categoria \033[4m{nivel}\033[0m, com \033[4m{xp}\033[0m pontos de experiência.")
