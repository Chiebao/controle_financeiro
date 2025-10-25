import pandas as pd


arquivo = "./controle_financeiro.xlsx"

receitas = pd.read_excel(arquivo, sheet_name="Receitas")
despesas = pd.read_excel(arquivo, sheet_name="Despesas")

receitas["Data"] = pd.to_datetime(receitas["Data"])
despesas["Data"] = pd.to_datetime(despesas["Data"])

receitas["Mes_Ano"] = receitas["Data"].dt.to_period("M")
despesas["Mes_Ano"] = despesas["Data"].dt.to_period("M")

df_receitas = receitas.groupby(
    "Mes_Ano")["Valor"].sum().reset_index(name="Receita_Total")
df_despesas = despesas.groupby(
    "Mes_Ano")["Valor"].sum().reset_index(name="Despesa_Total")

financeiro = pd.merge(df_receitas, df_despesas,
                      on="Mes_Ano", how="outer").fillna(0)

financeiro["Lucro_Liquido"] = financeiro["Receita_Total"] - \
    financeiro["Despesa_Total"]
financeiro["Margem_Lucro_%"] = (
    financeiro["Lucro_Liquido"] / financeiro["Receita_Total"]) * 100
financeiro["Margem_Lucro_%"] = financeiro["Margem_Lucro_%"].round(2)

financeiro.to_excel("base_tratada.xlsx", index=False)

print("✅ Base tratada gerada com sucesso! Arquivo salvo como: base_tratada.xlsx")
print(financeiro)
