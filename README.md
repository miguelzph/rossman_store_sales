## 1. Contexto
- Reunião Mensal de Resultados
- CFO solicitou a previsão de vendas das próximas 6 semanas para cada loja
## 2. Desafio
### Problema
- Definição de budget para a reforma das lojas
###Causas
- Predição atual de vendas apresetava muita divergência
- O processo de previsão de vendas é baseado apenas em experiências passadas
- Toda a previsão de vendas é realizada manualmente para as mais de 1000 lojas
- A visualização da previsão é limitada ao compudator local.
### Solução
- Usar Machine Learning para realizar a previsão de vendas de todas as lojas
- Disponibilzar as previsões de venda no smartphone

## 3. Desenvolvimento da Solução

### Informações disponíveis

Id - an Id that represents a (Store, Date) duple within the test set
Store - Id único da loja
Sales - O valor vendido para o dia (valor a ser previsto)
Customers - Quantidade de clientes que visitaram a loja em um dia
Open - indica se a loja abriu ou não: 0 = closed, 1 = open
StateHoliday - Indica feriado estadual.  a = public holiday, b = Easter holiday, c = Christmas, 0 = None
SchoolHoliday - Indica se a loja foi afetada por um feriado escolar
StoreType - Diferencia os 4 tipos de loja: a, b, c, d
Assortment - Descreve o nível de sortimento de produtos da loja: a = basic, b = extra, c = extended
CompetitionDistance - Distância em metros do competidor mais próximo
CompetitionOpenSince[Month/Year] - Fornece o ano e o mês aproximados em que o concorrente mais próximo foi aberto
Promo - Indica se uma loja está realizando uma promoção naquele dia
Promo2 - É uma promoção contínua e consecutiva para algumas lojas: 0 = a loja não está participando, 1 = a loja está participando
Promo2Since[Year/Week] - Descreve o ano e a semana do calendário em que a loja começou a participar da Promo2
PromoInterval - Descreve os intervalos consecutivos em que a Promo2 é iniciada, nomeando os meses em que a promoção é iniciada novamente.

### Mapa mental de hipóteses
<img src="/img/MindMapHypothesis.png" alt="Hypothesis" style="height: 100px; width:100px;"/>
