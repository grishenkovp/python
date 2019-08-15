import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Считываем данные из файла 'SalesByRegion'
df_sales = pd.read_csv('D:/.../SalesByRegion.csv',
                       sep=';')
# Определяем тип загруженных столбцов и производим необходимые замены. Столбец 'date' - даты, остальные столбцы кроме
# 'amount' - категориальные данные
# print(df_sales.dtypes)
df_sales['date'] = pd.to_datetime(df_sales['date'], format='%d.%m.%Y')
list_category ={'shop','region', 'city', 'brand', 'product'}
for name_category in list_category:
    df_sales[name_category] = df_sales[name_category].astype('category')
# print(df_sales.info())
# Построим дополнительные столбцы 'year' и 'month', которые станут новыми аналитическим срезами. Удаляем  столбец 'date',
# который нам больше не нужен. Задаем новый порядок столбцов.
df_sales['year'] = df_sales['date'].dt.year
df_sales['month_number'] = df_sales['date'].dt.month
df_sales['month'] = df_sales['date'].dt.month_name().str.slice(stop=3)
df_sales.drop(['date'], axis='columns', inplace=True)
column_titles = ['year','month_number','month','region','city', 'shop', 'brand','product', 'amount']
df_sales = df_sales.reindex(columns=column_titles)
# print(df_sales.head(5))
# *********************************************************************************************************************
#  Объем продаж по месяцам суммарно за три года
df_sales_month = df_sales.groupby(by=['month_number','month'],as_index=False).agg({'amount':sum})
df_sales_month.drop(['month_number'], axis=1, inplace=True)
df_sales_month['amount'] = df_sales_month['amount'].apply(lambda x: round(x/1000000,1))
# print(df_sales_month)
# Строим график
# #fig = plt.figure()
# plt.bar(df_sales_month['month'], df_sales_month['amount'], color='red')
# plt.title('Помесячный объем продаж')
# plt.ylim(45,55)
# plt.ylabel('млн руб')
# #fig.savefig('df_sale_month.png')  # сохраняем полученный график для презентации
# plt.show()
# *********************************************************************************************************************
#  Структура продаж "регион-магазин"
df_sales_region_shop = df_sales.groupby(by=['region','shop'], as_index=False).agg({'amount':sum})
df_sales_region_shop['amount'] = df_sales_region_shop['amount'].apply(lambda x: round(x/1000000,1))
# print(df_sales_region_shop)
# Определим долю продаж разных типов магазинов в каждом регионе
df_sales_region_shop_total = df_sales_region_shop.groupby(by=['region'],as_index=False)['amount'].sum()
df_sales_region_shop_total.rename(columns={'amount': 'total_amount'}, inplace=True)
df_sales_region_shop = pd.merge(df_sales_region_shop,df_sales_region_shop_total, how='left', on='region')
df_sales_region_shop['percent'] = df_sales_region_shop['amount']/df_sales_region_shop['total_amount']
df_sales_region_shop['percent']  = df_sales_region_shop['percent'].apply(lambda x: "{0:.2f}%".format(x * 100))
# print(df_sales_region_shop)
# Строим график
# #fig = plt.figure()
# heatmap_data = df_sales_region_shop.pivot('shop','region','amount')
# plt.imshow(heatmap_data, cmap='hot',interpolation='none')
# plt.colorbar()
# plt.title('Тепловая карта')
# plt.xticks(range(len(heatmap_data.columns)),heatmap_data.columns)
# plt.yticks(range(len(heatmap_data)),heatmap_data.index)
# #fig.savefig('/.../.png')  # сохраняем полученный график для презентации
# plt.show()
# **********************************************************************************************************************
# Определим три ведущих бренда для каждого региона
df_sales_region_brand = df_sales.groupby(by=['region','brand'],as_index=False)['amount'].sum()
df_sales_region_brand = df_sales_region_brand.sort_values(['region','amount'],ascending=[True, False])\
    .groupby(by='region').head(3)
# print(df_sales_region_brand)
# **********************************************************************************************************************
# Определим три товара, которые приносят больше всего выручки по всем брендам (т.е. три SKU, которые одновременно
# есть в линейке сразу всех производителей и при этом эти позиции приносят набольший оборот)
df_sales_brand_product= df_sales.groupby(by=['brand','product'],as_index=False)['amount'].sum()
df_sales_brand_product = df_sales_brand_product.pivot(index='product', columns='brand', values='amount')
df_sales_brand_product.columns.name = None
df_sales_brand_product = df_sales_brand_product.rename(index=str, columns=str).reset_index()
df_sales_brand_product['val'] = df_sales_brand_product.iloc[:,1:].count(axis=1)
df_sales_brand_product= df_sales_brand_product[df_sales_brand_product['val']==25]
df_sales_brand_product['total_amount'] = df_sales_brand_product.iloc[:,1:].sum(axis=1)
df_sales_brand_product = df_sales_brand_product.sort_values(['total_amount'],ascending=False).head(3)
print(df_sales_brand_product[['product','total_amount']])
# Строим график
#fig = plt.figure()
labels = df_sales_brand_product['product']
sizes = df_sales_brand_product['total_amount']
plt.pie(sizes,labels=labels,autopct='%1.1f%%', shadow=True, startangle=90)
#fig.savefig('df_sale_month.png')  # сохраняем полученный график для презентации
plt.show()
