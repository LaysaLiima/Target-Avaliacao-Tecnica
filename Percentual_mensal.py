faturamento_SP = 67836.43
faturamento_RJ = 36678.66 
faturamento_MG = 29229.88
faturamento_ES = 27165.48
faturamento_Outros = 1949.53

valor_total = faturamento_SP  + faturamento_RJ + faturamento_MG + faturamento_ES + faturamento_Outros

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