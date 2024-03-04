faturamentos = {
'SP' : 67836.43,
'RJ' : 36678.66, 
'MG' : 29229.88,
'ES' : 27165.48,
'Outros' : 1949.53
}

valor_total = sum(faturamentos.values())

porcentagem_SP = (67836.43 / valor_total)* 100;
porcentagem_RJ =(36678.66 / valor_total)* 100;
porcentagem_MG = (29229.88 / valor_total)* 100;
porcentagem_ES = (27165.48 / valor_total)* 100;
porcentagem_Outros = (1949.53 / valor_total)* 100;

print(f"O percentual do estado de São Paulo foi  {porcentagem_SP:.2f}%" )
print(f"O percentual do estado de Rio de Janeiro  foi {porcentagem_RJ:.2f}% ")
print(f"O percentual do estado de Minas Gerais foi  {porcentagem_MG:.2f}%")
print(f"O percentual do estado de Espirito Santo foi  {porcentagem_ES:.2f}%");
print(f"O percentual do estado de Outros foi  {porcentagem_Outros:.2f}%");		  