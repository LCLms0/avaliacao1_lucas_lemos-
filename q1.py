n=float(input("Digite um número e lhe direi se ele é par ou impar,além disso irei dizer se ele é negativo,positivo ou zero:   "))
while n < 0:
    if n % 2 == 0  :
        print(f"{n} é par e é um número negativo")
    else:
        print(f"{n} é impar e é um número negativo")
    break
while n > 0 :
    if n % 2 == 0 :
        print(f"{n} é par e é um número positivo")
    else:
        print(f"{n} é impar e é um número positivo")
    break
while n == 0:
    if n % 2 == 0  :
        print(f"{n} é par e é um número igual a zero")
    else:
        print(f"{n} é impar e é um número igual a zero")
    break

