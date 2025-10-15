## Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# A operação pode ser soma, subtração, multiplicação ou divisão.
# Depois exiba o resultado da operação.

# Solicita dois números como entrada
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Solicita a operação desejada
operacao = input("Digite a operação (+, -, *, /): ")

# Realiza a operação e exibe o resultado
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = (abs(num1 - num2))
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero!"
else:
    resultado = "Erro: Operação inválida!"  

print("Resultado:", resultado)


# --- IGNORE ---