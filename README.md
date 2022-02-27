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

<strong>Id</strong> - an Id that represents a (Store, Date) duple within the test set <br>
<strong>Store</strong> - Id único da loja <br>
<strong>Sales</strong> - O valor vendido para o dia (valor a ser previsto) <br>
<strong>Customers</strong> - Quantidade de clientes que visitaram a loja em um dia <br>
<strong>Open</strong> - indica se a loja abriu ou não: 0 = closed, 1 = open <br>
<strong>StateHoliday</strong> - Indica feriado estadual.  a = public holiday, b = Easter holiday, c = Christmas, 0 = None <br>
<strong>SchoolHoliday</strong> - Indica se a loja foi afetada por um feriado escolar <br>
<strong>StoreType</strong> - Diferencia os 4 tipos de loja: a, b, c, d <br>
<strong>Assortment</strong> - Descreve o nível de sortimento de produtos da loja: a = basic, b = extra, c = extended <br>
<strong>CompetitionDistance</strong> - Distância em metros do competidor mais próximo <br>
<strong>CompetitionOpenSince[Month/Year]</strong> - Fornece o ano e o mês aproximados em que o concorrente mais próximo foi aberto <br>
<strong>Promo</strong> - Indica se uma loja está realizando uma promoção naquele dia <br>
<strong>Promo2</strong> - É uma promoção contínua e consecutiva para algumas lojas: 0 = a loja não está participando, 1 = a loja está participando <br>
<strong>Promo2Since[Year/Week]</strong> - Descreve o ano e a semana do calendário em que a loja começou a participar da Promo2 <br>
<strong>PromoInterval</strong> - Descreve os intervalos consecutivos em que a Promo2 é iniciada, nomeando os meses em que a promoção é iniciada novamente. <br>

### Mapa mental de hipóteses
<img src="/img/MindMapHypothesis.png" alt="Hypothesis" style="height: 720px; width:1366px;"/>

### Hipóteses validadas

1. Lojas com maior sortimento deveriam vender mais
2. Lojas com competidores mais proximos deveriam vender menos
3. Lojas que têm competidores mais tempo deveriam vender mais (estabilização)
4. Lojas com promoções ativas por mais tempo deveriam vender mais
5. Lojas com mais dias de promoção deveriam vender mais
6. Lojas com mais promoções consecutivas deveriam vender mais
7. Lojas abertas durante o feriado de Natal deveriam vender mais
8. Lojas deveriam vender mais ao longo dos anos
9. Lojas deveriam vender mais no segundo semestre do ano
10. Lojas deveriam vender mais depois do dia 10 de cada mês
11. Lojas deveriam vender menos aos finais de semana
12. Lojas deveriam vender menos durante os feriados escolares

## 4. Métricas de Machine Learning 

![image](https://user-images.githubusercontent.com/64989931/155896420-9d2bbcd2-beb1-4035-a874-b85e62253bf0.png)

### Predictions 
![image](https://user-images.githubusercontent.com/64989931/155896416-2b2f95e9-a21a-4065-9160-22056720bc04.png)


## 5. Deploy do Modelo
- Deploy da API de previsão no Heroku 

- Consulta de previsão via Telegram BOT <br>
![ezgif com-gif-maker](https://user-images.githubusercontent.com/64989931/155896886-018fccfe-2258-4493-a62d-36a837fd5747.gif)

