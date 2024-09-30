soma = 0

for i in range (5):
    numero = float(input(f"inserir numero {i + 1}: "))
    soma += numero
    
media = soma / 5

print(f" a media dos numeros e {media}")