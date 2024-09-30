numero = int(input("Insira um número para calcular o fatorial: "))

fatorial = 1

if numero == 0:
    fatorial = 1 
else:
    for i in range(1, numero + 1):
        fatorial = fatorial * i 

print("O fatorial de", numero, "é:", fatorial)
