## Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

# Solicita uma palavra como entrada
palavra = input("Digite uma palavra: ")

# Verifica se a palavra é um palíndromo
if palavra == palavra[::-1]:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")

    
# --- IGNORE ---
