# Crie um programa que receba um número inteiro e calcule o fatorial desse número usando uma estrutura de repetição.

n=int(input("Digite um numero para ver seu fatorial:"))
print(f"Calculando {n}!")
c = n
f = 1
fatorial = c
while c> 0:
    print("{}".format(c),end = " ")
    print("x"if c >1 else "=",end = " ")
    
    f = f*c
    c-=1
    
print(f)








