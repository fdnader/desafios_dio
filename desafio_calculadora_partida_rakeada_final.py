"""

 #  Calculadora de partidas Rankeadas
**O Que deve ser utilizado**

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões
- Funções

## Objetivo:

Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

Se vitórias for menor do que 10 = Ferro
Se vitórias for entre 11 e 30 = Bronze
Se vitórias for entre 21 e 50 = Prata
Se vitórias for entre 51 e 70 = Ouro
Se vitórias for entre 81 e 90 = Diamante
Se vitórias for entre 91 e 100= Lendário
Se vitórias for maior ou igual a 101 = Imortal

## Saída

Ao final deve se exibir uma mensagem:
"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**"

"""
def nivel_rankeada(vitorias, derrotas):
    saldo = vitorias - derrotas
    nivel = [(10, "ferro"), (30, "bronze"), (50, "prata"), (70, "ouro"), (90, "diamante"), (100, "lendario"), (101, "imortal")]
    for i in nivel:
        if saldo <= i[0]:
            return i[1]
    return "imortal"
print("==============================================")
print("BEM-VINDO A CALCULADORA DE PARTIDAS RANQUEADAS")
print("==============================================")
while True:
    try:
        nome = str(input("Digite o seu nome: "))	
        print("==============================================")
        vitorias = int(input("Digite o número de vitórias: "))
        print("==============================================")
        derrotas = int(input("Digite o número de derrotas: "))
        print("==============================================")
        break
    except ValueError:
        print("==============================================")
        print("Por favor, insira um número válido. Tente novamente")
        print("==============================================")
nivel = nivel_rankeada(vitorias, derrotas)
saldo = vitorias - derrotas
print(f"O herói {nome} tem {vitorias} vitórias e {derrotas} derrotas (saldo: {saldo}). Nível: \033[1m{nivel.upper()}\033[0m")