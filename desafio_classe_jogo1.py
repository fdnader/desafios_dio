"""

Escrevendo as classes de um Jogo:

**O Que deve ser utilizado**

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões
- Funções
- Classes e Objetos

## Objetivo:

Crie uma classe generica que represente um herói de uma aventura e que possua as seguintes propriedades:

Nome ; Idade ; Tipo (guerreiro, mago, monge, ninja)

Além disso, deve ter um método chamado atacar que deve atender os seguientes requisitos:

Exibir a mensagem:
 "o {tipo} atacou usando {ataque}" ; Aonde o {tipo} deve ser concatenando ao tipo que está na propriedade da classe e o {ataque} deve seguir uma descrição diferente conforme o tipo, sendo:
=> se mago -> ataque exibir (usou magia); se guerreiro -> ataque exibir (usou espada); se monge -> ataque exibir (usou artes marciais); se ninja -> ataque exibir (usou shuriken)

## Saída

Ao final deve se exibir uma mensagem:

- "o {tipo} atacou usando {ataque}"
  ex: mago atacou usando magia
  guerreiro atacou usando espada
 
"""
# 1. Criação da classe Heroi
class Heroi:

    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
# # 2. Método para atacar
    def atacar(self):
        ataques = {
            
            "Mago": "Magia",
            "Guerreiro": "Espada",
            "Monge": "Artes Marciais",
            "Ninja": "Shuriken"
        }
        ataque = ataques.get(self.tipo, "ataque desconhecido")

        print(f"O {self.tipo} atacou usando {ataque}")

# 3. Criação de instâncias da classe Heroi        
heroi1 = Heroi("Jin-woo", 30, "Mago")
heroi2 = Heroi("Sung", 19, "Guerreiro")
heroi3 = Heroi("Anng", 255, "Monge")
heroi4 = Heroi("Naruto", 14, "Ninja")

# 4. Exibição das informações do herói
print(f"Nome: {heroi1.nome}, Idade: {heroi1.idade}, Tipo: {heroi1.tipo}")
print(f"Nome: {heroi2.nome}, Idade: {heroi2.idade}, Tipo: {heroi2.tipo}")
print(f"Nome: {heroi3.nome}, Idade: {heroi3.idade}, Tipo: {heroi3.tipo}")
print(f"Nome: {heroi4.nome}, Idade: {heroi4.idade}, Tipo: {heroi4.tipo} \n")
# 5. Exibição do ataque de cada herói
heroi1.atacar()
heroi2.atacar()
heroi3.atacar()
heroi4.atacar() 
# 6. Exibição de uma mensagem final
print("\nTodos os heróis atacaram com sucesso!".upper())

