faturamentos = {
'SP' : 67836.43,
'RJ' : 36678.66, 
'MG' : 29229.88,
'ES' : 27165.48,
'Outros' : 1949.53
}

valor_total = sum(faturamentos.values())
faturamentos_porcentagem = {
'SP' : (faturamentos['SP'] / valor_total)* 100,
'RJ' : (faturamentos['RJ'] / valor_total)* 100, 
'MG' : (faturamentos['MG'] / valor_total)* 100,
'ES' : (faturamentos['ES'] / valor_total)* 100,
'Outros' : (faturamentos['Outros'] / valor_total)* 100
}

print(f"O percentual do estado de São Paulo foi {faturamentos_porcentagem['SP']:.2f}%" )
print(f"O percentual do estado de Rio de Janeiro foi {faturamentos_porcentagem['RJ']:.2f}% ")
print(f"O percentual do estado de Minas Gerais foi {faturamentos_porcentagem['MG']:.2f}%")
print(f"O percentual do estado de Espirito Santo foi {faturamentos_porcentagem['ES']:.2f}%");
print(f"O percentual do estado de Outros foi {faturamentos_porcentagem['Outros']:.2f}%");		  