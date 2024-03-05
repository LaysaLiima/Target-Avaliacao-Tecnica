import json

with open('arquivo.json', 'r') as arquivo:
    dados_faturamento = json.load(arquivo)

valores_diarios = [(dado['dia'], dado['valor']) for dado in dados_faturamento if dado.get('valor', 0) != 0]

dia_min, valor_min = valores_diarios[0]
for dia,valor in valores_diarios:
    if valor < valor_min:
        valor_min = valor 
        dia_min = dia

dia_max, valor_max = valores_diarios[0]
for dia,valor in valores_diarios:
    if valor > valor_max:
        valor_max = valor 
        dia_max = dia

print(f"O maior valor diário foi de R${valor_max:.2f}, no dia {dia_max}")
print(f"O menor valor diário foi de R${valor_min:.2f}, no dia {dia_min}")

soma_dos_valores_diarios = 0
for dia, valor in valores_diarios:
    soma_dos_valores_diarios += valor

media_mensal = soma_dos_valores_diarios / len(valores_diarios)

count = 0
for dia, valor in valores_diarios:
    if valor > media_mensal:
        count += 1
print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {count}")