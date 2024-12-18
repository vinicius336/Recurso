def processar_dados(dados):
    resultado = []
    for num in dados:
        if num % 2 == 0:
            resultado.append(num ** 2)
        else:
            resultado.append(num ** 3)
    return sum(resultado)

valores = [2, 5, 8, 7, 10]
resultado_final = processar_dados(valores)
print(f"O resultado final é: {resultado_final}")