import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files

df1 = pd.read_excel("./datasets/Aracaju.xlsx")
df2 = pd.read_excel("./datasets/Fortaleza.xlsx")
df3 = pd.read_excel("./datasets/Natal.xlsx")
df4 = pd.read_excel("./datasets/Recife.xlsx")
df5 = pd.read_excel("./datasets/Salvador.xlsx")

print(df5.head())

df = pd.concat([df1,df2,df3,df4,df5])

print(df.head())

print(df.tail())

print(df.sample(5))

print(df.dtypes)

df["LojaID"] = df["LojaID"].astype("object")

print(df.dtypes)

print(df.head())

print(df.isnull().sum())

print(df["Vendas"].fillna(df["Vendas"].mean(), inplace=True))

df["Vendas"].mean()

df.isnull().sum()

df.sample(15)

df["Vendas"].fillna(0, inplace=True)

df.dropna(inplace=True)

df.dropna(subset=["Vendas"], inplace=True)

df.dropna(how="all", inplace=True)

df["Receita"] = df["Vendas"].mul(df["Qtde"])

df.head()

df["Receita/Vendas"] = df["Receita"] / df["Vendas"]

df.head()

df["Receita"].max()

df["Receita"].min()

df.nlargest(3, "Receita")

df.nsmallest(3, "Receita")

df.groupby("Cidade")["Receita"].sum()

df.sort_values("Receita", ascending=False).head(10)

df["Data"] = df["Data"].astype("int64")

df.dtypes

df["Data"] = pd.to_datetime(df["Data"])

df.dtypes

df.groupby(df["Data"].dt.year)["Receita"].sum()

df["Ano_Venda"] = df["Data"].dt.year

df.sample(5)

df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)

df.sample(5)

df["Data"].min()

df["diferenca_dias"] = df["Data"] - df["Data"].min()

df.sample(5)

df["trimestre_venda"] = df["Data"].dt.quarter

df.sample(5)

vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]

vendas_marco_19.sample(20)


# Visualização de Dados

df["LojaID"].value_counts(ascending=False)

df["LojaID"].value_counts(ascending=False).plot.bar()

df["LojaID"].value_counts().plot.barh()

df["LojaID"].value_counts(ascending=True).plot.barh()

df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie()

df["Cidade"].value_counts()




df["Cidade"].value_counts().plot.bar(title="Total vendas por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas")



df["Cidade"].value_counts().plot.bar(title="Total vendas por Cidade", color="red")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas")


plt.style.use("ggplot")


df.groupby(df["mes_venda"])["Qtde"].sum().plot(title = "Total Produtos vendidos x mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend()


df.groupby(df["mes_venda"])["Qtde"].sum()


df_2019 = df[df["Ano_Venda"] == 2019]


df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum()


df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "o")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend()


plt.hist(df["Qtde"], color="orangered")


plt.scatter(x=df_2019["dia_venda"], y = df_2019["Receita"])


df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "v")
plt.title("Quantidade de produtos vendidos x mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend()
plt.savefig("grafico QTDE x MES.png")



plt.style.use("seaborn")

arq = files.upload()

df = pd.read_excel("AdventureWorks.xlsx")

df["Valor Venda"].sum()

df["custo"] = df["Custo Unitário"].mul(df["Quantidade"])

round(df["custo"].sum(), 2)

df["lucro"]  = df["Valor Venda"] - df["custo"] 

round(df["lucro"].sum(),2)

df["Tempo_envio"] = df["Data Envio"] - df["Data Venda"]

df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days

df.head(1)

df["Tempo_envio"].dtype

df.groupby("Marca")["Tempo_envio"].mean()

df.isnull().sum()

df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum()

pd.options.display.float_format = '{:20,.2f}'.format

lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum().reset_index()
lucro_ano

df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)


df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto")


df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title="Lucro x Ano")
plt.xlabel("Ano")
plt.ylabel("Receita")

df.groupby(df["Data Venda"].dt.year)["lucro"].sum()

df_2009 = df[df["Data Venda"].dt.year == 2009]

df_2009.head()


df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title="Lucro x Mês")
plt.xlabel("Mês")
plt.ylabel("Lucro")


df_2009.groupby("Marca")["lucro"].sum().plot.bar(title="Lucro x Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal')


df_2009.groupby("Classe")["lucro"].sum().plot.bar(title="Lucro x Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal')


df["Tempo_envio"].describe()


plt.boxplot(df["Tempo_envio"])


plt.hist(df["Tempo_envio"])

df["Tempo_envio"].min()

df['Tempo_envio'].max()

df[df["Tempo_envio"] == 20]

df.to_csv("df_vendas_novo.csv", index=False)