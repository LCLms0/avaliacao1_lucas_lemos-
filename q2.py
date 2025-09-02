produtos_menor_50 = 0
produtos_maior_50 = 0
soma_produtos = 0
total_de_produtos_vendidios= int(input("digite a quantidade de produtos vendidos:  "))
for i in range(0,total_de_produtos_vendidios):
    produto=float(input("Digite o valor do produto:  "))
    soma_produtos += produto
    if produto > 50 :
        produtos_maior_50 += 1
    if produto < 50:
        produtos_menor_50 += 1
print(f"ao todo esses produtos custaram {soma_produtos}")
print(f"os produtos maiores que 50$ foram {produtos_maior_50}")
print(f"os produtos menores que 50$ foram {produtos_menor_50}")
