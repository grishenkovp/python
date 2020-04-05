import pandas as pd
import numpy as np

from plotly.subplots import make_subplots
import plotly.graph_objects as go

df_manager_plan = pd.read_excel('db/sale_plan_manager.xlsx')
df_product_plan = pd.read_excel('db/sale_plan_product.xlsx')
df_region_plan = pd.read_excel('db/sale_plan_region.xlsx')
df_all_fact = pd.read_excel('db/sale_fact_manager_region_product.xlsx')

# **********************************************************************************************************************
fig = make_subplots(
    rows=2, cols=2,
    specs=[[{"type": "scatter"},{"type": "bar"}],[{"type": "scatter"},{"type": "table"}]],
    subplot_titles=("Регионы (план-факт)", "Общие продажи по месяцам (факт)", "Продукты (план-факт)", "Топ-7 продаж")
)

# **********************************************************************************************************************
df_all_fact_groupby_region = df_all_fact.groupby(by=['region'])['value'].sum()
df_all_fact_groupby_region.sort_index(ascending=True, inplace=True)
x1 = df_all_fact_groupby_region.index
y1_1 = df_all_fact_groupby_region.values
df_region_plan.sort_values(['region'],ascending=True, inplace=True)
y1_2 =df_region_plan['value']
fig.add_trace(go.Scatter(x=x1, y=y1_1, mode='markers', name='регионы_факт'), row=1, col=1)
fig.add_trace(go.Scatter(x=x1, y=y1_2, mode='lines',name='регионы_план'),row=1, col=1)
# **********************************************************************************************************************
df_all_fact['month'] = df_all_fact['date'].dt.month
df_all_fact_groupby_month = df_all_fact.groupby(by=['month'])['value'].sum()
x2 = df_all_fact_groupby_month.index
y2 = df_all_fact_groupby_month.values
fig.add_trace(go.Bar(x=x2, y=y2, name='мес_факт'), row=1, col=2)

# **********************************************************************************************************************
df_all_fact_groupby_product = df_all_fact.groupby(by=['product'])['value'].sum()
df_all_fact_groupby_product.sort_index(ascending=True, inplace=True)
x3 = df_all_fact_groupby_product.index
y3_1 = df_all_fact_groupby_product.values
df_product_plan.sort_values(['product'],ascending=True, inplace=True)
y3_2 =df_product_plan['value']
fig.add_trace(go.Scatter(x=x3, y=y3_1,  mode='markers', name='продукты_факт'), row=2, col=1)
fig.add_trace(go.Scatter(x=x3, y=y3_2, mode='lines',name='продукты_план'),row=2, col=1)
# **********************************************************************************************************************
df_table = df_all_fact.sort_values('value',ascending=False)
df_table['date'] = df_all_fact['date'].apply(lambda x: x.strftime("%m/%d/%Y"))
df_table = df_table.drop(['month'],axis=1)
df_table = df_table.head(7)
fig.add_trace(go.Table(
    header=dict( values=["Date", "Manager", "Region", "Product", "Value"], font=dict(size=10), align="left" ),
    cells=dict(values=[df_table[k].tolist() for k in df_table.columns[0:]],align = "left")
                    ), row=2, col=2)
# **********************************************************************************************************************

fig.update_layout( height=650, width=1250, title_text="Структура продаж за 2019", showlegend=True)
fig.write_html('dashboard.html', auto_open=True)

