import json

with open('arquivo.json', 'r') as arquivo:
    dados_faturamento = json.load(arquivo)
print(dados_faturamento)  

valores_diarios = [dado['valor'] for dado in dados_faturamento if dado.get('valor', 0)!=0]

faturamento_max = max(valores_diarios)
faturamento_min = min(valores_diarios)

print(f"O maior valor de faturamento ocorrido em um dia do mês foi de R${faturamento_max} no dia 16")
print(f"O menor valor de faturamento ocorrido em um dia do mês foi de R${faturamento_min} no dia 14")

soma_dos_valores_diarios = 0

for valor in valores_diarios:
    soma_dos_valores_diarios += valor

media_mensal = soma_dos_valores_diarios / len(valores_diarios)

count = 0

for valor in valores_diarios:
    if valor > media_mensal:
        count += 1
print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {count}")