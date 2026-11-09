# Controle Financeiro Empresarial — Nexa Solutions

Análise financeira ponta a ponta de uma empresa fictícia: tratamento dos dados em Python e dashboard interativo no Power BI para acompanhar receita, despesa, lucro e margem mês a mês.

> **Dados simulados.** A Nexa Solutions é fictícia e a base foi criada para estudo e portfólio.

![Dashboard no Power BI](Captura%20de%20tela%202025-10-25%20095436.png)

---

## Problema

Uma empresa que só olha o faturamento não percebe quando está perdendo dinheiro. O objetivo foi responder, mês a mês: **quanto entrou, quanto saiu, quanto sobrou e o que puxou o resultado.**

## O que foi feito

1. **Base de dados** em Excel com 200 lançamentos de receita (5 categorias) e 250 de despesa (8 categorias, fixas e variáveis), de janeiro a junho de 2025.
2. **Tratamento em Python** (`finac.py`): leitura das duas abas, conversão de datas, agrupamento por mês, junção de receitas e despesas e cálculo de lucro líquido e margem. O resultado sai em `base_tratada.xlsx`.
3. **Dashboard no Power BI** (`controle_financeiro.pbix`): evolução do lucro, margem por mês, receita × despesa, tabela mensal e card de meta, com versão para celular.
4. **Página web** (`index.html`) para apresentar o dashboard e os insights a quem não tem o Power BI.

## Resultados da análise

| Mês | Receita | Despesa | Lucro | Margem |
|---|---:|---:|---:|---:|
| Jan | R$ 210.219 | R$ 187.329 | R$ 22.890 | 10,9% |
| Fev | R$ 205.529 | R$ 170.873 | R$ 34.656 | 16,9% |
| Mar | R$ 176.572 | R$ 205.907 | **−R$ 29.335** | **−16,6%** |
| Abr | R$ 169.833 | R$ 174.160 | −R$ 4.327 | −2,6% |
| Mai | R$ 222.465 | R$ 158.560 | R$ 63.905 | 28,7% |
| Jun | R$ 156.010 | R$ 157.397 | −R$ 1.387 | −0,9% |
| **Semestre** | **R$ 1.140.628** | **R$ 1.054.226** | **R$ 86.402** | **7,6%** |

**Principais achados**

- **Metade dos meses deu prejuízo.** Março, abril e junho fecharam no vermelho, apesar de o semestre ter lucro.
- **Março foi o pior mês por causa do marketing.** Foram R$ 59 mil em marketing, o maior gasto mensal de uma única categoria no período, num mês de receita abaixo da média.
- **Não existe um "vilão" único nas despesas.** Nenhuma categoria passa de 15% do total; marketing (14,5%) e energia (14,4%) lideram. Reduzir custo aqui exige ajuste em várias frentes, não um corte só.
- **52% das despesas são fixas**, o que deixa a margem sensível a meses de receita mais fraca.

## Tecnologias

`Python` `Pandas` `openpyxl` `Excel` `Power BI` `HTML` `CSS`

## Estrutura

```
/
├── controle_financeiro.xlsx   # Base original (abas Receitas e Despesas)
├── finac.py                   # Tratamento e cálculo dos indicadores
├── base_tratada.xlsx          # Saída do script, usada no Power BI
├── controle_financeiro.pbix   # Dashboard
├── index.html                 # Página de apresentação do projeto
└── Captura de tela *.png      # Prints do dashboard (desktop e celular)
```

## Como executar

```bash
pip install pandas openpyxl
python finac.py
```

O script gera `base_tratada.xlsx`. Para ver o dashboard, abra `controle_financeiro.pbix` no Power BI Desktop.

## Próximos passos

- Análise de rentabilidade por categoria de receita
- Projeção de fluxo de caixa para os meses seguintes
- Atualização automática da base no Power BI

---

**Luana Godoy** · Estudante de Análise e Desenvolvimento de Sistemas
[LinkedIn](https://www.linkedin.com/in/luana-chiebao) · [GitHub](https://github.com/Chiebao)
